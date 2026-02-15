from datetime import datetime

def get_days_from_today(date):
    try:
        past_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - past_date).days
    except ValueError:
        raise ValueError(f"Невірний формат дати: '{date}'. Очікується формат 'РРРР-ММ-ДД'.")


if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))
    print(get_days_from_today("2025-12-31"))
