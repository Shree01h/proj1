# Importing a function from math_utils.py
from math_utils import add_numbers, multiply_numbers

def demonstrate_dependencies():
    # Using the imported functions
    result_add = add_numbers(5, 10)
    result_multiply = multiply_numbers(3, 4)

    print(f"Addition Result: {result_add}")
    print(f"Multiplication Result: {result_multiply}")

if __name__ == "__main__":
    demonstrate_dependencies()

# done
