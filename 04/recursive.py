'''
The sequence 0, 1, 1, 2, 3, 5, 8, … is known as the Fibonacci sequence.

Each successive number is found by adding up the two preceding numbers

We can define the function like this:

f(n) = f(n-1) + f(n-2), where f(n) represents the nth Fibonacci number and

f(0) = 0

f(1) = 1

Write a program, recursively that prints out the nth Fibonacci number.

'''
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = int(input("Enter the value of n: "))
print(f"The {n}th Fibonacci number (recursive) is: {fibonacci_recursive(n)}")
