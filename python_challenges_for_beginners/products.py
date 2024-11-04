"""Given two integer numbers, write a Python code to return
their product only if the product is equal to or lower than 1000.
Otherwise, return their sum."""



number1 = 40
number2 = 30

product = number1 * number2
sum = number1 + number2

# if product <= 1000:   #1200 > 1000
#     print(f"The result is {product}")
# else :
#     print(f"The result is {sum}")



"""solving with functions"""
def solution(num1: int, num2: int) -> int:
    sum = num1 + num2
    prod = num1 * num2

    if prod <= 1000:
        return f"The result is {prod}"
    else:
        return f"The result is {sum}"



"""solving with classes"""
class Solution:
    """a class to return sum or product based on a threshold"""
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @property
    def product(self):
        return self.num1 * self.num2
    
    @property
    def sum(self):
        return self.num1 + self.num2
    
    def display(self):
        if self.product <= 1000:  #10,000
            return "The result {}".format(self.product)
        else:
            return "The result {}".format(self.sum)



given1 = Solution(40, 30)
print(given1.display())