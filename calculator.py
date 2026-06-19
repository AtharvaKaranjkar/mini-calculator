# Mini Calculator - Trade Finance Toolkit
# A simple command-line calculator

def add(a, b):
    return a + b


def main():
    print("=== Mini Calculator ===")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(f"Result: {add(x, y)}")


if __name__ == "__main__":
    main()
