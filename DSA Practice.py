import time


def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Get user input
user_input = int(input("Enter a number: "))

# Check if the number is odd or even
result = check_odd_even(user_input)

# Display the result
print(f"The number {user_input} is {result}.")
# TIme efficency
start = time.time()
for i in range(1, 100):
    print(i)
print("Time Calculated to print number is ", time.time() - start)
# algorithm
n = 40
print(n * n)  # n square means 40 into 40
# constant time
i = {'Umang', 'shivansh', 'shaurya'}
print(i.__len__())


# Reverse String Tecxhnique
def my_function(x):
    return x[::-1]


mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)
