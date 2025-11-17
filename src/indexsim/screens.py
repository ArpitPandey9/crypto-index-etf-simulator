from dataclasses import dataclass

@dataclass
class UniverseRule:
    min_price: float = 1.0
    min_volume: float = 1e6
    min_days: int = 90

def eligible(df_prices, df_meta, rule=UniverseRule()):
    """Return list of eligible tickers given price history + meta (volume, days traded)."""
    # TODO: implement checks per rule; return sorted list
    return []
