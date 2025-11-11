import datetime

date_input = input("Enter a date (in DD-MM-YYYY format): ")

day , month , year = map(int, date_input.split('-'))
date = datetime.date(year, month, day)

day_name = date.strftime("%A")
print(f"\nThe day on {date_input} was: {day_name}")