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

    birthday_this_year = date(today.year, birthday.month, birthday.day)
    if(today <= birthday_this_year) and ((today + timedelta(days=7)) >= birthday_this_year):
        if birthday_this_year.weekday() >= 5: 
            days_to_add = 7 - birthday_this_year.weekday()
            return birthday_this_year + timedelta(days=days_to_add)
        else:
            return birthday_this_year
            
    else:
        return False

if __name__ == "__main__":
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)