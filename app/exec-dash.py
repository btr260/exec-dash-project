##Exec Dashboard Project

#PACKAGES

import os
import operator
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import PySimpleGUI as sg



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

#Create list of files
data_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
data_files = os.listdir(data_filepath)
#print(data_files)

#initialize dataframe
master_data = pd.DataFrame()

#import all data
for dfile in data_files:
    temp = pd.read_csv(os.path.join(data_filepath, dfile))
    master_data=temp.append(master_data,ignore_index=True) # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html

#print(master_data)
#date            product  unit price  units sold  sales price
#0     2019-04-01        Khaki Pants       89.00           1        89.00
#1     2019-04-01  Button-Down Shirt       65.05           1        65.05
#2     2019-04-01   Vintage Logo Tee       15.95           2        31.90
#3     2019-04-01       Sticker Pack        4.50           1         4.50
#4     2019-04-02        Khaki Pants       89.00           1        89.00
#...          ...                ...         ...         ...          ...
#2342  2017-10-30        Khaki Pants       89.00           1        89.00
#2343  2017-10-30  Button-Down Shirt       65.05           4       260.20
#2344  2017-10-30   Vintage Logo Tee       15.95           1        15.95
#2345  2017-10-30       Sticker Pack        4.50           3        13.50
#2346  2017-10-31       Sticker Pack        4.50           2         9.00

master_data['year']=master_data['date'].str.split('-').str[0]
master_data['month'] = master_data['date'].str.split('-').str[1]
master_data['yearmon']=master_data['year']+master_data['month']
#print(master_data)
#date            product  unit price  ...  sales price  year  month
#0     2019-04-01        Khaki Pants       89.00  ...        89.00  2019      4
#1     2019-04-01  Button-Down Shirt       65.05  ...        65.05  2019      4
#2     2019-04-01   Vintage Logo Tee       15.95  ...        31.90  2019      4
#3     2019-04-01       Sticker Pack        4.50  ...         4.50  2019      4
#4     2019-04-02        Khaki Pants       89.00  ...        89.00  2019      4
#...          ...                ...         ...  ...          ...   ...    ...
#2342  2017-10-30        Khaki Pants       89.00  ...        89.00  2017     10
#2343  2017-10-30  Button-Down Shirt       65.05  ...       260.20  2017     10
#2344  2017-10-30   Vintage Logo Tee       15.95  ...        15.95  2017     10
#2345  2017-10-30       Sticker Pack        4.50  ...        13.50  2017     10
#2346  2017-10-31       Sticker Pack        4.50  ...         9.00  2017     10

#print(master_data.dtypes)
#date            object
#product         object
#unit price     float64
#units sold       int64
#sales price    float64
#year             int16
#month             int8



#sg.ChangeLookAndFeel("GreenTan")
#
#layout = [
#    [sg.Text("Welcome to your monthly sales report!",
#             size=(30, 1), font=("Helvetica", 25))],
#    [sg.Text("Please select the month of interest:")],
#    #[sg.InputText("This is my text")],
#    #[sg.Checkbox("My first checkbox!"), sg.Checkbox(
#    #    "My second checkbox!", default=True)],
#    #[sg.Radio("My first Radio!     ", "RADIO1", default=True),
#    # sg.Radio("My second Radio!", "RADIO1")],
#    #[sg.Multiline(default_text="This is the default Text should you decide not to type anything", size=(35, 3)),
#    # sg.Multiline(default_text="A second multi-line", size=(35, 3))],
#    #[sg.InputCombo(("Combobox 1", "Combobox 2"), size=(20, 3)),
#    # sg.Slider(range=(1, 100), orientation="h", size=(34, 20), default_value=85)],
#    [sg.Listbox(values=("Listbox 1", "Listbox 2", "Listbox 3"), size=(30, 3))],
#    [sg.Text("_" * 80)],
#    #[sg.Text("Choose A Folder", size=(35, 1))],
#    #[sg.Text("Your Folder", size=(15, 1), auto_size_text=False, justification="right"),
#    # sg.InputText("Default Folder"), sg.FolderBrowse()],
#    [sg.Submit(), sg.Cancel()]
#]
#
#window = sg.Window("Monthly sales report",
#                   default_element_size=(40, 1)).Layout(layout)
#button, values = window.Read()
#sg.Popup(button, values)





#TODO: FILE SELECTION

cur_month = input("Please input month (e.g. 'February'): ")
num_year=input("Please input year (e.g. 2019): ")
cur_year = str(num_year)
    #TODO: user input cur_month and cur_year
cur_ym = cur_year + month_num(cur_month)
#cur_csvname = f'sales-{cur_ym}.csv'
#cur_filepath = os.path.join(data_filepath, cur_csvname)
#print(cur_filepath)
#print(os.path.isfile(cur_filepath))


#TODO: CALCULATIONS ON SELECTED FILE

#cur_sales=pd.read_csv(cur_filepath)
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

month_prod_sales=master_data.groupby(['yearmon','product']).sum()
print(month_prod_sales)

month_total_sales = master_data.groupby(['yearmon']).sum()
print(month_total_sales)

breakpoint()

cur_total_sales=cur_sales["sales price"].sum()
#print(cur_total_sales)
cur_prod_sales = cur_sales.groupby(['product']).sum()
#print(cur_prod_sales)
cur_prod_sales=cur_prod_sales.sort_values(by=['sales price'],ascending=False)
#print(cur_prod_sales)


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


print('-----------------------')
print('VISUALIZING THE DATA...')

fig, ax = plt.subplots(figsize=(15,5))

plt.barh(cur_prod_sales.index, cur_prod_sales["sales price"], align='center')

#Source for y axis inversion: https://stackoverflow.com/questions/34076177/matplotlib-horizontal-bar-chart-barh-is-upside-down
plt.gca().invert_yaxis()

plt.xlabel(f"Total Sales in {cur_month} {cur_year} ($)",fontname='times new roman',fontweight='bold', fontsize='12', horizontalalignment='center')

plt.ylabel("Product", fontname='times new roman', fontweight='bold',fontsize='12', verticalalignment='center')

plt.grid(which='major',axis='x',linestyle="--")

#Source for axis label formatting: https://stackoverflow.com/questions/25973581/how-do-i-format-axis-number-format-to-thousands-with-a-comma-in-matplotlib
ax.get_xaxis().set_major_formatter(tck.FuncFormatter(lambda x, p: format(int(x), ',')))

#Source for tick formatting: http://jonathansoma.com/lede/data-studio/matplotlib/changing-fonts-in-matplotlib/
for tick in ax.get_xticklabels():
    tick.set_fontname('times new roman')

for tick in ax.get_yticklabels():
    tick.set_fontname('times new roman')

plt.title(f"Monthly Sales by Product\n{cur_month} {cur_year}",fontname='times new roman', fontweight='bold', fontsize='16')

plt.show()
