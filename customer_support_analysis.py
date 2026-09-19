import pandas as pd

# Load the customer support dataset
df = pd.read_csv("customer_support_data.csv")

print("CUSTOMER SUPPORT ANALYTICS")
print("=" * 40)

# Basic overview
print("\nTotal number of cases:")
print(len(df))

# Cases by category
print("\nCases by category:")
print(df["category"].value_counts())

# Average resolution time
print("\nAverage resolution time:")
print(round(df["resolution_hours"].mean(), 2), "hours")

# Average satisfaction
print("\nAverage customer satisfaction:")
print(round(df["satisfaction"].mean(), 2), "out of 5")

# Unresolved cases
unresolved = df[df["status"] == "Unresolved"]

print("\nUnresolved cases:")
print(len(unresolved))

# Average resolution time by category
print("\nAverage resolution time by category:")
print(
    df.groupby("category")["resolution_hours"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

# Average satisfaction by category
print("\nAverage satisfaction by category:")
print(
    df.groupby("category")["satisfaction"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)