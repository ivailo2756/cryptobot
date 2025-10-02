# main.py
# Minimal crypto-bot skeleton using ccxt
# Works without API keys for public data

import os
import time
from typing import Optional

try:
    import ccxt
except ImportError:
    raise SystemExit("Missing dependency: install ccxt (pip install ccxt)")

try:
    from rich.console import Console
    from rich.table import Table
    from rich.prompt import Prompt
    from rich.panel import Panel
    from rich import box
except ImportError:
    raise SystemExit("Missing dependency: install rich (pip install rich)")

console = Console()

def show_markets(exchange: str = "binance"):
    ex = getattr(ccxt, exchange)()
    markets = ex.load_markets()
    table = Table(title=f"Markets on {exchange}", box=box.SIMPLE)
    table.add_column("Symbol")
    for m in list(markets.keys())[:10]:
        table.add_row(m)
    console.print(table)

if __name__ == "__main__":
    console.print(Panel("CryptoBot Started", expand=False))
    show_markets()
