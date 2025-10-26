# 📈 Market Forecast Capstone

**Graduate Data Science Capstone Project (2025)**  
Author: *[Your Name]*  
Environment: Google Colab + GitHub  
Primary Ticker: **SPY (S&P 500 Index)**  
Project Period: 2019–Present (expandable up to 25 years)  

---

## 🚀 Overview
This project aims to build a **multi-model predictive system** for the U.S. equity market using the **S&P 500 Index (SPY)** as the benchmark.  
The pipeline integrates **macroeconomic data**, **technical indicators**, and **news sentiment analysis** to forecast short-term and medium-term market movements.

The system combines **classical ML models**, **sequence models (LSTM)**, and **time-series forecasting (Prophet)**, culminating in a **heterogeneous ensemble** of the top-performing models.

---

## 🎯 Objectives

1. Build an integrated financial and sentiment dataset (Alpha Vantage, FRED, Guardian APIs).  
2. Conduct robust **EDA and PCA** to analyze feature relationships and dimensionality.  
3. Train **9 independent predictive models** for regression and classification tasks.  
4. Construct an **ensemble model** combining top models (2–3).  
5. Evaluate **next-day** and **30/60-day forward returns**.  
6. Analyze feature importances, trends, and residual behaviors.  

---

## 🧠 Data Sources

| Source | Description | Notes |
|---------|--------------|-------|
| **Alpha Vantage** | Historical price data, technical indicators, and financial news | Primary API |
| **FRED** | Macroeconomic data (CPI, Unemployment, Fed Funds, Term Spread) | Updated monthly |
| **Guardian API** | Political & market-related news headlines and sentiment | Aligned by timestamp |
| *(Optional)* Alpha Vantage News | Supplementary sentiment data | For experimentation |

---

## 🧩 Feature Engineering

Computed locally (no indicator API calls):
- SMA (20, 50, 200), EMA  
- Bollinger Bands  
- RSI (14), Stoch %K/%D  
- MACD (12-26-9)  
- %Δ Close, %Δ Moving Average  
- Rolling autocorrelation (60-day lag 1)  
- Rolling correlations (%Δ Close vs %Δ MA, %Δ Volume)  
- Second derivatives (price & MA returns)  
- Volatility and z-score features  

Additional Flags:
- `pres_dem`, `is_election_day`, `is_inauguration_day`, `is_shutdown_window`

---

## 🧰 Modeling Pipeline

### Phase 1 — Data & EDA
- Data ingestion from Alpha Vantage, FRED, and Guardian APIs  
- Merge and align datasets using trading calendar (NYSE)  
- Exploratory Data Analysis & PCA  
- Train/test split using rolling windows  

### Phase 2 — Model Training
**Planned Models (v1):**
- Linear Regression / Ridge / Lasso  
- Random Forest / XGBoost / CatBoost  
- SVR / MLP  
- LSTM  
- Prophet (trend residual features + forecasting)  

### Phase 3 — Ensemble & Evaluation
- Stacked ensemble (meta-learner) of top 2–3 models  
- Compare next-day vs 30/60-day horizon performance  
- Evaluation metrics: MSE, RMSE, R² (regression), Accuracy, F1 (classification)  
- Rolling backtests & out-of-sample validation  

---

## 🗂️ Repository Structure

market-forecast-capstone/
│
├── data/ <- processed datasets
├── raw/ <- raw API payloads
├── src/ <- Python modules for ETL, modeling, utils
├── notebooks/
│ ├── 01_ingest_explore.ipynb
│ ├── 02_EDA_feature_targets.ipynb
│ ├── 03_model_baselines.ipynb
│ ├── 04_model_lstm_prophet.ipynb
│ ├── 05_ensemble_backtest.ipynb
│ └── 99_report_figures.ipynb
├── requirements.txt
├── LICENSE
└── README.md

---

## ⚙️ Environment

- **Platform:** Google Colab  
- **Language:** Python 3.10+  
- **Core Libraries:**  
  `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`, `tensorflow`,  
  `statsmodels`, `prophet`, `vaderSentiment`, `fredapi`, `alpha_vantage`, `requests`, `plotly`

---

## 🧩 Notes & Configuration

- Time zone normalized to **America/New_York**  
- Data stored in local Colab or mounted Drive  
- NYSE holiday calendar respected for trading days  
- Raw API responses retained in `/raw/`  
- Rolling windows configurable (default 60 days)  
- Target returns evaluated for next-day and 30/60-day horizons  

---

## 📊 Future Extensions (v2)

- Add survivorship bias correction  
- Include additional sentiment model (FinBERT or BERT)  
- Incorporate ETF and sector-level features  
- Add reinforcement learning agent (optional experimental phase)

---

## 📜 License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact
For questions or collaboration opportunities:  
📩 *[jgiwa@depaul.edu]*  
💼 *[your LinkedIn or GitHub profile]*
