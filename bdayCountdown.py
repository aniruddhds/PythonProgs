from datetime import datetime

def birthday_info(birthday_str):
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
    now = datetime.now()

    # Calculate age
    age = now.year - birthday.year
    if (now.month, now.day) < (birthday.month, birthday.day):
        age -= 1

    # Calculate next birthday date
    next_birthday_year = now.year if (now.month, now.day) < (birthday.month, birthday.day) else now.year + 1
    next_birthday = datetime(next_birthday_year, birthday.month, birthday.day)

    # Time delta until next birthday
    delta = next_birthday - now
    days = delta.days
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    print(f"Age: {age} years")
    print(f"Time until next birthday: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

bday=input("Enter date of birth as YYYY-MM-DD: ")
birthday_info(bday)