# 📈 Dynamic Pricing Engine

This project implements a **dynamic pricing engine** that adjusts product prices based on inventory levels and recent sales data. The goal is to optimize pricing strategies in response to supply and demand while maintaining a minimum profit margin.

---

## 📁 Files

- `pricing_engine.py`: Python script that performs the price adjustments.
- `products.csv`: Input file containing product details like SKU, price, cost, and stock.
- `sales.csv`: Input file containing recent sales data (last 30 days).
- `updated_prices.csv`: Output file containing the updated pricing information.
- `README.md`: Project documentation and approach.

---

## 🔧 How It Works

### 1. **Input Files**
- **`products.csv`** contains:
  - SKU
  - Product name
  - Current price
  - Cost price
  - Stock level
- **`sales.csv`** contains:
  - SKU
  - Quantity sold in the last 30 days

### 2. **Pricing Rules**
The script applies pricing rules in the following order of precedence:

1. **Low Stock & High Demand**
   - Condition: `stock < 20` and `quantity_sold > 30`
   - Action: Increase price by 15%

2. **Dead Stock**
   - Condition: `stock > 200` and `quantity_sold == 0`
   - Action: Decrease price by 30%

3. **Overstocked Inventory**
   - Condition: `stock > 100` and `quantity_sold < 20`
   - Action: Decrease price by 10%

4. **Minimum Profit Margin (Always Applied)**
   - Ensures final price is at least **20% above the cost price**.

### 3. **Output**
- A new file called `updated_prices.csv` is created.
- Columns:
  - `sku`
  - `old_price` (with $ units)
  - `new_price` (with $ units)

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Install `pandas` if not already installed:
   ```bash
   pip install pandas
