"""
Optional Analytical Implementation using Python (Pandas)
E-Commerce Sales Data Analysis and Customer Insights
Student: Abhijeet Kundu | Roll No: 2306168 | B.Tech IT - SAP Data Analytics
"""

import pandas as pd

# Load Dataset
df = pd.read_csv('ecommerce_dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

print("=" * 55)
print("  E-COMMERCE SALES DATA ANALYSIS - Python Report")
print("=" * 55)

# 1. Revenue by Product Category
print("\n1. REVENUE BY PRODUCT CATEGORY")
print("-" * 35)
cat_revenue = df.groupby('Product_Category')['Amount'].sum().sort_values(ascending=False)
for cat, rev in cat_revenue.items():
    print(f"  {cat:<25} ₹{rev:>10,.0f}")
print(f"\n  TOP CATEGORY: {cat_revenue.idxmax()} (₹{cat_revenue.max():,.0f})")

# 2. Monthly Sales Trend
print("\n2. MONTHLY SALES TREND")
print("-" * 35)
monthly = df.groupby('Month')['Amount'].sum()
for month, revenue in monthly.items():
    print(f"  {str(month):<12}  ₹{revenue:>10,.0f}")

# 3. Payment Mode Distribution
print("\n3. PAYMENT MODE DISTRIBUTION")
print("-" * 35)
payment = df['Payment_Mode'].value_counts()
for mode, count in payment.items():
    pct = count / len(df) * 100
    print(f"  {mode:<20} {count:>3} orders  ({pct:.1f}%)")
print(f"\n  MOST USED: {payment.idxmax()} ({payment.max()} orders)")

# 4. New vs Returning Customers
print("\n4. NEW vs RETURNING CUSTOMERS")
print("-" * 35)
cust = df.groupby('Customer_Type').agg(
    Orders=('Order_ID', 'count'),
    Total_Revenue=('Amount', 'sum'),
    Avg_Order=('Amount', 'mean')
)
print(cust.to_string())

# 5. City-wise Revenue
print("\n5. CITY-WISE REVENUE")
print("-" * 35)
city_rev = df.groupby('City')['Amount'].sum().sort_values(ascending=False)
for city, rev in city_rev.items():
    print(f"  {city:<12}  ₹{rev:>10,.0f}")
print(f"\n  TOP CITY: {city_rev.idxmax()} (₹{city_rev.max():,.0f})")

print("\n" + "=" * 55)
print("  Analysis Complete")
print("=" * 55)
