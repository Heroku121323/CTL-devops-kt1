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

def main():
    if len(sys.argv) != 4:
        print(f"Правильное использование: {sys.argv[0]} <operation> <x> <y>")
        print("Доступные операции: add, subtract, multiply, divide, power")
        sys.exit(1)
    
    
    op, xs, ys = sys.argv[1], sys.argv[2], sys.argv[3]
    x = float(xs)
    y = float(ys)


    if op == "add":
        result = add(x, y)
    elif op == "subtract":
        result = subtract(x, y)
    elif op == "multiply":
        result = multiply(x, y)
    elif op == "divide":
        try:
            result = divide(x, y)
        except ValueError as e:
            print(e)
            sys.exit(1)
    elif op == "power":
        result = power(x, y)
    else:
        print(f"Неизвестная операция: {op}")
        sys.exit(1)


    print(f"Результат: {result}")
if __name__ == "__main__":
    main()