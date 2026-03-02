import re

def is_hex_color(s: str) -> bool:
    return bool(re.fullmatch(r"#[0-9A-Fa-f]{6}", s))

while True:
    text = input().strip()

    if text.lower() == "done":
        print("END")
        break

    print(is_hex_color(text))