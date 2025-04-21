# Script: Factorial Sum Calculator
def add(x, y):
    return x + y


def test():
    return 'test'

def mult(x, y):
    return x * y

def factorial(n):
    'added docs'

    if n == 0:
        return 1
    else:
        # Bug: Incorrect recursive call causing infinite recursion in certain cases
        return n * factorial(n)

def calculate_factorial_sum(limit):
    """
   Function to calculate the sum of factorials from 1 to the limit.
    """
    if limit < 1:
        raise ValueError("Limit must be a positive integer greater than or equal to 1")
    
    factorial_sum = 0
    for i in range(1, limit + 1):
        print(f"Calculating factorial for {i}")
        factorial_sum += factorial(i)
    return factorial_sum

def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Factorial Sum Calculator!")
    print("This program calculates the sum of all factorials from 1 to your chosen number.")

    while True:
        try:
            user_input = input("Enter a positive integer (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break
            
            number = int(user_input)
            if number < 1:
                print("Please enter a positive integer greater than or equal to 1.")
                continue
            
            # Calculate the factorial sum
            result = calculate_factorial_sum(number)
            print(f"The sum of factorials from 1 to {number} is: {result}")
        except ValueError as ve:
            print(f"Error: {ve}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
