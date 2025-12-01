"""
Day 22 - Data Operations
========================
Learn: Filter, group, and aggregate operations

Key Concepts:
- Advanced filtering techniques
- Groupby operations
- Aggregation functions
- Pivot tables
- Merging and joining DataFrames
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("DATA OPERATIONS")
print("=" * 60)

# ========== CREATE SAMPLE DATA ==========
print("\n" + "=" * 60)
print("CREATING SAMPLE DATA")
print("=" * 60)

# Sales data
np.random.seed(42)
n_rows = 50

sales = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=n_rows, freq='D'),
    'product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Watch'], n_rows),
    'region': np.random.choice(['North', 'South', 'East', 'West'], n_rows),
    'salesperson': np.random.choice(['Alice', 'Bob', 'Charlie', 'Diana'], n_rows),
    'units': np.random.randint(1, 20, n_rows),
    'unit_price': np.random.choice([999, 699, 449, 299], n_rows)
})
sales['revenue'] = sales['units'] * sales['unit_price']
sales['month'] = sales['date'].dt.month_name()

print("Sales Data (first 10 rows):")
print(sales.head(10))
print(f"\nShape: {sales.shape}")

# ========== ADVANCED FILTERING ==========
print("\n" + "=" * 60)
print("ADVANCED FILTERING")
print("=" * 60)

print("\n1. Multiple conditions with & (AND):")
high_laptop = sales[(sales['product'] == 'Laptop') & (sales['units'] > 10)]
print(f"   Laptop sales with >10 units:\n{high_laptop.head()}")

print("\n2. Multiple conditions with | (OR):")
north_south = sales[(sales['region'] == 'North') | (sales['region'] == 'South')]
print(f"   North or South region: {len(north_south)} rows")

print("\n3. Using isin() for multiple values:")
selected_products = sales[sales['product'].isin(['Laptop', 'Phone'])]
print(f"   Laptop or Phone: {len(selected_products)} rows")

print("\n4. Using between():")
mid_revenue = sales[sales['revenue'].between(2000, 5000)]
print(f"   Revenue between 2000-5000: {len(mid_revenue)} rows")

print("\n5. String filtering with str methods:")
alice_sales = sales[sales['salesperson'].str.startswith('A')]
print(f"   Salesperson starting with 'A': {len(alice_sales)} rows")

print("\n6. Using query() - cleaner syntax:")
result = sales.query('product == "Laptop" and units > 10')
print(f"   Query result: {len(result)} rows")

print("\n7. Negation with ~:")
not_laptop = sales[~(sales['product'] == 'Laptop')]
print(f"   Not Laptop: {len(not_laptop)} rows")

# ========== SORTING ==========
print("\n" + "=" * 60)
print("SORTING")
print("=" * 60)

print("\n1. Sort by single column:")
sorted_rev = sales.sort_values('revenue', ascending=False)
print(f"Top 5 by revenue:\n{sorted_rev.head()}")

print("\n2. Sort by multiple columns:")
sorted_multi = sales.sort_values(['product', 'revenue'], ascending=[True, False])
print(f"Sorted by product then revenue:\n{sorted_multi.head(10)}")

print("\n3. Get top N with nlargest/nsmallest:")
print(f"Top 3 by units:\n{sales.nlargest(3, 'units')}")
print(f"\nBottom 3 by revenue:\n{sales.nsmallest(3, 'revenue')}")

# ========== GROUPBY OPERATIONS ==========
print("\n" + "=" * 60)
print("GROUPBY OPERATIONS")
print("=" * 60)

print("\n1. Basic groupby with single function:")
by_product = sales.groupby('product')['revenue'].sum()
print(f"Total revenue by product:\n{by_product}")

print("\n2. Multiple aggregations:")
by_product_stats = sales.groupby('product')['revenue'].agg(['sum', 'mean', 'count'])
print(f"\nRevenue stats by product:\n{by_product_stats}")

print("\n3. Group by multiple columns:")
by_prod_region = sales.groupby(['product', 'region'])['revenue'].sum()
print(f"\nRevenue by product and region:\n{by_prod_region}")

print("\n4. Different aggregations for different columns:")
agg_result = sales.groupby('product').agg({
    'units': 'sum',
    'revenue': ['sum', 'mean'],
    'salesperson': 'nunique'  # Count unique
})
print(f"\nMultiple aggregations:\n{agg_result}")

print("\n5. Reset index after groupby:")
by_product_df = sales.groupby('product')['revenue'].sum().reset_index()
by_product_df.columns = ['product', 'total_revenue']
print(f"\nAs DataFrame:\n{by_product_df}")

print("\n6. Groupby with transform (keep original shape):")
sales_with_avg = sales.copy()
sales_with_avg['product_avg'] = sales.groupby('product')['revenue'].transform('mean')
print(f"\nWith product average column:\n{sales_with_avg.head()}")

print("\n7. Groupby with filter:")
# Keep only products with total revenue > 20000
high_rev_products = sales.groupby('product').filter(lambda x: x['revenue'].sum() > 20000)
print(f"\nFiltered to high revenue products: {len(high_rev_products)} rows")
print(f"Remaining products: {high_rev_products['product'].unique()}")

# ========== AGGREGATION FUNCTIONS ==========
print("\n" + "=" * 60)
print("AGGREGATION FUNCTIONS")
print("=" * 60)

print("""
Common aggregation functions:
- sum()     : Total sum
- mean()    : Average
- median()  : Median value
- min()     : Minimum
- max()     : Maximum
- count()   : Number of non-null values
- nunique() : Number of unique values
- std()     : Standard deviation
- var()     : Variance
- first()   : First value
- last()    : Last value
""")

print("Example with named aggregations (pandas 0.25+):")
named_agg = sales.groupby('product').agg(
    total_units=('units', 'sum'),
    avg_revenue=('revenue', 'mean'),
    max_sale=('revenue', 'max'),
    sale_count=('revenue', 'count')
).round(2)
print(named_agg)

# ========== PIVOT TABLES ==========
print("\n" + "=" * 60)
print("PIVOT TABLES")
print("=" * 60)

print("\n1. Basic pivot table:")
pivot = sales.pivot_table(
    values='revenue',
    index='product',
    columns='region',
    aggfunc='sum'
)
print(f"Revenue by Product and Region:\n{pivot}")

print("\n2. Pivot with multiple values:")
pivot_multi = sales.pivot_table(
    values=['units', 'revenue'],
    index='product',
    columns='region',
    aggfunc='sum',
    fill_value=0
)
print(f"\nUnits and Revenue:\n{pivot_multi}")

print("\n3. Pivot with margins (totals):")
pivot_margins = sales.pivot_table(
    values='revenue',
    index='product',
    columns='region',
    aggfunc='sum',
    margins=True,
    margins_name='Total'
)
print(f"\nWith totals:\n{pivot_margins}")

# ========== VALUE COUNTS ==========
print("\n" + "=" * 60)
print("VALUE COUNTS")
print("=" * 60)

print("\n1. Basic value counts:")
print(sales['product'].value_counts())

print("\n2. Value counts with percentages:")
print(sales['product'].value_counts(normalize=True).round(2))

print("\n3. Sorted by index:")
print(sales['product'].value_counts().sort_index())

print("\n4. Value counts with bins (for numeric):")
print(pd.cut(sales['revenue'], bins=5).value_counts().sort_index())

# ========== MERGING DATAFRAMES ==========
print("\n" + "=" * 60)
print("MERGING DATAFRAMES")
print("=" * 60)

# Create related data
products = pd.DataFrame({
    'product': ['Laptop', 'Phone', 'Tablet', 'Watch'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Wearable'],
    'weight_kg': [2.5, 0.2, 0.5, 0.1]
})

regions = pd.DataFrame({
    'region': ['North', 'South', 'East', 'West'],
    'country': ['USA', 'USA', 'USA', 'USA'],
    'timezone': ['EST', 'CST', 'EST', 'PST']
})

print(f"Products table:\n{products}\n")
print(f"Regions table:\n{regions}\n")

print("\n1. Inner merge (default):")
merged_inner = pd.merge(sales.head(5), products, on='product')
print(merged_inner)

print("\n2. Left merge (keep all from left):")
left_df = pd.DataFrame({'product': ['Laptop', 'Phone', 'Camera']})
merged_left = pd.merge(left_df, products, on='product', how='left')
print(merged_left)

print("\n3. Merge on different column names:")
sales_sample = sales.head(3).copy()
regions_renamed = regions.rename(columns={'region': 'area'})
merged_diff = pd.merge(sales_sample, regions_renamed, 
                       left_on='region', right_on='area')
print(merged_diff[['product', 'region', 'country', 'timezone']])

# ========== CONCATENATING DATAFRAMES ==========
print("\n" + "=" * 60)
print("CONCATENATING DATAFRAMES")
print("=" * 60)

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

print(f"df1:\n{df1}\n")
print(f"df2:\n{df2}\n")

print("1. Vertical concatenation (stack rows):")
concat_vertical = pd.concat([df1, df2], ignore_index=True)
print(concat_vertical)

print("\n2. Horizontal concatenation (add columns):")
concat_horizontal = pd.concat([df1, df2], axis=1)
print(concat_horizontal)

# ========== APPLY AND MAP ==========
print("\n" + "=" * 60)
print("APPLY AND MAP")
print("=" * 60)

print("\n1. Apply function to column:")
sales_sample = sales.head(5).copy()
sales_sample['revenue_category'] = sales_sample['revenue'].apply(
    lambda x: 'High' if x > 5000 else 'Medium' if x > 2000 else 'Low'
)
print(sales_sample[['product', 'revenue', 'revenue_category']])

print("\n2. Apply function to entire row:")
def format_sale(row):
    return f"{row['product']} - {row['units']} units - ${row['revenue']}"

sales_sample['description'] = sales_sample.apply(format_sale, axis=1)
print(sales_sample[['description']].head())

print("\n3. Map values to new values:")
product_emojis = {
    'Laptop': '💻', 
    'Phone': '📱', 
    'Tablet': '📲', 
    'Watch': '⌚'
}
sales_sample['emoji'] = sales_sample['product'].map(product_emojis)
print(sales_sample[['product', 'emoji']].head())

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Sales Report")
print("=" * 60)

print("\n📊 SALES REPORT")
print("-" * 40)

print(f"\nOverall Statistics:")
print(f"   Total Revenue: ${sales['revenue'].sum():,.2f}")
print(f"   Total Units: {sales['units'].sum()}")
print(f"   Average Order Value: ${sales['revenue'].mean():,.2f}")
print(f"   Number of Sales: {len(sales)}")

print(f"\nTop Products by Revenue:")
top_products = sales.groupby('product')['revenue'].sum().sort_values(ascending=False)
for product, revenue in top_products.items():
    print(f"   {product}: ${revenue:,.2f}")

print(f"\nTop Salesperson:")
top_salesperson = sales.groupby('salesperson').agg({
    'revenue': 'sum',
    'units': 'sum'
}).sort_values('revenue', ascending=False)
print(top_salesperson)

print(f"\nRegional Performance:")
regional = sales.groupby('region').agg({
    'revenue': ['sum', 'mean'],
    'units': 'sum'
}).round(2)
print(regional)

print(f"\nBest Day:")
best_day = sales.loc[sales['revenue'].idxmax()]
print(f"   Date: {best_day['date'].strftime('%Y-%m-%d')}")
print(f"   Product: {best_day['product']}")
print(f"   Revenue: ${best_day['revenue']:,.2f}")

print("\n" + "=" * 60)
print("✅ Data Operations - Complete!")
print("=" * 60)
