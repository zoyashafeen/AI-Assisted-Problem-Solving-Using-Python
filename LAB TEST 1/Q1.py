n = int(input("Enter the number of Fibonacci terms: "))
a, b = 0, 1
fib_sequence = []

for _ in range(n):
    fib_sequence.append(a)
    a, b = b, a + b

print("Fibonacci sequence up to", n, "terms:")
if n <= 0:
    print("Please enter a positive integer for the number of Fibonacci terms.")
else:
    print(fib_sequence)

# Explanation:
# The program takes input n for the number of Fibonacci terms.
# It initializes the first two Fibonacci numbers (a=0, b=1), then iteratively computes each next term.
# Each computed value of 'a' is appended to a list, updating values for the next iteration.
# The resulting sequence is printed.
