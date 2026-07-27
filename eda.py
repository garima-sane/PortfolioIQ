from numpy import average
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

df = pd.read_csv("data/intermediate/renamed_columns.csv")

print("=" * 60)
print("PORTFOLIOIQ - EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# --------------------------------------------------
# BASIC INFORMATION
# --------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum().sum())

print("\nDate Range:")
print(df["Date"].min(), "to", df["Date"].max())

close_columns = [col for col in df.columns if col.endswith("_Close")]

print("\nNumber of Companies:", len(close_columns))

# Understanding Missing Values
print("\n" + "=" * 60)
print("MISSING VALUES PER COLUMN")
print("=" * 60)

missing = df.isnull().sum()
missing = missing[missing > 0]

print(missing.sort_values(ascending=False).head(20))
print("\nColumns with Missing Values:")

print(len(missing))

#--------------------------------------------------
# Daily returns
#--------------------------------------------------
close_columns = [col for col in df.columns if col.endswith("_Close")]

returns = df[close_columns].pct_change()

returns.columns = [
    col.replace("_Close", "_Return")
    for col in returns.columns
]

returns_df = pd.concat([df[["Date"]], returns], axis=1)

print("\nDaily Returns Dataset Created!")
returns_df.to_csv(
    "data/processed/daily_returns.csv",
    index=False
)

print("\nDaily Returns Dataset Saved Successfully!")


#Average Daily Returns
average_daily_returns = returns_df.mean(numeric_only=True)
average_daily_returns = average_daily_returns.sort_values(ascending=False)
average_daily_returns.to_csv(
    "outputs/average_daily_returns.csv",
    header=["Average_Daily_Return"]
)
print("\nTop 10 Stocks by Average Daily Return")
print(average_daily_returns.head(10))    

# --------------------------------------------------
# VOLATILITY (RISK)
# --------------------------------------------------

volatility = returns_df.drop(columns="Date").std()

volatility = volatility.sort_values(ascending=False)

print("\nTop 10 Most Volatile Stocks")
print(volatility.head(10))

print("\nTop 10 Least Volatile Stocks")
print(volatility.tail(10))

volatility.to_csv(
    "data/processed/volatility.csv",
    header=["Volatility"]
)

print("\nVolatility Saved Successfully!")

# --------------------------------------------------
# CORRELATION MATRIX
# --------------------------------------------------

correlation = returns_df.drop(columns="Date").corr()

print("\nCorrelation Matrix Created!")
print(correlation.iloc[:5, :5])

correlation.to_csv(
    "data/processed/correlation_matrix.csv"
)

print("Correlation Matrix Saved!")

plt.figure(figsize=(16,12))

sns.heatmap(
    correlation,
    cmap="coolwarm",
    center=0
)

plt.title("Correlation Between Stock Returns")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png")


plt.figure(figsize=(16,12))

#Correlation for top 20 stocks
corr = returns_df.drop(columns="Date").corr()

# Keep only the upper triangle (no duplicates)
upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))

top_corr = (
    upper.stack()
    .sort_values(ascending=False)
    .head(20)
)

print("\nTop 20 Unique Correlations")
print(top_corr)

#TOP 10 Stocks by Average Daily Return

top10 = average_daily_returns.head(10)

plt.figure(figsize=(10,6))

top10.sort_values().plot(kind="barh")

plt.title("Top 10 Stocks by Average Daily Return")
plt.xlabel("Average Daily Return")
plt.tight_layout()
plt.savefig("outputs/top10_average_returns.png")

#--------------------------------------------------
# Risk vs Return Graph 
#--------------------------------------------------

risk_return = pd.DataFrame({
    "Return": average_daily_returns,
    "Risk": volatility
})

plt.figure(figsize=(12,8))
plt.scatter(
    risk_return["Risk"],
    risk_return["Return"],
    alpha=0.7
)

plt.xlabel("Risk (Volatility)")
plt.ylabel("Average Daily Return")
plt.title("Risk vs Return")

plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/risk_vs_return.png")

#Sharpe Ratio
sharpe = average_daily_returns / volatility
sharpe = sharpe.sort_values(ascending=False)

print(sharpe.head(20))
sharpe.to_csv(
    "outputs/sharpe_ratio.csv",
    header=["Sharpe"]
)

#Top 10 Stocks by Sharpe Ratio
top10 = sharpe.head(10)

plt.figure(figsize=(12,6))
top10.plot(kind="bar")
plt.ylabel("Sharpe Ratio")
plt.title("Top 10 Stocks by Sharpe Ratio")
plt.tight_layout()

plt.savefig("outputs/top10_sharpe.png")


#--------------------------------------------------
# Random Portfolio Simulation
#--------------------------------------------------
top_companies = sharpe.head(20).index
print(top_companies)

portfolio_returns = returns_df[top_companies]
print(portfolio_returns.head())

#mean returns
mean_returns = portfolio_returns.mean()
print(mean_returns.head())

#covariance matrix
cov_matrix = portfolio_returns.cov()
print(cov_matrix.shape)
print(cov_matrix.head())

#--------------------------------------------------
# Generate Random Weights (normalized to sum to 1)
#--------------------------------------------------
weights = np.random.random(20)
weights = weights / np.sum(weights)

print("Weights= ",weights)
print("Sum of Weights= ",weights.sum())

#--------------------------------------------------
# Portfolio Expected Return
#--------------------------------------------------
portfolio_return = np.sum(mean_returns * weights)
print("Portfolio Expected Return= ",portfolio_return)

#--------------------------------------------------
# Portfolio Volatility
#--------------------------------------------------
portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
print("Portfolio Volatility= ",portfolio_volatility)

#--------------------------------------------------
# Portfolio Sharpe Ratio
#--------------------------------------------------
portfolio_sharpe = portfolio_return / portfolio_volatility
print("Portfolio Sharpe Ratio:", portfolio_sharpe)
