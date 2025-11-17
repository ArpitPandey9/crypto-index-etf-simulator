# S&P 500 ETF Risk Analyzer 🔍📉

**Solves S&P Global Pain Point:** Automated institutional-grade ETF risk reporting

## Features
- 📊 Dynamic risk metric calculation (volatility, max drawdown)
- 📅 Date range flexibility
- 🔥 Wall Street-quality visualization
- 📈 Outputs PDF-ready report

## S&P Global Applications
- Daily ETF surveillance reports
- Portfolio stress-testing
- Client risk briefing automation


## About

**What this is:** A rules-based **index/ETF simulator** for digital assets/crypto.
It converts research signals and eligibility rules into **index-grade** methods:
universe → liquidity/eligibility screens → weighting/caps → monthly rebalance →
**turnover & cost** reporting → **factsheet** and **methodology** artifacts.

**S&P Alignment:** **DJI (Index R&D)** — mirrors index methodology development:
eligibility/liquidity thresholds, weighting schemes (cap-weight, capped, HRP),
rebalance cadence, turnover & cost estimation, factsheet PDFs, and governance notes.

**Key features**
- Universe + eligibility/liquidity screens (min price, volume, days traded)
- Weighting: cap-weight, capped (e.g., 10%), HRP; optional **volatility targeting**
- Monthly rebalance with **buffers**; turnover & after-cost performance
- **Tracking error** vs baseline; **IC/IR** for any predictive inputs
- **Factsheet generator** (charts + table), **methodology.md**, **governance checklist**
- Reproducible env, seeds, CI tests; no secrets committed

**Metrics we track**
- Strategy: Sharpe/Sortino/Calmar (after costs), Max DD, Turnover
- Index: Eligibility pass rate, Rebalance cost estimate, **Tracking error**
- Forecast inputs (optional): IC/IR, OOS RMSE/MAE (walk-forward)

**How to run**
```bash
python -m venv .venv && .\.venv\Scripts\activate
pip install -r requirements.txt
python run.py  # generates weights & a factsheet sample
pytest -q      # CI-quality smoke tests


## Installation
```bash
pip install -r requirements.txt
