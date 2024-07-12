from datetime import datetime
from typing import Callable, Optional

from xtquant import (
    xtdata,
    xtdatacenter as xtdc
)
from filelock import FileLock, Timeout

from vnpy.event import EventEngine
from vnpy.trader.gateway import BaseGateway
from vnpy.trader.object import (
    OrderRequest,
    CancelRequest,
    SubscribeRequest,
    ContractData,
    TickData,
    HistoryRequest,
    OptionType,
)
from vnpy.trader.constant import (
    Exchange,
    Product
)
from vnpy.trader.utility import (
    ZoneInfo,
    get_file_path,
    round_to
)

# 交易所映射
EXCHANGE_VT2XT: dict[str, Exchange] = {
    Exchange.SSE: "SH",
    Exchange.SZSE: "SZ",
    Exchange.BSE: "BJ",
    Exchange.SHFE: "SF",
    Exchange.CFFEX: "IF",
    Exchange.INE: "INE",
    Exchange.DCE: "DF",
    Exchange.CZCE: "ZF",
    Exchange.GFEX: "GF",
}

EXCHANGE_XT2VT: dict[str, Exchange] = {v: k for k, v in EXCHANGE_VT2XT.items()}
EXCHANGE_XT2VT["SHO"] = Exchange.SSE
EXCHANGE_XT2VT["SZO"] = Exchange.SZSE


# 其他常量
CHINA_TZ = ZoneInfo("Asia/Shanghai")       # 中国时区


# 合约数据全局缓存字典
symbol_contract_map: dict[str, ContractData] = {}


class XtGateway(BaseGateway):
    """
    VeighNa用于对接迅投研的实时行情接口。
    """

    default_name: str = "XT"

    default_setting: dict[str, str] = {
        "token": "",
        "股票市场": ["是", "否"],
        "期货市场": ["是", "否"],
        "期权市场": ["是", "否"]
    }

    exchanges: list[str] = list(EXCHANGE_VT2XT.keys())

    def __init__(self, event_engine: EventEngine, gateway_name: str) -> None:
        """构造函数"""
        super().__init__(event_engine, gateway_name)

        self.md_api: "XtMdApi" = XtMdApi(self)

    def connect(self, setting: dict) -> None:
        """连接交易接口"""
        token: str = setting["token"]
        stock_active: bool = setting["股票市场"] == "是"
        futures_active: bool = setting["期货市场"] == "是"
        option_active: bool = setting["期权市场"] == "是"

        self.md_api.connect(token, stock_active, futures_active, option_active)

    def subscribe(self, req: SubscribeRequest) -> None:
        """订阅行情"""
        self.md_api.subscribe(req)

    def send_order(self, req: OrderRequest) -> str:
        """委托下单"""
        pass

    def cancel_order(self, req: CancelRequest) -> None:
        """委托撤单"""
        pass

    def query_account(self) -> None:
        """查询资金"""
        pass

    def query_position(self) -> None:
        """查询持仓"""
        pass

    def query_history(self, req: HistoryRequest) -> None:
        """查询历史数据"""
        return None

    def close(self) -> None:
        """关闭接口"""
        pass


