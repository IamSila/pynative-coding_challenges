# Write a Python code to remove characters from a string
# from 0 to n and return a new string.

def remove_chars(s, n):
    return s[n:]

string = "Hello, World!"
n = 5
new_string = remove_chars(string, n)
print(new_string)  
