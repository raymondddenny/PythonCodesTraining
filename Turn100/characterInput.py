# simple program to tell when the person is  gonna turn to 100 years old
# import datetime function to know the current year,month,date,etc
import datetime

# assign datetime to variable now
now = (datetime.datetime.now())

# variable costruction
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

# str.capitalize() for return a copy of string with its first character Capitalized and the rest lowercased
# the codes maybe not that pythonic yet, feel free to correct it :)