class XtMdApi:
    """行情API"""

    lock_filename = "xt_lock"
    lock_filepath = get_file_path(lock_filename)

    def __init__(self, gateway: XtGateway) -> None:
        """构造函数"""
        self.gateway: XtGateway = gateway
        self.gateway_name: str = gateway.gateway_name

        self.inited: bool = False
        self.subscribed: set = set()

        self.token: str = ""
        self.stock_active: bool = False
        self.futures_active: bool = False
        self.option_active: bool = False

    def onMarketData(self, data: dict) -> None:
        """行情推送回调"""
        for xt_symbol, buf in data.items():
            for d in buf:
                xt_symbol: str = next(iter(data.keys()))
                symbol, xt_exchange = xt_symbol.split(".")
                exchange = EXCHANGE_XT2VT[xt_exchange]

                tick: TickData = TickData(
                    symbol=symbol,
                    exchange=exchange,
                    datetime=generate_datetime(d["time"]),
                    volume=d["volume"],
                    turnover=d["amount"],
                    open_interest=d["openInt"],
                    gateway_name=self.gateway_name
                )

                contract = symbol_contract_map[tick.vt_symbol]
                tick.name = contract.name

                bp_data: list = d["bidPrice"]
                ap_data: list = d["askPrice"]
                bv_data: list = d["bidVol"]
                av_data: list = d["askVol"]

                tick.bid_price_1 = round_to(bp_data[0], contract.pricetick)
                tick.bid_price_2 = round_to(bp_data[1], contract.pricetick)
                tick.bid_price_3 = round_to(bp_data[2], contract.pricetick)
                tick.bid_price_4 = round_to(bp_data[3], contract.pricetick)
                tick.bid_price_5 = round_to(bp_data[4], contract.pricetick)

                tick.ask_price_1 = round_to(ap_data[0], contract.pricetick)
                tick.ask_price_2 = round_to(ap_data[1], contract.pricetick)
                tick.ask_price_3 = round_to(ap_data[2], contract.pricetick)
                tick.ask_price_4 = round_to(ap_data[3], contract.pricetick)
                tick.ask_price_5 = round_to(ap_data[4], contract.pricetick)

                tick.bid_volume_1 = bv_data[0]
                tick.bid_volume_2 = bv_data[1]
                tick.bid_volume_3 = bv_data[2]
                tick.bid_volume_4 = bv_data[3]
                tick.bid_volume_5 = bv_data[4]

                tick.ask_volume_1 = av_data[0]
                tick.ask_volume_2 = av_data[1]
                tick.ask_volume_3 = av_data[2]
                tick.ask_volume_4 = av_data[3]
                tick.ask_volume_5 = av_data[4]

                tick.last_price = round_to(d["lastPrice"], contract.pricetick)
                tick.open_price = round_to(d["open"], contract.pricetick)
                tick.high_price = round_to(d["high"], contract.pricetick)
                tick.low_price = round_to(d["low"], contract.pricetick)
                tick.pre_close = round_to(d["lastClose"], contract.pricetick)

                self.gateway.on_tick(tick)

    def connect(
        self,
        token: str,
        stock_active: bool,
        futures_active: bool,
        option_active: bool
    ) -> None:
        """连接"""
        self.token = token
        self.stock_active = stock_active
        self.futures_active = futures_active
        self.option_active = option_active

        if self.inited:
            self.gateway.write_log("行情接口已经初始化，请勿重复操作")
            return

        try:
            self.init_xtdc()

            # 尝试查询合约信息，确认连接成功
            xtdata.get_instrument_detail("000001.SZ")
        except Exception as ex:
            self.gateway.write_log(f"迅投研数据服务初始化失败，发生异常：{ex}")
            return False

        self.inited = True

        self.gateway.write_log("行情接口连接成功")

        self.query_contracts()

    def get_lock(self) -> bool:
        """获取文件锁，确保单例运行"""
        self.lock = FileLock(self.lock_filepath)

        try:
            self.lock.acquire(timeout=1)
            return True
        except Timeout:
            return False

    def init_xtdc(self) -> None:
        """初始化xtdc服务进程"""
        if not self.get_lock():
            return

        # 设置token
        xtdc.set_token(self.token)

        # 将VIP服务器设为连接池
        server_list: list = [
            "115.231.218.73:55310",
            "115.231.218.79:55310",
            "218.16.123.11:55310",
            "218.16.123.27:55310"
        ]
        xtdc.set_allow_optmize_address(server_list)

        # 开启使用期货真实夜盘时间
        xtdc.set_future_realtime_mode(True)

        # 执行初始化，但不启动默认58609端口监听
        xtdc.init(False)

        # 设置监听端口58620
        xtdc.listen(port=58620)

    def query_contracts(self) -> None:
        """查询合约信息"""
        if self.stock_active:
            self.query_stock_contracts()

        if self.futures_active:
            self.query_future_contracts()

        if self.option_active:
            self.query_option_contracts()

        self.gateway.write_log("合约信息查询成功")

    def query_stock_contracts(self) -> None:
        """查询股票合约信息"""
        xt_symbols: list[str] = []
        markets: list = [
            "沪深A股",
            "沪深转债",
            "沪深ETF",
            "沪深指数",
            "京市A股"
        ]

        for i in markets:
            names: list = xtdata.get_stock_list_in_sector(i)
            xt_symbols.extend(names)

        for xt_symbol in xt_symbols:
            # 筛选需要的合约
            product = None
            symbol, xt_exchange = xt_symbol.split(".")

            if xt_exchange == "SZ":
                if xt_symbol.startswith("00"):
                    product = Product.EQUITY
                elif xt_symbol.startswith("159"):
                    product = Product.FUND
                else:
                    product = Product.INDEX
            elif xt_exchange == "SH":
                if xt_symbol.startswith(("60", "68")):
                    product = Product.EQUITY
                elif xt_symbol.startswith("51"):
                    product = Product.FUND
                else:
                    product = Product.INDEX
            elif xt_exchange == "BJ":
                product = Product.EQUITY

            if not product:
                continue

            # 生成并推送合约信息
            data: dict = xtdata.get_instrument_detail(xt_symbol)

            contract: ContractData = ContractData(
                symbol=symbol,
                exchange=EXCHANGE_XT2VT[xt_exchange],
                name=data["InstrumentName"],
                product=product,
                size=data["VolumeMultiple"],
                pricetick=data["PriceTick"],
                history_data=False,
                gateway_name=self.gateway_name
            )

            symbol_contract_map[contract.vt_symbol] = contract
            self.gateway.on_contract(contract)

    def query_future_contracts(self) -> None:
        """查询期货合约信息"""
        xt_symbols: list[str] = []
        markets: list = [
            "中金所期货",
            "上期所期货",
            "能源中心期货",
            "大商所期货",
            "郑商所期货",
            "广期所期货"
        ]

        for i in markets:
            names: list = xtdata.get_stock_list_in_sector(i)
            xt_symbols.extend(names)

        for xt_symbol in xt_symbols:
            # 筛选需要的合约
            product = None
            symbol, xt_exchange = xt_symbol.split(".")

            if xt_exchange == "ZF" and len(symbol) > 6 and "&" not in symbol:
                product = Product.OPTION
            elif xt_exchange in ("IF", "GF") and "-" in symbol:
                product = Product.OPTION
            elif xt_exchange in ("DF", "INE", "SF") and ("C" in symbol or "P" in symbol) and "SP" not in symbol:
                product = Product.OPTION
            else:
                product = Product.FUTURES

            # 生成并推送合约信息
            if product == Product.OPTION:
                data: dict = xtdata.get_instrument_detail(xt_symbol, True)
            else:
                data: dict = xtdata.get_instrument_detail(xt_symbol)

            if not data["ExpireDate"]:
                continue

            contract: ContractData = ContractData(
                symbol=symbol,
                exchange=EXCHANGE_XT2VT[xt_exchange],
                name=data["InstrumentName"],
                product=product,
                size=data["VolumeMultiple"],
                pricetick=data["PriceTick"],
                history_data=False,
                gateway_name=self.gateway_name
            )

            symbol_contract_map[contract.vt_symbol] = contract
            self.gateway.on_contract(contract)

    def query_option_contracts(self) -> None:
        """查询期权合约信息"""
        xt_symbols: list[str] = []

        markets: list = [
            "上证期权",
            "深证期权",
            "中金所期权",
            "上期所期权",
            "能源中心期权",
            "大商所期权",
            "郑商所期权",
            "广期所期权"
        ]

        for i in markets:
            names: list = xtdata.get_stock_list_in_sector(i)
            xt_symbols.extend(names)

        for xt_symbol in xt_symbols:
            ""
            _, xt_exchange = xt_symbol.split(".")

            if xt_exchange in {"SHO", "SZO"}:
                contract = process_etf_option(xtdata.get_instrument_detail, xt_symbol)
            else:
                contract = process_futures_option(xtdata.get_instrument_detail, xt_symbol)

            if contract:
                symbol_contract_map[contract.vt_symbol] = contract
                self.gateway.on_contract(contract)

    def subscribe(self, req: SubscribeRequest) -> None:
        """订阅行情"""
        if req.vt_symbol not in symbol_contract_map:
            return

        xt_exchange: str = EXCHANGE_VT2XT[req.exchange]
        if xt_exchange in {"SH", "SZ"} and len(req.symbol) > 6:
            xt_exchange += "O"

        xt_symbol: str = req.symbol + "." + xt_exchange

        if xt_symbol not in self.subscribed:
            xtdata.subscribe_quote(stock_code=xt_symbol, period="tick", callback=self.onMarketData)
            self.subscribed.add(xt_symbol)

    def close(self) -> None:
        """关闭连接"""
        pass


