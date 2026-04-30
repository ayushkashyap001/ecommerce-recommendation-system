import pandas as pd
from src.recommender import Recommender

# Load dataset
df = pd.read_csv("data/train.csv", nrows=10000)

print("Dataset loaded ✔")

# Build model
rec = Recommender(df)
rec.build_model()

# Test using first product
product = df['TITLE'].iloc[0]

print("\nBase Product:")
print(product)

print("\nRecommended Products:\n")

print(rec.recommend(product))