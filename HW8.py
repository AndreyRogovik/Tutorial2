import datetime
from datetime import datetime, timedelta

users = [
    {'name': 'Марія', 'birthday': datetime(1968, 7, 27, 20, 42, 20, 68613)},
    {'name': 'Ігор',  'birthday': datetime(1963, 7, 28, 20, 42, 20, 68613)},
    {'name': 'Богдан', 'birthday': datetime(2002, 7, 29, 20, 42, 20, 68613)},
    {'name': 'Ольга', 'birthday': datetime(1998, 7, 30, 20, 42, 20, 68613)},
    {'name': 'Максим', 'birthday': datetime(1955, 7, 31, 20, 42, 20, 68613)},
    {'name': 'Юлія', 'birthday': datetime(2003, 8, 1, 20, 42, 20, 68613)},
    {'name': 'Олена', 'birthday': datetime(2006, 8, 2, 20, 42, 20, 68613)},
    {'name': 'Брат', 'birthday': datetime(1999, 8, 4, 20, 42, 20, 68613)},
    {'name': 'Богдан', 'birthday': datetime(1965, 11, 5, 20, 42, 20, 68613)},
    {'name': 'Киргиза Чупакабрівна Фігова', 'birthday': datetime(2001, 7, 31, 20, 42, 20, 68613)}
]

def get_birthdays_per_week(users):
    today = datetime.now()
    one_week_later = today + timedelta(days=7)
    # Знаходимо поточний день тижня (0 - понеділок, 1 - вівторок, ..., 6 - неділя)
    current_day = today.weekday()

    
    week_dict = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],   
    }
    
    
    for user in users:
        # Визначаю день народження в цьому році
        this_year_bd = datetime(year = today.year, month = user['birthday'].month, day = user['birthday'].day)
        # визначаю чи знаходиться день народження в тижневому діапазоні
        if  this_year_bd >= today and this_year_bd < one_week_later:
            # Визначаємо день тижня для дня народження користувача
            birthday_day = this_year_bd.strftime("%A")
            if this_year_bd.weekday() in range(0,5):
                # Додаємо ім'я користувача до списку за відповідним ключем у словнику
                week_dict[birthday_day].append(user['name'])
            else:
                # Додаємо ім'я користувача до списку понеділка
                week_dict['Monday'].append(user['name'])
        
    print("week_dict", week_dict)
    # Створюємо список днів тижня у відповідному порядку, починаючи з поточного дня
    days_list = list(week_dict.keys())
    week_days_ordered = days_list[current_day:] + days_list[:current_day]

    # Виводимо список іменинників на найближчі 7 днів
    for day in week_days_ordered:
        users_list = week_dict[day]
        if users_list:
            print(f"{day}: {', '.join(users_list)}")




print(get_birthdays_per_week(users))