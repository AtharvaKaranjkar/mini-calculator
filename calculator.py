# Mini Calculator - Trade Finance Toolkit
# A simple command-line calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

def show_help():
    print("This calculator performs: add, subtract, multiply, divide")

    
show_help()

def goodbye():
    print("Thanks for using Mini Calculator!")
    
def main():
    print("=== Mini Calculator ===")
    print("Available operations: add, subtract, multiply, divide")
    op = input("Choose operation: ")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if op == "add":
        print(f"Result: {add(x, y)}")
    elif op == "subtract":
        print(f"Result: {subtract(x, y)}")
    elif op == "multiply":
        print(f"Result: {multiply(x, y)}")
    elif op == "divide":
        print(f"Result: {divide(x, y)}")
    else:
        print("Unknown operation")


if __name__ == "__main__":
    main()
