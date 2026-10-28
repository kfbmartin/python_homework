import csv


def read_employees():
    employee_list = []
    employee_list_with_e = []

    with open('../csv/employees.csv', 'r') as file:
        reader = list(csv.reader(file))
    
        employee_list = [f"{row[1]} {row[2]}" for row in reader[1:]]

        employee_list_with_e = [name for name in  employee_list if 'e' in name]

        return employee_list, employee_list_with_e

print(read_employees())