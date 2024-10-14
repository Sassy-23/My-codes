def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    return x / y

def calculator():
    while True:
        #used float for decimals
        try:
            num1 = float(input("Enter your first number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue 

        try:
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        #If the input is not in the selection, It will loop back making a choice
        try:
            choice = input("Enter your choice: ")
        except ValueError:
            print("Invalid input. Please choose a valid operation.")
            continue
        #Used if statements for the choosing of operators
        if choice == '1':
            print(f"{num1} + {num2} = {addition(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtraction(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {division(num1, num2)}")
                #Added a "division by zero" error for more complexity
            else:
                print("Error: Division by zero is not allowed.")

        else:
            #For when you don't choose a valid operator
            print("Invalid choice. Please choose a valid operation.")
            continue
        #loops back to the start if yes
        while True:
            proceed = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            if proceed in ['yes', 'no']:
                break
            else:
                #if you input a different word
                print("Invalid input. Please enter 'yes' or 'no'.")
        #ends and close the calculator if no has been selected
        if proceed == 'no':
            print("Calculator is off.")
            break

print("Welcome to Calculator")
calculator()