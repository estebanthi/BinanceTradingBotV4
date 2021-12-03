# Put here your imports
import backtrader as bt
import warnings
from models.Engine.EngineConfiguration import EngineConfiguration as EngineConfiguration
from models.Strategies.SimpleStrats.TripleEMA import TripleEMA as TripleEMA
from models.Engine.Engine import Engine as Engine
from models.Analyzers.ResultAnalyzer import ResultAnalyzer as ResultAnalyzer
from models.Analyzers.TradeAnalyzer import TradeAnalyzer as TradeAnalyzer
from models.Analyzers.PercentGetter import PercentGetter as PercentGetter
from models.Strategies.BracketStrats.StochMacdRsi import StochMacdRsi as StochMacdRsi
import datetime as dt
from models.Observers.Value import Value as ValueObserver
from models.Timers.StopSession import StopSession as StopSession
from models.TelegramBot.TelegramBot import TelegramBot as TelegramBot
from models.Sizers.PercentSizer import PercentSizer as PercentSizer
from models.Strategies.BracketStrats.BollingerBandsDivergences import \
    BollingerBandsDivergence as BollingerBandsDivergence
from models.Strategies.BracketStrats.PSAR_EMA import PSAR_EMA as PSAR_EMA
from models.Sizers.FixedSizer import FixedSizer as FixedSizer
from models.Analyzers.AnnualReturn import AnnualReturn
from models.Analyzers.PyFolio import PyFolio
from models.Analyzers.StratQuality import StratQuality
from models.Analyzers.TradeList import TradeList
import ccxt

# To disable useless warnings
warnings.filterwarnings("ignore")

# Put here your trading components
strategies = [StochMacdRsi()]
analyzers = [TradeAnalyzer(), TradeList()]
observers = [ValueObserver()]
sizer = PercentSizer(99)

# Instantiate the engine
engine = Engine()

# Configure the engine
config = EngineConfiguration(
    mode="BACKTEST",
    symbol="BNB/BTC",
    start_date="2021/10/01 0:0:0",
    end_date="2021/11/01 0:0:0",
    timeframe=bt.TimeFrame.Minutes,
    compression=5,
    strategies=strategies,
    analyzers=analyzers,
    stdstats=True,
    observers=observers,
    sizer=sizer,
    commission=0.075,
    exchange=ccxt.binance(),
)
engine.set_configuration(config)

# Run the engine
result = engine.run()

# Charting
engine.plot()

result_analyzer = ResultAnalyzer(result)
result_analyzer.pretty_pnls()
result_analyzer.print_trade_list()
