# Day 22 Exercises

## Exercise 1: NumPy Arrays
Create a NumPy array with numbers 1-20, reshape it to 4x5, and:
- Find the sum of each row
- Find the mean of each column
- Extract the center 2x3 subarray

## Exercise 2: Array Operations
Given two arrays a = [1, 2, 3, 4, 5] and b = [2, 4, 6, 8, 10]:
- Multiply them element-wise
- Find elements in `a` that are less than their corresponding element in `b`
- Calculate the dot product

## Exercise 3: DataFrame Creation
Create a DataFrame with the following employee data:
- Names: ['John', 'Jane', 'Bob', 'Alice', 'Charlie']
- Ages: [32, 28, 45, 36, 41]
- Departments: ['IT', 'HR', 'IT', 'Finance', 'HR']
- Salaries: [65000, 55000, 75000, 70000, 58000]

Then:
- Display the first 3 rows
- Select only 'Name' and 'Salary' columns
- Filter employees older than 35

## Exercise 4: Data Cleaning
Given a DataFrame with missing values:
```python
data = {
    'product': ['A', 'B', np.nan, 'D', 'E'],
    'price': [100, np.nan, 150, 200, np.nan],
    'quantity': [10, 20, 15, np.nan, 25]
}
```
- Count missing values in each column
- Fill missing prices with the average price
- Drop rows where product is missing

## Exercise 5: Groupby Operations
Using your employee DataFrame:
- Calculate total salary by department
- Find average age by department
- Count employees in each department
- Find the highest paid employee in each department

## Solutions
Solutions are in the `solutions/` folder (create your own first!)
