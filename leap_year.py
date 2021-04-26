# Filename: leap_year.py
# Author: Megan Black
# Description: Program that says if the year entered by the user is a leap year or not.

year = input("Please enter a year: ")
year_i = int(year)
if(year_i % 4 == 0 and year_i % 100 == 0 and year_i % 400 == 0):
  print(year + " is a leap year")
elif(year_i % 4 == 0 and year_i % 100 != 0):
  print(year + "is a leap year")
else:
  print(year + "is not a leap year") 
