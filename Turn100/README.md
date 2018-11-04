# Codes Explanation 
so the objective of this code is to know when is the person will turn to 100 year
maybe the codes is not pythonic yet, feel free to give me some advice :) 

<pre>
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
</pre>
