import pandas as pd

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
    # Create a DataFrame from a dictionary:
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
task1_data_frame = df

    # Add a new column:
task1_with_salary = df.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

    # Modify an existing column:
task1_older = task1_with_salary.copy()
task1_older['Age'] += 1

    # Save the DataFrame as a CSV file:
task1_older.to_csv('employees.csv', index=False)

# Task 2: Loading Data from CSV and JSON
    # Read data from a CSV file:
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

    # Read data from a JSON file:
json_employees = pd.read_json('additional_employees.json')
print(json_employees)

    # Combine DataFrames:
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
    # Use the head() method:
first_three = more_employees.head(3)
print(first_three)

    # Use the tail() method:
last_two = more_employees.tail(2)
print(last_two)

    # Get the shape of a DataFrame
employee_shape = more_employees.shape
print(employee_shape)

    # Use the info() method:
print(more_employees.info())

# Task 4: Data Cleaning
    # Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.
dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data)
clean_data = dirty_data.copy()

    # Remove any duplicate rows from the DataFrame
clean_data = dirty_data.drop_duplicates()
print(clean_data)

    # Convert Age to numeric and handle missing values
clean_data['Age'] = clean_data['Age'].replace('unknown', pd.NA)
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
print(clean_data)

    # Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data['Salary'] = clean_data['Salary'].replace('unknown', pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print(clean_data)

    # Convert Hire Date to datetime
clean_data['Hire Date'] = clean_data['Hire Date'].replace('unknown', pd.NA)
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
clean_data['Hire Date'] = clean_data['Hire Date'].fillna(pd.to_datetime('2000-01-01'))
print(clean_data['Hire Date'])

    # Strip extra whitespace and standardize Name and Department as uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print(clean_data[['Name', 'Department']])
