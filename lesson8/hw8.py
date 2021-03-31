from datetime import timedelta, datetime


users = {'Viktorya': datetime(2021, 2, 21), 
        'Helen': datetime(2021, 2, 20),
        'Sasha': datetime(2021, 2, 22),
        'Kate': datetime(2021, 2, 23),
        'Valerii': datetime(2021, 2, 24),
        }


def find_users(users, day):
    birthday_list = []
    for name, birthday in users.items():
        if birthday.date() == day.date():
            birthday_list.append(name)
    
    return birthday_list

def congratulating_day(users):
    today = datetime.now()
    today_week_day = today.isoweekday()
    week_days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday'}
    birthday_list = {i: list() for i in range(1, 6)}
    monday_date = today - timedelta(how_day = today_week_day - 1)
    birthday_list[1] = (find_users(users, monday_date)) #Monday
    birthday_list[1].append(find_users(users, monday_date - timedelta(how_day = 1)))
    birthday_list[1].append(find_users(users, monday_date - timedelta(how_day = 2)))
    
    for day in range(2, 6):
        birthday_list[day] = find_users(users, monday_date + timedelta(how_day = day - 1))

    for day, list_user in birthday_list.items():
        if len(list_user) > 0:
            print(f'{week_days[day]}: ' + ", ".join(list_user))

congratulating_day(users)