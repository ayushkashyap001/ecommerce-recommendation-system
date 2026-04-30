import pandas as pd

df = pd.read_csv("data/train.csv", nrows=5)

print(df.columns)
print(df.head())