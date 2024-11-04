

"""Write a Python code to iterate the first 10 numbers,
and in each iteration, print the sum of the current and previous number.

previous = current -1 

#result1#
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5

"""


sum = 0 #15

for number in range(0, 10, 1):
    if number == 0:
        previous = 0
    else:
        previous = number - 1
    sum  = sum + number
    print(f"Current Number {number} Previous Number {previous} Sum: {sum}")

