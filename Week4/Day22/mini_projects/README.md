# Day 22 Mini Projects

## Project 1: Dataset Analyzer
**Libraries:** pandas, numpy

Build a simple dataset analyzer that:
- Loads a CSV file using `pd.read_csv()`
- Displays basic statistics (shape, columns, dtypes)
- Shows missing value counts using `df.isnull().sum()`
- Calculates summary statistics for numeric columns using `df.describe()`
- Exports a summary report to a text file

**Expected Input:** Any CSV file (e.g., sales data, employee records)
**Expected Output:** Text report with statistics and a cleaned DataFrame

## Project 2: Sales Data Dashboard
**Libraries:** pandas, numpy

Create a sales data analysis script that:
- Generates 500 rows of sample sales data using `np.random`
- Creates a DataFrame with columns:
  - `date`: datetime values (use `pd.date_range()`)
  - `product`: string (e.g., 'Laptop', 'Phone', 'Tablet', 'Watch')
  - `region`: string (e.g., 'North', 'South', 'East', 'West')
  - `units`: integer (1-50 range)
  - `revenue`: float (calculated from units * price)
- Performs groupby analysis by product and region
- Calculates key metrics (total revenue, average order value, top sellers)
- Saves results to CSV using `df.to_csv()`

**Expected Output:** sales_data.csv and sales_summary.csv

## Project 3: Data Cleaning Pipeline
**Libraries:** pandas, numpy

Build a data cleaning script that handles:
- Missing values: NaN, empty strings, 'N/A', 'NULL'
- Duplicate rows: exact duplicates and duplicates based on key columns
- Incorrect data types: dates stored as strings, numbers stored as text
- Inconsistent formatting: mixed case ('NYC', 'nyc', 'Nyc'), extra whitespace

Steps to implement:
1. Load messy data from CSV
2. Identify and log data quality issues
3. Clean each issue step by step with print statements
4. Export cleaned data to new CSV

**Expected Input:** messy_data.csv with intentional data quality issues
**Expected Output:** cleaned_data.csv and cleaning_log.txt

## Getting Started
1. Pick one project and create a new Python file
2. Import pandas and numpy
3. Use the concepts from Day 22 tutorials
4. Test with sample data before using real data

## Tips
- Start simple, add features incrementally
- Use functions to organize your code
- Add comments to explain your logic
- Test with different datasets
- Use `try/except` for error handling
