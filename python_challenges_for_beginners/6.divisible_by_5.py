"""
Write a Python code to display numbers from a list divisible by 5
"""

list1 = [10, 20, 33, 46, 55]
print(f"Give the list is {list1}")
length = len(list1)
print("Divisble by 5")

#using loops
for x in list1:
    if x % 5 == 0:
        print(x)

# using list compression
[print(i) for i in list1 if i % 5 == 0]
