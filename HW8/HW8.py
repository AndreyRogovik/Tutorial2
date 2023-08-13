import datetime 
from datetime import datetime, timedelta


users = [
    {'name': 'Марія', 'birthday': datetime (1968, 7, 27, 20, 42, 20, 68613)}, 
    {'name': 'Ігор',  'birthday': datetime (1963, 7, 28, 20, 42, 20, 68613)}, 
    {'name': 'Богдан','birthday': datetime (2002, 7, 29, 20, 42, 20, 68613)}, 
    {'name': 'Ольга', 'birthday': datetime (1998, 7, 30, 20, 42, 20, 68613)}, 
    {'name': 'Максим','birthday': datetime (1955, 7, 31, 20, 42, 20, 68613)}, 
    {'name': 'Юлія',  'birthday': datetime (2003, 8, 1, 20, 42, 20, 68613)}, 
    {'name': 'Олена', 'birthday': datetime (2006, 8, 2, 20, 42, 20, 68613)}, 
    {'name': 'Брат',  'birthday': datetime (1999, 8, 4, 20, 42, 20, 68613)}, 
    {'name': 'Богдан','birthday': datetime (1965, 11, 5, 20, 42, 20, 68613)}, 
    {'name': 'Киргиза Чупакабрівна Фігова', 'birthday': datetime(2001, 7, 31, 20, 42, 20, 68613)}
]


def get_birthdays_per_week(users):
    today = datetime.now()

    week_dict = {
        "Monday"    : [],
        "Tuesday"   : [],
        "Wednesday" : [],
        "Thursday"  : [],
        "Friday"    : [],
        "Saturday"  : [],
        "Sunday"    : [],   
    }

    # Ітерація на 7 днів вперед
    for i in range(7):       
        for user in users:
            # Перевіряю співпадіння дати ДН і поточної
            if today.month == user['birthday'].month and today.day == user['birthday'].day:
                
                if today.weekday() == 0: 
                    week_dict["Monday"].append(user['name'])

                elif today.weekday() == 1: 
                    week_dict["Tuesday"].append(user['name'])

                elif today.weekday() == 2: 
                    week_dict["Wednesday"].append(user['name'])

                elif today.weekday() == 3: 
                    week_dict["Thursday"].append(user['name'])

                elif today.weekday() == 4: 
                    week_dict["Friday"].append(user['name'])
                # У вихідні додаю у список вітань на ПН
                elif today.weekday() == 5: 
                    week_dict["Monday"].append(user['name'])

                elif today.weekday() == 6: 
                    week_dict["Monday"].append(user['name'])

        # Додаємо до поточної дати один день       
        today += timedelta(days=1)        
    # Виводимо список іменинників на найближчі 7 днів.    
    for day, users_list in week_dict.items():
            if users_list:
                print(f"{day}: {', '.join(users_list)}")


# Викликаємо функцію для виведення іменинників на тиждень
get_birthdays_per_week(users)