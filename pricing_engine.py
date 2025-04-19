import pandas as pd

# Load product and sales data
products_df = pd.read_csv("products.csv")
sales_df = pd.read_csv("sales.csv")

# Aggregate sales data to get quantity sold per SKU
sales_summary = sales_df.groupby("sku")["quantity_sold"].sum().reset_index()

# Merge sales data with product data
merged_df = pd.merge(products_df, sales_summary, on="sku", how="left")
merged_df["quantity_sold"].fillna(0, inplace=True)

# Apply pricing rules
def apply_pricing_rules(row):
    old_price = row["current_price"]
    new_price = old_price

    stock = row["stock"]
    sold = row["quantity_sold"]
    cost = row["cost_price"]

    # Rule 1: Low Stock, High Demand
    if stock < 20 and sold > 30:
        new_price = old_price * 1.15

    # Rule 2: Dead Stock
    elif stock > 200 and sold == 0:
        new_price = old_price * 0.70

    # Rule 3: Overstocked Inventory
    elif stock > 100 and sold < 20:
        new_price = old_price * 0.90

    # Rule 4: Minimum Profit Constraint
    min_price = cost * 1.2
    if new_price < min_price:
        new_price = min_price

    # Final rounding
    new_price = round(new_price, 2)

    return new_price

# Apply the pricing function
merged_df["new_price"] = merged_df.apply(apply_pricing_rules, axis=1)

# Prepare final output
output_df = merged_df[["sku", "current_price", "new_price"]].copy()
output_df.rename(columns={"current_price": "old_price"}, inplace=True)

# Add currency unit
output_df["old_price"] = output_df["old_price"].apply(lambda x: f"${x:.2f}")
output_df["new_price"] = output_df["new_price"].apply(lambda x: f"${x:.2f}")

# Save to CSV
output_df.to_csv("updated_prices.csv", index=False)
