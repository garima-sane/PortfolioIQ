import pandas as pd

df = pd.read_csv("data/intermediate/renamed_columns.csv")

print(df[[
    "Date",
    "AAPL_Close",
    "AAPL_Open",
    "AAPL_High",
    "AAPL_Low",
    "AAPL_Volume"
]].head(10))