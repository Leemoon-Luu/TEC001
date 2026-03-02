import re

def redact_phone_numbers(text: str) -> str:
    pattern = r"\b\d{10}\b|\+84\d+"
    return re.sub(pattern, "[REDACTED]", text)


document = input()
print(redact_phone_numbers(document))