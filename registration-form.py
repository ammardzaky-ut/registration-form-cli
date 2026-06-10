# Registration Form CLI

print("=== Registration Form ===")

# User inputs
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

address = input("Enter your address: ")
extra_address = input("Enter apartment/unit (optional): ")

if extra_address != "":
    address += ", " + extra_address

age = int(input("Enter your age: "))

user_info = full_name + " is " + str(age) + " years old"
print(user_info)

experience_years = int(input("Enter your years of experience: "))

experience_info = "Experience: " + str(experience_years) + " years"
print(experience_info)

position = input("Enter your position: ")
salary = int(input("Enter your salary: "))

user_card = (
    f"Employee: {full_name} | "
    f"Age: {age} | "
    f"Position: {position} | "
    f"Salary: ${salary}"
)

print(user_card)

employee_code = input("Enter employee code (example: DEV-2026-JD-001): ")

department = employee_code[0:3]
print("Department:", department)

year_code = employee_code[4:8]
print("Year:", year_code)

initials = employee_code[9:11]
print("Initials:", initials)

print("\n=== Registration Complete ===")
print("Name:", full_name)
print("Address:", address)