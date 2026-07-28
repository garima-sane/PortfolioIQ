# 📈 PortfolioIQ
### Quantitative Portfolio Analysis & Optimization using Python

> "Learning Quantitative Finance one concept at a time."

PortfolioIQ is my second major Data Science project after TRACKX.

While TRACKX focused on data cleaning and visualization, this project explores the mathematics behind investing, portfolio construction and quantitative finance.

Instead of analysing individual stocks, PortfolioIQ studies how groups of stocks behave together and how statistical techniques can be used to build better investment portfolios.

The goal wasn't simply to build a portfolio optimizer—it was to understand every concept before implementing it.

This project marks my introduction to Quantitative Finance, Modern Portfolio Theory (MPT) and Portfolio Optimization.

---

# 🎯 Project Objectives

Through this project, I wanted to answer questions like:

- Which companies historically generated the best average returns?
- Which companies are the most volatile?
- How can investment risk actually be measured?
- Why isn't the highest return always the best investment?
- How are portfolios evaluated mathematically?
- How does Monte Carlo Simulation help discover better portfolios?
- How can thousands of portfolios be compared efficiently?

Rather than copying formulas, I focused on understanding the intuition behind every calculation before writing the code.

---

# 📊 Dataset

Historical S&P 500 Stock Dataset

- 503 Companies
- Daily Historical Stock Prices
- Time Period: 2010 – Present
- OHLCV Data
  - Open
  - High
  - Low
  - Close
  - Volume

### Original Dataset

Rows : **4166**

Columns : **2516**

---

# 🛠 Project Workflow

Raw Dataset

↓

Data Cleaning

↓

Column Renaming

↓

Missing Value Analysis

↓

Exploratory Data Analysis

↓

Daily Return Calculation

↓

Expected Returns

↓

Volatility Analysis

↓

Sharpe Ratio

↓

Correlation Analysis

↓

Portfolio Mathematics

↓

Monte Carlo Portfolio Simulation

↓

Efficient Frontier

↓

Optimal Portfolio Selection

↓

Dashboard (Future Work)

---

# 📚 What I Learned

Instead of directly jumping into portfolio optimization, I broke the project into smaller learning stages.

Every section taught me one new concept in quantitative finance before moving to the next.

---

# Stage 1 — Understanding the Dataset

The original dataset contained over **2500 columns** representing stock prices of **503 companies**.

Each company contained five features:

- Open
- High
- Low
- Close
- Volume

One of the first tasks was understanding how these columns were organised before beginning any analysis.

---

# Stage 2 — Column Renaming

The original dataset contained generic column names.

I extracted company tickers and automatically renamed every feature into meaningful names such as

```
AAPL_Close
AAPL_Open
AAPL_High
AAPL_Low
AAPL_Volume
```

This significantly improved readability and made later analysis much easier.

---

# Stage 3 — Data Cleaning

The first two rows contained metadata instead of stock observations.

These rows were removed to create a clean numerical dataset suitable for analysis.

---

# Stage 4 — Missing Value Analysis

One of the most interesting findings of this project.

Initially the dataset contained over

**645,000 missing values**

Instead of assuming the data was corrupted, I investigated why these values existed.

I discovered that many companies joined the S&P 500 years after 2010.

Examples include

- HONA
- FDXF
- SNDK
- Q

Since these companies weren't part of the index during earlier years, their historical prices simply don't exist.

This taught me an important lesson:

> Missing values don't always indicate poor data quality—they often represent real-world business events.

---

# Why Closing Prices?

For this project I decided to use **Closing Prices**.

Closing prices represent the final market consensus after an entire trading session.

Most quantitative finance calculations use closing prices because they provide consistency when calculating

- Daily Returns
- Expected Returns
- Portfolio Returns
- Volatility
- Risk Metrics

---

# Stage 5 — Daily Returns

Raw prices alone don't provide meaningful comparisons.

Instead, prices were converted into percentage changes using

```python
pct_change()
```

This transformed every stock into comparable daily returns regardless of its actual stock price.

---

# Stage 6 — Expected Returns

The average daily return was calculated for every company.

These values estimate each company's historical expected performance.

This became the first building block for portfolio optimization.

Concept learned:

> Portfolio returns are simply weighted averages of expected returns.

---

# Stage 7 — Volatility

Return alone doesn't describe an investment.

Risk matters.

Volatility was calculated using standard deviation to measure how much each stock fluctuates over time.

Higher volatility generally indicates greater uncertainty and investment risk.

---

# Stage 8 — Sharpe Ratio

