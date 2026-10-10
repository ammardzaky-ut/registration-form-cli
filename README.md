# Registration Form CLI (OOP Refactored)

An enterprise-pattern command-line employee registration system built with Python Object-Oriented Programming (OOP) principles. 

## Architecture & Features

This project demonstrates a clear separation of concerns by utilizing a lightweight Model-Controller architecture:
* **EmployeeModel (Data Layer):** Encapsulates employee attributes, manages data formatting (e.g., Title Case normalization), and auto-generates structured employee ID codes.
* **RegistrationController (Logic Layer):** Handles user interaction flow and implements defensive programming strategies (`try-except` blocks within `while` loops) to validate numerical inputs and prevent application crashes.
* **String Manipulation:** Demonstrates Python string slicing and dynamic f-string formatting for structured data output.

## How to Run

1. Ensure Python 3.x is installed.
2. Open a terminal in the project directory.
3. Execute the application:

```bash
python registration_form.py

## Example Output

```bash
=== Employee Registration Form ===
First Name: Alice
Last Name: Smith
Address: 123 Main St
Apartment/Unit (Optional): 4B
Age: 25
...

==============================
   REGISTRATION SUCCESSFUL
==============================
Employee ID : DEV-2026-AS-742
Name        : Alice Smith
Address     : 123 Main St, 4B
Profile     : 25 years old | 3 yrs exp.
Role        : DEVELOPER | Salary: $5,500.00

## Development Note

Originally written as a procedural script to understand basic I/O and variable assignments, this project has been refactored into an OOP structure to align with scalable backend development practices.

## Author

Created by Dzaky