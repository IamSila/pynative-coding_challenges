

"""Write a Python code to accept a string from the user
and display characters present at an even index number.

For example, str = "PYnative".
                    0 2 4 67

so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

Orginal String is  PYnative



"""

string = input("Enter a string: ")
print(f"Orginal String is {string}")

length = len(string)
print("Printing only even index chars")

for index in range(0, length, 2):
    if index % 2 == 0:
        print(string[index])






