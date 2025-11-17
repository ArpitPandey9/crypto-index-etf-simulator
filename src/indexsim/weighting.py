import pandas as pd

def cap_weight(mcap: pd.Series) -> pd.Series:
    w = mcap / mcap.sum()
    return w

def capped_10(w: pd.Series, cap=0.10) -> pd.Series:
    w = w.clip(upper=cap)
    spill = 1 - w.sum()
    if spill > 0:
        rest = (w < cap)
        w.loc[rest] += spill * (w[rest] / w[rest].sum())
    return w
