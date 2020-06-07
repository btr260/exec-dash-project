##Exec Dashboard Project

#PACKAGES

import os
import operator
import pandas as pd
import matplotlib.pyplot as plt

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

cur_month = 'March'
cur_year = '2018'
    #TODO: user input cur_month and cur_year
cur_ym = cur_year + month_num(cur_month)
cur_csvname = f'sales-{cur_ym}.csv'
cur_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', cur_csvname)
print(cur_filepath)
print(os.path.isfile(cur_filepath))


#TODO: CALCULATIONS ON SELECTED FILE

cur_sales=pd.read_csv(cur_filepath)
#print(cur_sales)
#           date            product  unit price  units sold  sales price
#0    2019-04-01        Khaki Pants       89.00           1        89.00
#1    2019-04-01  Button-Down Shirt       65.05           1        65.05
#2    2019-04-01   Vintage Logo Tee       15.95           2        31.90
#3    2019-04-01       Sticker Pack        4.50           1         4.50
#4    2019-04-02        Khaki Pants       89.00           1        89.00
#..          ...                ...         ...         ...          ...
#110  2019-04-29        Khaki Pants       89.00           1        89.00
#111  2019-04-29   Vintage Logo Tee       15.95           2        31.90
#112  2019-04-30        Khaki Pants       89.00           1        89.00
#113  2019-04-30  Button-Down Shirt       65.05           3       195.15
#114  2019-04-30   Vintage Logo Tee       15.95           3        47.85

#print(type(cur_sales))  # > <class 'pandas.core.frame.DataFrame'>

cur_total_sales=cur_sales["sales price"].sum()
#print(cur_total_sales)
cur_prod_sales = cur_sales.groupby(['product']).sum()
#print(cur_prod_sales)
cur_prod_sales=cur_prod_sales.sort_values(by=['sales price'],ascending=False)
print(cur_prod_sales)


print('-----------------------')
print(f'MONTH: {cur_month} {cur_year}')

print('-----------------------')
print('CRUNCHING THE DATA...')

print('-----------------------')
print(f'TOTAL MONTHLY SALES: {to_usd(cur_total_sales)}')

user_top = 3 #TODO: let user specify number of products

print('-----------------------')
print(f"TOP {user_top} SELLING PRODUCTS:")

rank=0
for i, rows in cur_prod_sales.iterrows():
    rank+=1
    if rank <= user_top:
        print(f"  {rank}) {i}: {to_usd(rows['sales price'])}")



#TODO: CHARTS

fig, ax = plt.subplots(figsize=(15,5))
plt.barh(cur_prod_sales.index, cur_prod_sales["sales price"], align='center')
plt.gca().invert_yaxis()
plt.xlabel(f"Total Sales in {cur_month} {cur_year} ($)")
plt.ylabel("Product")
plt.show()
#
#print('-----------------------')
#print('VISUALIZING THE DATA...')
#
