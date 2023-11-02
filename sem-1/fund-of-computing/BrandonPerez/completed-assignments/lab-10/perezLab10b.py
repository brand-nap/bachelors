# Name: Brandon Perez
# Class: CSCI 1411-006
# Due Date: 11/3/23
# Description: This program shows how to use functions in a Python
# program. It also shows how to use parameters to pass data
# to a function and return data from a function using a return
# statement.
# Status: Works as expected


# month_to_name function
# parameter: Takes an integer from 1-12 (to represent a month)
# returns equivalent month name in string format

def month_to_name(month):
    return "January" if month=='1' else "February" if month=='2' else "March" if month=='3' else "April" if month=='4' else "May" if month=='5' else "June" if month=='6' else "July" if month=='7' else "August" if month=='8' else "September" if month=='9' else "October" if month=='10' else "November" if month=='11' else "December" if month=='12' else "Invalid Month";

# split_date function
# parameter: takes short date with format 'mm/dd/yyyy'
# returns mm, dd, and yyyy

def split_date(short_date):
    return short_date.split('/')
        
# date_convert function
# parameter: takes date in short format '1/1/23'
# returns the day in a long format 'January 1, 2023'

def date_convert(short_date):
    return f'{month_to_name(split_date(short_date)[0])} {split_date(short_date)[1]}, {split_date(short_date)[2]}';
        
# main function
def main():
    short_date = input('Enter date: ');
    print(f'{short_date} in long format is {date_convert(short_date)}')
