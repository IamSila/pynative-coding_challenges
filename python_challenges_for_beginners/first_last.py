"""
Write a code to return True if the list's first and last numbers are the same.
If the numbers are different, return False.
"""
from typing import List, Union

list1 = [20, 50, 90, 100, 20]

def same(numbers: int) -> bool:
    """
    compares the first and last values of list
    """
    if numbers[0] == numbers[-1]:
        return True
    else:
        return False


results: callable = same(list1)
print(results)



#classes

class Same(object):
    """class to check the first and last element in a list"""
    def __init__(self, nums: List[Union[int, int]]):
        self.nums = nums
    def compare(self):
        if self.nums[0] == self.nums[-1]:
            return True
        else:
            return False
    


obj1 = Same([30, 50, 60, 90, 30])
print(obj1.compare())

#promt chatgpt on how to use contents of dir(Same)