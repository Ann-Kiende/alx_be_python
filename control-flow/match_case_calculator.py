num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        addition = num1 + num2
        print("The result is "+addition)

    case "-":
        subtract = num1 - num2
        print("The result is "+subtract)

    case "*":
        multiply = num1 * num2
        print("The result is "+multiply)
    
    case "/":
        divide = num1 / num2
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("The result is "+divide)

