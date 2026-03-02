import re

def is_course_code(s: str) -> bool:
    return bool(re.fullmatch(r"[A-Z]{3}\d{3}", s))

text = input().strip()

if is_course_code(text):
    print(True)
else:
    print(False)