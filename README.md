# Crypto Index / ETF Simulator — Early Prototype

Small public prototype containing early index-weighting helpers, an eligibility-rule scaffold, and historical ETF-analysis artifacts.

## What is implemented

The tracked Python source currently provides:

- `UniverseRule`, a dataclass carrying minimum price, volume, and trading-history thresholds
- `cap_weight()`, a basic market-cap weighting helper
- `capped_10()`, an experimental capped-weight helper
- an `eligible()` function scaffold

## What is not yet implemented

The current public snapshot does **not** contain a complete end-to-end crypto index engine. In particular:

- `eligible()` is still a stub and currently returns an empty list
- there is no tracked `run.py`
- there is no behavioral test suite
- HRP weighting, volatility targeting, transaction-cost modeling, tracking-error analysis, factsheet generation, and governance workflows are not implemented in the tracked source shown here
- the repository should not be described as production or institutional-grade

The SPY notebook, chart, and CSV are retained as historical prototype artifacts from earlier ETF-risk exploration.

## Validation

Automated validation checks:

- Python source syntax
- notebook JSON validity
- public documentation for unsupported institutional or employer-specific claims

It does not claim behavioral correctness for the incomplete simulator.

## Repository contents

```text
src/indexsim/screens.py
src/indexsim/weighting.py
spy_analyzer.ipynb
spy_analysis.png
spy_risk_report.csv
```

## Limitations

This repository is an early research prototype, not an investment recommendation, official index methodology, production financial system, or representation of any employer or client.

## License

See `LICENSE`.
