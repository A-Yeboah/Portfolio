#!/usr/bin/env python3
#print out a date, given year, month, and day as numbers

months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
#A list with one ending for each number from 1 to 31

endings=["st", "nd", "rd"] + 17*["th"]\
         + ["st", "nd", "rd"] + 7*["th"]\
         + ["st"]
year=input("Year: ")
month=input("Month in number (1-12): ")
day=input("Day of the month (1-31): ")

month_number=int(month)
day_number=int(day)

#Since index starts from 0, substract 1 from month and day to get the actual index

month_name=months[month_number-1]
ordinal=day+endings[day_number-1]

print(month_name + " " + ordinal + ", " + year)
