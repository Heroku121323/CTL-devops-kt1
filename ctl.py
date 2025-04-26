#!/usr/bin/python3
import sys
def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def power(x, y):
    """Raise x to the power of y."""
    return x ** y

def factorial(n):
    """Calculate the factorial of n."""
    if n < 0:
        raise ValueError("Cannot calculate factorial of a negative number.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def root(x):
    """Calculate the square root of x."""
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return x ** 0.5


def usage():
    print("Правильное использование: ctl.py <operation> <x> <y>")
    print("Доступные операции: add, subtract, multiply, divide, power, factorial")
    sys.exit(1)

OPS_ARITY = {
    "add": 2,
    "subtract": 2,
    "multiply": 2,
    "divide": 2,
    "power": 2,
    "factorial": 1,
    "root": 1
}

def main():
    # Проверяем, что операция задана и она поддерживается
    if len(sys.argv) < 2 or sys.argv[1] not in OPS_ARITY:
        usage()

    op = sys.argv[1]
    arity = OPS_ARITY[op]


    expected_len = 2 + OPS_ARITY[op]
    if len(sys.argv) != expected_len:
        usage()

    if arity == 1:
        x = int(sys.argv[2])
        y = None   
    else:
        x = int(sys.argv[2])
        y = int(sys.argv[3])


    if arity == 1:
        result = {
            "factorial": factorial,
            "root": root
        }[op](x)
    else:
        result = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide,
            "power": power
        }[op](x, y)


    print(f"Результат: {result}")
if __name__ == "__main__":
    main()