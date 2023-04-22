
employee_db = {}


def add_employee():

    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    position = input("Enter employee position: ")
    salary = input("Enter employee salary: ")


    while not age.isnumeric() or not salary.isnumeric():
        print("Invalid input. Age and salary must be numeric values.")
        age = input("Enter employee age: ")
        salary = input("Enter employee salary: ")

    # Adding employee to dictionary
    employee_db[name] = {"age": int(age), "position": position, "salary": int(salary)}
    print("Employee added successfully!")


def update_employee():
 
    name = input("Enter employee name: ")
    field = input("Enter field to update (age, position, or salary): ")


    while field not in ["age", "position", "salary"]:
        print("Invalid input. Field must be 'age', 'position', or 'salary'.")
        field = input("Enter field to update (age, position, or salary): ")


    new_value = input(f"Enter new value for {field}: ")


    while (field in ["age", "salary"] and not new_value.isnumeric()) or (field == "position" and new_value == ""):
        print(f"Invalid input. {field} must be a numeric value." if field in ["age", "salary"] else f"Invalid input. {field} cannot be empty.")
        new_value = input(f"Enter new value for {field}: ")


    employee_db[name][field] = int(new_value) if field in ["age", "salary"] else new_value
    print("Employee information updated successfully!")


def delete_employee():

    name = input("Enter employee name: ")


    if name in employee_db:

        del employee_db[name]
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")


def view_employee_list():

    if not employee_db:
        print("Employee database is empty.")
    else:
        # Print table header
        print(f"{'Name':<20} {'Age':<10} {'Position':<20} {'Salary':<10}")

        # Print table rows
        for name, info in employee_db.items():
            print(f"{name:<20} {info['age']:<10} {info['position']:<20} {info['salary']:<10}")


def search_employee():

    search_term = input("Enter name or position to search for: ")


    results = []


    for name, info in employee_db.items():
        if search_term.lower() in name.lower() or search_term.lower() in info['position'].lower():
            results.append((name, info['age'], info['position'], info['salary']))


        if not results:
            print("No results found.")
        else:

            print(f"{'Name':<20} {'Age':<10} {'Position':<20} {'Salary':<10}")


        for result in results:
            print(f"{result[0]:<20} {result[1]:<10} {result[2]:<20} {result[3]:<10}")




def sort_employee_list():

    sort_field = input("Enter field to sort by (name, age, position, or salary): ")


    while sort_field not in ["name", "age", "position", "salary"]:
        print("Invalid input. Field must be 'name', 'age', 'position', or 'salary'.")
        sort_field = input("Enter field to sort by (name, age, position, or salary): ")


    if sort_field == "name":
        sorted_employee_list = sorted(employee_db.items())
    else:
        sorted_employee_list = sorted(employee_db.items(), key=lambda x: x[1][sort_field])


    print(f"Sorted by {sort_field}:")
    print(f"{'Name':<20} {'Age':<10} {'Position':<20} {'Salary':<10}")
    for name, info in sorted_employee_list:
        print(f"{name:<20} {info['age']:<10} {info['position']:<20} {info['salary']:<10}")


def main():
    while True:

        print("\nEmployee Database")
        print("1. Add employee")
        print("2. Update employee information")
        print("3. Delete employee")
        print("4. View employee list")
        print("5. Search for employees")
        print("6. Sort employee list")
        print("7. Quit")

        choice = input("Enter choice (1-7): ")


        if choice == "1":
          add_employee()
        elif choice == "2":
            update_employee()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            view_employee_list()
        elif choice == "5":
            search_employee()
        elif choice == "6":
            sort_employee_list()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

main()
