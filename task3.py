import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(num):
    pattern = r'[^0-9]' 
    replacement = ''

    num = re.sub(pattern, replacement, num)
    if num[0 : 2] != "38":
        num = "+38" + num
    else:
        num = "+" + num

    return num


if __name__ == "__main__":
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)