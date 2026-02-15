import random

def get_numbers_ticket(min, max, quantity):
    try:
        min = normalize_input(min, 'min повинно бути цілим числом')
        if min < 1:
            raise ValueError("min повинно бути числом більше 1")
        
        max = normalize_input(max, 'max повинно бути цілим числом')
        if max < min:
            raise ValueError("max повинно бути більше ніж min")
        
        quantity = normalize_input(quantity, 'quantity повинно бути цілим числом')
        if quantity > (max - min):
            raise ValueError("quantity не може бути більшим ніж кількість варіантів в лотереї")
    except ValueError as e:
        print(f"Ви ввели хибні данні {e}")
        return []
    else:
        return random.sample(range(min, max + 1), quantity)
    
def normalize_input(value: str, error_message: str):
    if value.isdigit():
        return int(value)
    
    raise ValueError(error_message)

if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(input('Введіть min:'), input('Введіть max:'), input('Введіть quantity:'))
    print(lottery_numbers)