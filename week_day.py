#  Write a program that takes a date as input and determines the day of the week 
# (Sunday, Monday, etc.).
from datetime import datetime

date_object = datetime.strptime("2000-12-5","%Y-%m-%d")
print(date_object.strftime("%A"))