A stock with higher returns isn't necessarily better.

The Sharpe Ratio compares

**Return**

relative to

**Risk**

(Current implementation assumes Risk-Free Rate = 0.)

This introduced me to one of the most widely used portfolio performance metrics.

---

# Stage 9 — Correlation Analysis

One of my favourite parts of the project.

Instead of analysing companies individually, I explored how different companies move relative to one another.

Strong correlations discovered included

- GOOG ↔ GOOGL
- FOX ↔ FOXA
- NWS ↔ NWSA

These results also helped validate that the calculations were correct.

The project also generated a complete correlation heatmap for all companies.

---

# Stage 10 — Portfolio Mathematics

This project shifted from analysing stocks individually to analysing entire portfolios.

I learned that every portfolio can simply be represented by investment weights.

Example

```
Apple        18%

Microsoft    12%

Google       10%

...

```

The weights always sum to

```
100%
```

ensuring that all available capital is invested.

---

# Portfolio Expected Return

Portfolio return is calculated as a weighted average of expected returns.

Mathematically

```
Portfolio Return

=

Weights × Expected Returns
```

Implemented using

```python
np.dot()
```

This was my first practical application of vector mathematics in finance.

---

# Portfolio Risk

Portfolio risk depends on

- Individual stock volatility
- How stocks move relative to one another

Instead of simply adding risks, I used the covariance matrix.

Portfolio Risk is calculated using

```
√(WᵀΣW)
```

where

- W = Portfolio Weights
- Σ = Covariance Matrix

This introduced me to one of the core equations of Modern Portfolio Theory.

---

# Stage 11 — Monte Carlo Portfolio Simulation

After understanding portfolio mathematics, I implemented Monte Carlo Simulation.

Instead of evaluating a single portfolio, the program randomly generated **10,000 different portfolios**.

Each portfolio contained randomly assigned investment weights.

For every portfolio, the program calculated

- Expected Return
- Portfolio Risk
- Sharpe Ratio

The simulation then compared every generated portfolio to discover better investment allocations.

This was the first time I combined probability, statistics and programming into one complete financial model.

---

# Stage 12 — Efficient Frontier

After evaluating thousands of portfolios, I visualized them using the Efficient Frontier.

The graph compares

- Expected Return
- Portfolio Risk

Each portfolio is colour-coded using its Sharpe Ratio.

This visualization clearly demonstrates the trade-off between

Higher Return

vs

Higher Risk

One portfolio is highlighted as the optimal portfolio with the highest Sharpe Ratio.

---

# Stage 13 — Optimal Portfolio Selection

Using the results of the Monte Carlo Simulation, the project identifies

✅ Portfolio with Maximum Sharpe Ratio

along with

- Portfolio Return
- Portfolio Risk
- Portfolio Weights

The best portfolio allocation is displayed in descending order for easy interpretation.

---

# 📈 Visualizations Created

- Average Daily Returns
- Top 10 Average Performing Companies
- Volatility Analysis
- Top 10 Sharpe Ratio
- Risk vs Return Scatter Plot
- Correlation Heatmap
- Efficient Frontier

---

# 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Git
- GitHub
- VS Code

---

# ✅ Current Features

✔ Data Cleaning

✔ Feature Engineering

✔ Missing Value Analysis

✔ Daily Returns

✔ Expected Returns

✔ Volatility Analysis

✔ Sharpe Ratio

✔ Correlation Analysis

✔ Portfolio Mathematics

✔ Portfolio Return

✔ Portfolio Risk

✔ Monte Carlo Portfolio Simulation

✔ Efficient Frontier

✔ Optimal Portfolio Selection

---

# 🚀 Future Improvements

Although the internship version of PortfolioIQ is complete, I plan to continue improving it.

Upcoming features include

- Interactive Streamlit Dashboard
- Portfolio Allocation Pie Chart
- Company Search
- Portfolio Comparison Tool
- Real-Time Stock Prices using APIs
- Portfolio Rebalancing
- Sector-wise Portfolio Allocation
- User Defined Portfolio Simulation
- Risk-Free Rate Integration
- Downloadable Portfolio Reports

---

# 💡 Reflection

PortfolioIQ taught me that quantitative finance isn't about predicting the market.

It's about understanding uncertainty, measuring risk and making better decisions using mathematics, probability and data.

More importantly, I realised that formulas become much easier once the intuition behind them is understood first.

This project has given me a strong foundation in portfolio optimization, quantitative finance and financial data science, and I plan to continue expanding it into a complete portfolio analysis platform.