# Filename: leap_year.py
# Author: Megan Black
# Description: Program that says if the year entered by the user is a leap year or not.

# Function to error check user input
def check():
  year = input("Please enter a year: ")
  while(1):
    if year.isdigit():
      if len(year) == 4:
        return int(year)
      else:
        year = input("You didn't enter a good value, enter a valid year: ")
    else:
      year = input("You didn't enter a good value, enter a valid year: ")
  


year = check()
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
  print(year + " is a leap year")
elif year % 4 == 0 and year % 100 != 0:
  print(str(year) + " is a leap year")
else:
  print(str(year) + " is not a leap year") 