def generate_datetime(timestamp: int, millisecond: bool = True) -> datetime:
    """生成本地时间"""
    if millisecond:
        dt: datetime = datetime.fromtimestamp(timestamp / 1000)
    else:
        dt: datetime = datetime.fromtimestamp(timestamp)
    dt: datetime = dt.replace(tzinfo=CHINA_TZ)
    return dt


def process_etf_option(get_instrument_detail: Callable, xt_symbol: str) -> Optional[ContractData]:
    """处理ETF期权"""
    # 拆分XT代码
    symbol, xt_exchange = xt_symbol.split(".")

    # 筛选期权合约合约（ETF期权代码为8位）
    if len(symbol) != 8:
        return None

    # 查询转换数据
    data: dict = get_instrument_detail(xt_symbol, True)

    name: str = data["InstrumentName"]
    if "购" in name:
        option_type = OptionType.CALL
    elif "沽" in name:
        option_type = OptionType.PUT
    else:
        return None

    if "A" in name:
        option_index = str(data["OptExercisePrice"]) + "-A"
    else:
        option_index = str(data["OptExercisePrice"]) + "-M"

    contract: ContractData = ContractData(
        symbol=data["InstrumentID"],
        exchange=EXCHANGE_XT2VT[xt_exchange],
        name=data["InstrumentName"],
        product=Product.OPTION,
        size=data["VolumeMultiple"],
        pricetick=data["PriceTick"],
        min_volume=data["MinLimitOrderVolume"],
        option_strike=data["OptExercisePrice"],
        option_listed=datetime.strptime(data["OpenDate"], "%Y%m%d"),
        option_expiry=datetime.strptime(data["ExpireDate"], "%Y%m%d"),
        option_portfolio=data["OptUndlCode"] + "_O",
        option_index=option_index,
        option_type=option_type,
        option_underlying=data["OptUndlCode"] + "-" + str(data["ExpireDate"])[:6],
        gateway_name="XT"
    )

    return contract


