from dash import Dash
from dash_bootstrap_templates import load_figure_template
from jupyter_dash import JupyterDash
from IPython import get_ipython
import dash_bootstrap_components as dbc
from quantfreedom.helpers.utils import pretty_qf, pretty_qf_string
from quantfreedom.helpers.helper_funcs import dl_ex_candles, all_backtest_stats, symbol_bt_df
from quantfreedom.helpers.custom_logger import set_loggers
from quantfreedom.core.enums import FootprintCandlesTuple, DynamicOrderSettings, CandleBodyType
from quantfreedom.backtesters import or_backtest
from quantfreedom.core.strategy import Strategy


__all__ = [
    "all_backtest_stats",
    "CandleBodyType",
    "dl_ex_candles",
    "DynamicOrderSettings",
    "FootprintCandlesTuple",
    "or_backtest",
    "pretty_qf",
    "pretty_qf_string",
    "set_loggers",
    "Strategy",
    "symbol_bt_df",
]

load_figure_template("darkly")
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
try:
    shell = str(get_ipython())
    if "ZMQInteractiveShell" in shell:
        app = JupyterDash(__name__, external_stylesheets=[dbc.themes.DARKLY, dbc_css])
    elif shell == "TerminalInteractiveShell":
        app = JupyterDash(__name__, external_stylesheets=[dbc.themes.DARKLY, dbc_css])
    else:
        app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, dbc_css])
except NameError:
    app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, dbc_css])

bg_color = "#0b0b18"
