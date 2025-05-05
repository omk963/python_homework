import csv

# Task 2: Read a CSV File
def read_employees():
    dict = {}
    list = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            dict['fields'] = next(reader)
            for row in reader:
                list.append(row)
            dict['rows'] = list
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        return dict
    
employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(column_header):
    try:
        return employees['fields'].index(column_header)
    except Exception as e:
        print(f"An error occurred: {e}")
    
employee_id_column = column_index('employee_id')
print(employee_id_column)

# Task 4: Find the Employee First Name
def first_name(row_index):
    try:
        index = column_index('first_name')
        return employees['rows'][row_index][index]
    except Exception as e:
        print(f"An error occurred: {e}")

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    index = column_index('last_name')
    employees['rows'].sort(key=lambda row: row[index])
    return employees['rows']

# Task 8: Create a dict for an Employee
def employee_dict(row):
    field = employees['fields'][1:]
    row_value = row[1:]
    return dict(zip(field, row_value))
print(employee_dict(employees['rows'][0]))

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    all_employees = {}
    for row in employees['rows']:
        id = row[employee_id_column]
        all_employees[id] = employee_dict(row)
    return all_employees

# Task 10: Use the os Module
import os
def get_this_value():
    return os.getenv('THISVALUE')

# Task 11: Creating Your Own Module
import custom_module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
set_that_secret('some_secret_value')
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    def read_minute(minute):
        dict = {}
        list = []
        dict['fields'] = next(minute)
        for row in minute:
            list.append(tuple(row))
        dict['rows'] = list
        return dict
    try:
        with open('../csv/minutes1.csv', 'r') as file1, open('../csv/minutes2.csv', 'r') as file2:
            reader1 = csv.reader(file1)
            reader2 = csv.reader(file2)
            
            return read_minute(reader1), read_minute(reader2)
    except Exception as e:
        print(f"An error occurred: {e}")
minutes1, minutes2 = read_minutes()
print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])
    combined_set = set1.union(set2)
    return combined_set
minutes_set = create_minutes_set()
print(minutes_set)

# Task 14: Convert to datetime
from datetime import datetime
def create_minutes_list():
    minutes_list = list(minutes_set)
    changed_list = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list)
    return list(changed_list)
minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    formatted_list = []
    try:
        with open('./minutes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1['fields'])
            for row in sorted_list:
                writer.writerow((row[0], row[1].strftime("%B %d, %Y")))
                list.append((row[0], row[1].strftime("%B %d, %Y")))
        return formatted_list
    except Exception as e:
        print(f"An error occurred: {e}")