def process_futures_option(get_instrument_detail: Callable, xt_symbol: str) -> Optional[ContractData]:
    """处理期货期权"""
    # 筛选期权合约
    data: dict = get_instrument_detail(xt_symbol, True)

    option_strike: float = data["OptExercisePrice"]
    if not option_strike:
        return None

    # 拆分XT代码
    symbol, xt_exchange = xt_symbol.split(".")

    # 移除产品前缀
    for ix, w in enumerate(symbol):
        if w.isdigit():
            break

    suffix: str = symbol[ix:]

    # 过滤非期权合约
    if "(" in symbol or " " in symbol:
        return None

    # 判断期权类型
    if "C" in suffix:
        option_type = OptionType.CALL
    elif "P" in suffix:
        option_type = OptionType.PUT
    else:
        return None

    # 获取期权标的
    if "-" in symbol:
        option_underlying: str = symbol.split("-")[0]
    else:
        option_underlying: str = data["OptUndlCode"]

    # 转换数据
    contract: ContractData = ContractData(
        symbol=data["InstrumentID"],
        exchange=EXCHANGE_XT2VT[xt_exchange],
        name=data["InstrumentName"],
        product=Product.OPTION,
        size=data["VolumeMultiple"],
        pricetick=data["PriceTick"],
        min_volume=data["MinLimitOrderVolume"],
        option_strike=data["OptExercisePrice"],
        option_listed=datetime.strptime(data["OpenDate"], "%Y%m%d"),
        option_expiry=datetime.strptime(data["ExpireDate"], "%Y%m%d"),
        option_index=str(data["OptExercisePrice"]),
        option_type=option_type,
        option_underlying=option_underlying,
        gateway_name="XT"
    )

    if contract.exchange == Exchange.CZCE:
        contract.option_portfolio = data["ProductID"][:-1]
    else:
        contract.option_portfolio = data["ProductID"]

    return contract
