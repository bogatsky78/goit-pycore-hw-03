from datetime import datetime, date, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.02.15"},
    {"name": "John Smith", "birthday": "1990.02.19"},
    {"name": "John Connor", "birthday": "1990.10.03"},
    {"name": "John Wick", "birthday": "1990.01.02"}
]

def get_upcoming_birthdays(users):
    output = [];
    for user in users:
        congratulation_date = get_congratulation_date(user['birthday'])
        if(congratulation_date):
            output_item = user
            output_item['congratulation_date'] = congratulation_date.strftime("%Y-%m-%d")
            output.append(output_item)
    
    return output
    
def get_congratulation_date(birthday: str):
    birthday = datetime.strptime(birthday, "%Y.%m.%d")
    today = datetime.today().date();
    #today = datetime.strptime("2026.12.30", "%Y.%m.%d").date();

    birthday_this_year = date(today.year, birthday.month, birthday.day)
    if birthday_this_year < today:
        birthday_next = date(today.year + 1, birthday.month, birthday.day)
    else:
        birthday_next = birthday_this_year;

    if(today <= birthday_next) and ((today + timedelta(days=7)) >= birthday_next):
        if birthday_next.weekday() >= 5: 
            days_to_add = 7 - birthday_next.weekday()
            return birthday_next + timedelta(days=days_to_add)
        else:
            return birthday_next
            
    else:
        return False

if __name__ == "__main__":
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)