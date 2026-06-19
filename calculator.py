# Mini Calculator - Trade Finance Toolkit
# A simple command-line calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def main():
    print("=== Mini Calculator ===")
    print("Operations available: add, subtract, multiply")
    op = input("Choose operation: ")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if op == "add":
        print(f"Result: {add(x, y)}")
    elif op == "subtract":
        print(f"Result: {subtract(x, y)}")
    elif op == "multiply":
        print(f"Result: {multiply(x, y)}")
    else:
        print("Unknown operation")


if __name__ == "__main__":
    main()