hours_worked = int(input("Enter number of hours worked : "))
def salary(hours):
    if hours<=40:
        return hours*200
    elif hours>40:
        return 8000+(hours-40)*300
    else:
        return False

salary_received = salary(hours_worked)
if not salary_received:
    print("Input out of bounds")
else:
    print(f"Salary is {salary_received}")