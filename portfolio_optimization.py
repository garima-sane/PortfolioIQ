import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Daily Returns Dataset
returns_df = pd.read_csv("data/processed/daily_returns.csv")

print("Dataset Loaded!")
print(returns_df.shape)

print("\nFirst 5 Rows")
print(returns_df.head())

#Removing Date Column
returns = returns_df.drop(columns=["Date"])
print(returns.shape)

#Calculate Expected Daily Returns
expected_returns = returns.mean()
print("\nExpected Daily Returns: ")
print(expected_returns)

#Covariance Matrix
cov_matrix = returns.cov()
print("\nCovariance Matrix shape: ")
print(cov_matrix.shape)

#-----------------------------------------------------------------------------
#Generating Random Portfolios
#-----------------------------------------------------------------------------

# Number of Companies
num_assets = len(expected_returns)
print("\nNumber of Assets:", num_assets)

# Generate Random Weights
weights = np.random.random(num_assets)

# Normalize them
weights = weights / np.sum(weights)

# Learning Mode: Display nicely
weights_df = pd.DataFrame({
    "Company": expected_returns.index,
    "Weight": weights
})

weights_df = weights_df.sort_values(
    by="Weight",
    ascending=False
)

print("\nRandom Portfolio Allocation")
print(weights_df.head(20))

print("\nSum of Weights:", weights.sum())

#Portfolio Expected Return
portfolio_return = np.dot(weights, expected_returns)

print("Portfolio Expected Return:")
print(portfolio_return)

#-----------------------------------------------------------------------------
# Portfolio Risk (Standard Deviation)
#-----------------------------------------------------------------------------
cov_matrix = cov_matrix.values

portfolio_variance = np.dot(
    weights.T,
    np.dot(cov_matrix, weights)
)

portfolio_risk = np.sqrt(portfolio_variance)

print("Portfolio Risk:", portfolio_risk)

# Risk- Return (Sharpe Ratio)
risk_free_rate=0
sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_risk

print("Sharpe Ratio:", sharpe_ratio)

#-----------------------------------------------------------------------------
# Monte Carlo Simulation
#-----------------------------------------------------------------------------
portfolio_returns = []
portfolio_risks = []
portfolio_sharpes = []
portfolio_weights = []

for i in range(10000):

    weights = np.random.random(num_assets)
    weights /= np.sum(weights)

    portfolio_return = np.dot(weights, expected_returns)

    portfolio_variance = np.dot(
        weights.T,
        np.dot(cov_matrix, weights)
    )

    portfolio_risk = np.sqrt(portfolio_variance)

    sharpe = portfolio_return / portfolio_risk

    portfolio_returns.append(portfolio_return)
    portfolio_risks.append(portfolio_risk)
    portfolio_sharpes.append(sharpe)
    portfolio_weights.append(weights)

# Best Portfolio using Sharpe Ratio
best_index = np.argmax(portfolio_sharpes)
print(best_index)

best_return = portfolio_returns[best_index]
best_risk = portfolio_risks[best_index]
best_sharpe = portfolio_sharpes[best_index]
best_weights = portfolio_weights[best_index]

best_portfolio = pd.DataFrame({
    "Company": expected_returns.index,
    "Weight": best_weights
})

best_portfolio = best_portfolio.sort_values(
    by="Weight",
    ascending=False
)

print(best_portfolio.head(20))

#-----------------------------------------------------------------------------
# Plotting the Efficient Frontier
#-----------------------------------------------------------------------------
plt.figure(figsize=(10,6))

plt.scatter(
    portfolio_risks,
    portfolio_returns,
    c=portfolio_sharpes,
    cmap="viridis",
    s=8
)

plt.colorbar(label="Sharpe Ratio")

plt.scatter(
    best_risk,
    best_return,
    color="red",
    marker="*",
    s=250,
    label="Optimal Portfolio"
)

plt.xlabel("Risk")
plt.ylabel("Expected Return")
plt.title("Monte Carlo Portfolio Optimization")
plt.legend()

plt.savefig("outputs/efficient_frontier.png")
plt.show()