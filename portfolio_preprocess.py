import pandas as pd
import numpy as np

print("=" * 60)
print("LOADING DATASET")
print("=" * 60)

# Read raw dataset
df = pd.read_csv("data/raw/SnP_daily_update.csv")

print("Dataset Loaded Successfully!")
print("Shape:", df.shape)

print("\nFirst 3 Rows:")
print(df.head(3))

print("\nFirst 15 Columns:")
print(df.columns[:15].tolist())

# --------------------------------------------------
# STEP 1 : Extract ticker names
# --------------------------------------------------

tickers = df.iloc[0]

print("\nTicker Row:")
print(tickers.head(15))

# --------------------------------------------------
# STEP 2 : Calculate number of companies
# --------------------------------------------------

num_companies = (df.shape[1] - 1) // 5

print("\nNumber of Companies :", num_companies)

#--------------------------------------------------
# STEP 3 : Create a new DataFrame with relevant columns
#--------------------------------------------------
features = [ "Close","High","Low","Open","Volume"]
new_columns = ["Date"] 
for feature in features:
    for ticker in tickers:
        new_columns.append(f"{ticker}_{feature}")

print("\nTotal New Columns:", len(new_columns))

# ---------------------------------------------------
# Assign new column names
# ---------------------------------------------------

df.columns = new_columns

print("\nColumns Renamed Successfully!")

print(df.columns[:15])

# ---------------------------------------------------
# Remove metadata rows
# ---------------------------------------------------

df = df.iloc[2:].reset_index(drop=True)

print("\nMetadata Removed!")
print("New Shape:", df.shape)

# ---------------------------------------------------
# Save Intermediate Dataset
# ---------------------------------------------------

df.to_csv(
    "data/intermediate/renamed_columns.csv",
    index=False
)


print("\nIntermediate Dataset Saved!")