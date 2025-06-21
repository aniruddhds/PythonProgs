from datetime import datetime

def currentDay():
    today = datetime.now()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_name = days[today.weekday()]
    print(f"Today is: {day_name}")

currentDay()