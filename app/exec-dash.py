##Exec Dashboard Project

#PACKAGES

import os
import operator
import pandas as pd


#DATA



#FUNCTIONS

def to_usd(my_price):
    '''
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    '''
    return f'${my_price:,.2f}'  # > $12,000.71

def month_num(month):
    '''
    Converts a full month name to numeric string for file recognition.
    Param: month (string) like February
    Example: month_num('February')
    Returns: '02'
    '''
    if month == 'January':
        return '01'
    elif month == 'February':
        return '02'
    elif month == 'March':
        return '03'
    elif month == 'April':
        return '04'
    elif month == 'May':
        return '05'
    elif month == 'June':
        return '06'
    elif month == 'July':
        return '07'
    elif month == 'August':
        return '08'
    elif month == 'September':
        return '09'
    elif month == 'October':
        return '10'
    elif month == 'November':
        return '11'
    else:
        return '12'


#CODE

#TODO: FILE SELECTION

cur_month = 'April'
cur_year = '2019'
    #TODO: user input cur_month and cur_year
cur_ym = cur_year + month_num(cur_month)
cur_csvname = f'sales-{cur_ym}.csv'
cur_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', cur_csvname)
print(cur_filepath)
print(os.path.isfile(cur_filepath))


#TODO: CALCULATIONS ON SELECTED FILE

#TODO: CHARTS


#print('-----------------------')
#print('MONTH: March 2018')
#
#print('-----------------------')
#print('CRUNCHING THE DATA...')
#
#print('-----------------------')
#print('TOTAL MONTHLY SALES: $12,000.71')
#
#print('-----------------------')
#print('TOP SELLING PRODUCTS:')
#print('  1) Button-Down Shirt: $6,960.35')
#print('  2) Super Soft Hoodie: $1,875.00')
#print('  3) etc.')
#
#print('-----------------------')
#print('VISUALIZING THE DATA...')
#
