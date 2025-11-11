import random
import datetime

name = input("Enter Your name:")
today = datetime.datetime.now().strftime("%A")

lucky_number = random.randint(1, 100)
print(f"\nHello {name}! ")
print(f"Today is {today}, and your lucky numberis {lucky_number} ")