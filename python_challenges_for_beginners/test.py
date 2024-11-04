


def solution(num1: int, num2: int) -> int:
    sum = num1 + num2
    prod = num1 * num2

    if prod <= 1000:
        return f"The result is {prod}"
    else:
        return f"The result is {sum}"
    
result = solution(40, 30)
print(result)
