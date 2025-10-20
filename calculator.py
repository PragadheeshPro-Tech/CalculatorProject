

def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    return result

def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

def divide(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        if n == 0:
            return "ERROR"
        result /= n
    return result

def show_menu():
    print("\n***** COMMAND LINE CALCULATOR *****")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def get_choice():
    return input("Enter your choice (1-5): ")

def get_numbers():
    try:
        raw_input = input("Enter numbers separated by spaces: ")
        numbers = [float(num) for num in raw_input.split()]
        if len(numbers) < 2:
            print("Please enter at least two numbers.")
            return None
        return numbers
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        return None

def perform_operation(choice):
    numbers = get_numbers()
    if numbers is None:
        return

    if choice == '1':
        result = add(numbers)
    elif choice == '2':
        result = subtract(numbers)
    elif choice == '3':
        result = multiply(numbers)
    elif choice == '4':
        result = divide(numbers)
    else:
        print("Invalid choice.")
        return

    print(f"Result = {result}")

def main():
    while True:
        show_menu()
        choice = get_choice()

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        perform_operation(choice)

if __name__ == "__main__":
    main()
