import re

def sum_numbers(text: str) -> int:
    numbers = re.findall(r"\d+", text)
    return sum(int(num) for num in numbers)


paragraph = input()
print(sum_numbers(paragraph))