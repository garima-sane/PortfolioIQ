# 📈 PortfolioIQ
### Financial Analytics & Portfolio Optimization using Python

PortfolioIQ is an end-to-end financial analytics and portfolio optimization project that transforms raw historical S&P 500 market data into meaningful investment insights.

Rather than simply visualizing stock prices, PortfolioIQ aims to answer a portfolio manager's most important question:

> **"How should capital be allocated to maximize returns while managing risk?"**

The project follows the complete workflow used in quantitative finance—from raw market data preprocessing to financial analytics and portfolio optimization using Modern Portfolio Theory and Monte Carlo Simulation.

---

# 🎯 Project Objective

Institutional investors and portfolio managers analyze thousands of stocks every day.

However, making investment decisions solely based on historical prices is ineffective.

PortfolioIQ helps investors by:

- Understanding historical market behaviour
- Measuring risk and returns
- Identifying relationships between companies
- Comparing investment opportunities
- Simulating thousands of possible portfolios
- Finding portfolios with better risk-adjusted performance

Ultimately, the project provides a data-driven foundation for building diversified investment portfolios.

---

# 📂 Dataset

**Source**

Historical S&P 500 Market Dataset

The dataset contains historical daily trading information of more than **500 companies** listed in the S&P 500 index.

Each company contains five financial attributes:

- Open Price
- High Price
- Low Price
- Close Price
- Trading Volume

Original Dataset Size

- **4166 Trading Days**
- **503 Companies**
- **2516 Columns**

---

# 🛠 Project Workflow

The project has been divided into multiple stages, closely following a real-world financial analytics pipeline.

```
Raw Historical Market Data
            │
            ▼
Data Cleaning & Preprocessing
            │
            ▼
Financial Feature Engineering
            │
            ▼
Exploratory Financial Analysis
            │
            ▼
Risk & Return Analytics
            │
            ▼
Portfolio Optimization
            │
            ▼
Interactive Dashboard (Upcoming)
```

---

# 🧹 Phase 1 — Data Preprocessing

Raw financial datasets are rarely analysis-ready.

The downloaded dataset contained:

- Metadata rows
- Generic column names
- Mixed financial attributes
- Missing values caused by companies entering the S&P 500 at different periods

To prepare the data for analysis:

### ✔ Metadata Removal

Removed non-data rows containing ticker symbols and metadata.

---

### ✔ Dynamic Column Renaming

The original dataset stored company data in the following format:

```
Close
Close.1
Close.2
...
```

These generic names were transformed into meaningful financial features such as:

```
AAPL_Close
MSFT_Close
NVDA_Close
GOOG_Close
```

This makes every company's financial data directly identifiable and easier to analyze.

---

### ✔ Financial Attribute Separation

Each company now contains:

- Open
- High
- Low
- Close
- Volume

allowing independent analysis of each market attribute.

---

### ✔ Missing Value Analysis

A large number of missing values were discovered.

Instead of removing them blindly, the data was investigated.

The analysis revealed that most missing values belonged to companies that joined the S&P 500 years after 2010.

Therefore, these values represented **non-existent historical records** rather than corrupted data.

This observation preserved important financial information while avoiding unnecessary data loss.

---

# 📊 Phase 2 — Financial Analytics

After cleaning the dataset, PortfolioIQ begins extracting meaningful financial insights.

---

## Daily Returns

Instead of analyzing raw prices, daily percentage returns were calculated.

Daily Returns describe how much a stock gained or lost compared to the previous trading day.

This is a more reliable measure because stocks have different price ranges.

Example:

A ₹50 increase means something very different for:

- ₹200 stock
- ₹2000 stock

Percentage returns standardize these movements.

---

## Average Daily Return

The average daily return was computed for every company.

Purpose:

- Identify historically stronger performers
- Compare long-term average growth
- Rank companies

---

## Volatility Analysis

Higher returns often come with higher risk.

PortfolioIQ measures risk using the standard deviation of daily returns.

Higher volatility indicates larger day-to-day price fluctuations.

Lower volatility generally represents more stable investments.

---

## Correlation Analysis

Diversification is one of the core principles of portfolio management.

A correlation matrix was generated to measure how companies move relative to one another.

The analysis successfully identified expected relationships such as:

- GOOG ↔ GOOGL
- FOX ↔ FOXA
- NWS ↔ NWSA

demonstrating that companies belonging to the same organization or industry exhibit highly similar market behaviour.

The correlation heatmap provides an intuitive visualization of market relationships.

---

## Risk vs Return Analysis

Every company was plotted using:

- Risk (Volatility)
- Average Daily Return

This visualization highlights the classic investment trade-off:

Higher returns generally require accepting higher levels of risk.

---

## Sharpe Ratio

PortfolioIQ evaluates investments using the Sharpe Ratio.

Rather than rewarding high returns alone, the Sharpe Ratio measures:

> **Return earned per unit of risk.**

This allows investors to compare companies on a risk-adjusted basis instead of simply selecting those with the highest returns.

---

## Top Performing Stocks

Stocks were ranked based on:

- Average Returns
- Volatility
- Sharpe Ratio

These rankings form the investment universe for the portfolio optimization stage.

---

# 🚀 Phase 3 — Portfolio Optimization *(In Progress)*

Financial analysis alone cannot recommend how investments should be allocated.

PortfolioIQ extends this analysis using portfolio optimization techniques.

Upcoming modules include:

- Monte Carlo Portfolio Simulation
- Efficient Frontier
- Maximum Sharpe Portfolio
- Minimum Variance Portfolio
- Optimal Portfolio Allocation

These methods aim to identify portfolios that provide the best balance between expected return and investment risk.

---

# 📈 Future Dashboard

An interactive dashboard will allow users to:

- Choose investment amount
- Select risk tolerance
- Generate optimized portfolios
- Visualize portfolio allocation
- Compare expected return and risk
- Explore efficient frontier interactively

---

# 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Git
- GitHub

---

# 📁 Project Structure

```
PortfolioIQ/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│
├── portfolio_preprocess.py
├── eda.py
├── portfolio_optimization.py
├── dashboard.py (Upcoming)
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📌 Current Progress

## Completed

- Data Cleaning
- Metadata Removal
- Dynamic Column Renaming
- Financial Feature Engineering
- Daily Returns
- Average Returns
- Volatility Analysis
- Correlation Analysis
- Correlation Heatmap
- Risk vs Return Analysis
- Sharpe Ratio
- Top Performing Stocks

## In Progress

- Monte Carlo Simulation
- Efficient Frontier
- Portfolio Optimization

## Planned

- Streamlit Dashboard
- Live Market Data Integration
- Portfolio Rebalancing
- Sector-wise Portfolio Analytics

---

# 💡 Key Learning Outcomes

This project strengthened practical understanding of:

- Financial Data Engineering
- Exploratory Financial Analysis
- Risk Measurement
- Portfolio Diversification
- Modern Portfolio Theory
- Quantitative Finance Concepts
- Data Visualization
- Python for Financial Analytics