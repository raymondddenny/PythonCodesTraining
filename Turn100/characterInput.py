# simple program to tell when the person is  gonna turn to 100 years old
import datetime
now = (datetime.datetime.now())

name = input("Siapakah Namamu ? : ")
age = int(input("Berapa Umurmu saat ini : "))

# 1.0 code
"""
years = 100 - age
yearsNow = now.year
turn100 = years + yearsNow
print("hello " + name+ ", you will turn to 100 years old in " + str(turn100))
"""
# 2.0 codes
turn100 = (100-age) + now.year
print("hello " + name.capitalize() +
      ", you will turn to 100 years old in " + str(turn100))
