
from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    if users == []:
        return {}

    if date.today().weekday() == 0:
        days_list = [-2, 6]
    elif date.today().weekday() == 6:
        days_list = [-1, 6]
    else:
        days_list = [0, 7]

    date_calend_list = [date.today() + timedelta(days=i) for i in range(days_list[0], days_list[1])]
    flag = date_calend_list[0].year != date_calend_list[-1].year
    
    birthday_name_week = [[], [], [], [], [], [], []]

    for user in users:
        user["birthday"] = user["birthday"].replace(year=date_calend_list[0].year)
        if flag and (user["birthday"] < date_calend_list[0]):
            user["birthday"] = user["birthday"].replace(year=date_calend_list[0].year + 1)
        if user["birthday"] in date_calend_list:
            birthday_name_week[user["birthday"].weekday()].append(user["name"])
            
    birthday_dict = {'Monday':birthday_name_week[5] + birthday_name_week[6] + birthday_name_week[0],
                     'Tuesday':birthday_name_week[1],
                     'Wednesday':birthday_name_week[2],
                     'Thursday':birthday_name_week[3],
                     'Friday':birthday_name_week[4],
                     }
    users = {key:value for key, value in birthday_dict.items() if value != []}

    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
