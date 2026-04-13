

import pandas as pd

# Sample Dataset (Sales Data)
data = {
    "Region": ["East", "West", "North", "South", "East", "West"],
    "Product": ["A", "B", "A", "C", "B", "C"],
    "Sales": [100, 200, 150, 300, 250, 400],
    "Year": [2022, 2022, 2023, 2023, 2022, 2023]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# -----------------------------
# OLAP Operations
# -----------------------------

# 1. Slice (filter data for one year)
slice_data = df[df["Year"] == 2022]
print("\nSlice (Year = 2022):")
print(slice_data)

# 2. Dice (filter multiple conditions)
dice_data = df[(df["Region"] == "East") & (df["Product"] == "B")]
print("\nDice (Region = East & Product = B):")
print(dice_data)

# 3. Roll-up (aggregate sales by Region)
rollup = df.groupby("Region")["Sales"].sum()
print("\nRoll-up (Total Sales by Region):")
print(rollup)

# 4. Drill-down (more detailed view)
drilldown = df.groupby(["Region", "Product"])["Sales"].sum()
print("\nDrill-down (Region + Product):")
print(drilldown)
