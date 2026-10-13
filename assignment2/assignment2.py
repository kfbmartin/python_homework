import csv
import os
import custom_module
from datetime import datetime

#Task 2: Read a CSV File
def read_employees():
   
    employee_dict = {}
    employee_list = []

    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = list(csv.reader(file))
         
        employee_dict["fields"] = reader[0]
        
        for row in reader[1:]:
            employee_list.append(row)
        
        employee_dict["rows"] = employee_list  

        return employee_dict
    except Exception as e:
        print(f"An error occurred reading the file: {e}")
       
employees = read_employees()

#Task 3: Find the Column Index
def column_index(string):
    position = employees["fields"].index(string)

    return position

employee_id_column = column_index("employee_id")

#Task 4: Find the Employee First Name
def first_name(row_number):
    return employees["rows"][row_number][column_index("first_name")]
    

print (employees)

#Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches=list(filter(employee_match, employees["rows"]))

    return matches

#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

#Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    employees["rows"].sort(key=lambda row:row[column_index("last_name")])

    return employees["rows"]

sort_by_last_name()

#Task 8: Create a dict for an Employee
def employee_dict(row):
    employee = {
        "first_name": row[1],
        "last_name": row[2],
        "phone":     row[3]
    }
    return employee


#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    all_employees = {}

    for row in employees ["rows"]:
        all_employees[row[0]] = employee_dict(row)

    return all_employees

#Task 10: Use the os Module
def get_this_value():
    return os.environ.get('THISVALUE')

#Task 11: Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Rainbows")
print(custom_module.secret)

#Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    minutes1 = {}
    minutes2 = {}

    minutes1_rows = []
    minutes2_rows = []

    try:
        with open('../csv/minutes1.csv', 'r') as file:
            reader = list(csv.reader(file))

            minutes1["fields"] = reader[0]

            for row in reader[1:]:
                minutes1_rows.append(tuple(row))

            minutes1["rows"] = minutes1_rows

        with open('../csv/minutes2.csv', 'r') as file:
            reader2 = list(csv.reader(file))

            minutes2["fields"] = reader2[0]

            for row in reader2[1:]:
                minutes2_rows.append(tuple(row))

            minutes2["rows"] = minutes2_rows
                 
    except Exception as e:
        print(f"An error occurred reading the file: {e}")

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

#Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    return set1| set2 

minutes_set = create_minutes_set()

#Task 14: Convert to datetime
def create_minutes_list():
    minutes_list = list(minutes_set)

    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))

    return minutes_list

minutes_list = create_minutes_list()

#Task 15: Write Out Sorted List
def write_sorted_list ():

    minutes_list_sorted = sorted(minutes_list, key=lambda x:x[1])

    #convert back to string
    minutes_list_sorted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list_sorted))

    #write to a csv file
    with open('./minutes.csv', 'w', newline='') as file:
    
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])   

        for row in minutes_list_sorted:
            writer.writerow(row)  # Write a data row

    return  minutes_list_sorted


write_sorted_list()