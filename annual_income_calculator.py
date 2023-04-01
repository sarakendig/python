# Author: Sara Kendig
# Date: March 31, 2023
# Purpose: to calculate annual income

# collect variables and print them to screen

# get hours per week
hours_per_week_inp= input("Enter hours worked per week: ")

# convert to int
hours_per_week = int(hours_per_week_inp)
print("Your hours per week:")
print(hours_per_week)

#get hourly wage
hourly_wage_inp = input("Enter hourly wage: ")

# convert to int
hourly_wage = int(hourly_wage_inp)
print("Your hourly wage is: ")
print(hourly_wage)

# calculate income per week
income_per_week = hours_per_week * hourly_wage

# get weeks per year
weeks_per_year_inp = input("Enter weeks worked per year: ")

# convert to int
weeks_per_year = int(weeks_per_year_inp)
print("Weeks per year: ")
print(weeks_per_year)

# calculate annual income
annual_income = income_per_week * weeks_per_year
print("Your annual income is: ")
print(annual_income)





