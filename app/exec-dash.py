##Exec Dashboard Project

# PACKAGES and MODULES----------------------------------------------------------

import os
import operator
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import PySimpleGUI as sg



# FUNCTIONS----------------------------------------------------------------------

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

def rev_month_num(mnum):
    if mnum == '01':
        return 'January'
    elif mnum == '02':
        return 'February'
    elif mnum == '03':
        return 'March'
    elif mnum == '04':
        return 'April'
    elif mnum == '05':
        return 'May'
    elif mnum == '06':
        return 'June'
    elif mnum == '07':
        return 'July'
    elif mnum == '08':
        return 'August'
    elif mnum == '09':
        return 'September'
    elif mnum == '10':
        return 'October'
    elif mnum == '11':
        return 'November'
    else:
        return 'December'

def validate(user_input,ref_list):
    store=0
    for item in ref_list:
        if item==user_input:
            store+=1
    if store>0:
        return "match"
    elif user_input=="Exit":
        return "exit"
    else:
        return "no match"

def prev_year(user_month,user_year,min_date):
    if user_month=="01":
        m_end="12"
        y_end=str(int(user_year)-1)
    else:
        y_end=user_year
        if int(user_month)<=10:
            m_end="0"+str(int(user_month)-1)
        else:
            m_end=str(int(user_month)-1)
    m_st=user_month
    y_st=str(int(user_year)-1)

    comp_str=y_st+m_st
    comp_int=int(comp_str)
    repl_int=max(int(min_date),comp_int)
    repl_str=str(repl_int)

    if repl_str!=comp_str:
        m_st=repl_str[0:4]
        y_st=repl_str[-2:]

    return [m_st,y_st,m_end,y_end]


# DATA---------------------------------------------------------------------------

# Create list of files
data_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
data_files = os.listdir(data_filepath)
#print(data_files)

#initialize dataframe
master_data = pd.DataFrame()

# import all data
for dfile in data_files:
    temp = pd.read_csv(os.path.join(data_filepath, dfile))
    master_data=temp.append(master_data,ignore_index=True) # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html


master_data['year']=master_data['date'].str.split('-').str[0]
master_data['month'] = master_data['date'].str.split('-').str[1]
master_data['yearmon']=master_data['year']+master_data['month']
master_data['yearmon num']=pd.to_numeric(master_data['yearmon'])


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





# List reporting periods

print('----------------')
print('Available Reporting Months:')
print('----------------')
data_pds=[x.replace('sales-','') for x in data_files]
data_pds=[x.replace('.csv','') for x in data_pds]
data_pds=sorted(data_pds)
str_pds=[f"{rev_month_num(m[-2:])} {m[0:4]}" for m in data_pds]

for m in str_pds:
    print(m)

# Ask for user input

my_input=input("Please enter month and year of sales report (example: February 2019) or enter 'Exit' to exit the program: ")
my_input=my_input.title()

while validate(my_input,str_pds)=="no match":
    print('-------------------------')
    print('-------------------------')
    print('Your entry did not match a period with existing data.')
    print('Please review the available reporting months, confirm\nspelling, and use full month name and year separated by a space.')
    print('-------------------------')
    print('-------------------------')
    for m in str_pds:
        print(m)
    my_input = input("Please enter month and year of sales report (example: February 2019): ")

if validate(my_input,str_pds)=="exit":
    exit()

else:
    print('-------------------------')
    print('Thank you for your entry.\nGenerating sales report now...')
    print('-------------------------')

cur_month = my_input[:my_input.find(' ')]
cur_year=my_input[-4:]
cur_ym = cur_year + month_num(cur_month)
cur_month_int=int(month_num(cur_month))
cur_year_int=int(cur_year)
cur_ym_int=int(cur_ym)

ltm=prev_year(month_num(cur_month),cur_year,data_pds[0])
print(ltm)


# Subset master data for current month and previous twelve months
cur_month_sales=master_data[master_data['yearmon']==cur_ym]

ltm_sales = master_data[(master_data['yearmon num'] <= int(ltm[3]+ltm[2])) & (master_data['yearmon num'] >= int(ltm[1]+ltm[0]))]

prev_sales=master_data[master_data['yearmon num']<=cur_ym_int]

#print(cur_month_sales)
#print(ltm_month_sales)

cur_total_sales=cur_month_sales['sales price'].sum()
#print('current sales total')
#print(cur_total_sales)

cur_prod_sales = cur_month_sales.groupby('product')['sales price'].sum()
cur_prod_sales=cur_prod_sales.sort_values(ascending=False)
#print('current prod sales')
print(cur_prod_sales)

ltm_total_sales = ltm_sales.groupby('yearmon')['sales price'].sum()
#print('ltm total sales')
#print(ltm_total_sales)

ltm_avg_sales=ltm_total_sales.mean()
#print('ltm avg sales')
#print(ltm_avg_sales)

ltm_prod_sales=ltm_sales.groupby(['yearmon','product'])['sales price'].sum()
#print('ltm prod sales')
#print(ltm_prod_sales)

ltm_avg_prod_sales=ltm_prod_sales.groupby(level='product').mean()
ltm_avg_prod_sales = ltm_avg_prod_sales.sort_values(ascending=False)
#print(ltm_avg_prod_sales)

# Full Time Series Total Sales

prev_total_sales = prev_sales.groupby('yearmon')['sales price'].sum()
#print('ltm total sales')
#print(ltm_total_sales)


#print('-----------------------')
#print(f'MONTH: {cur_month} {cur_year}')
#
#print('-----------------------')
#print('CRUNCHING THE DATA...')
#
#print('-----------------------')
#print(f'TOTAL MONTHLY SALES: {to_usd(cur_total_sales)}')

# Time Series Chart Total Sales

fig, ax = plt.subplots()

chtax = list(prev_total_sales.index)
fixax = [f"{x[:4]}-{x[-2:]}" for x in chtax]
#print(fixax)
ltm_pds = min(12, len(prev_total_sales) - 1)
prior_txt = f"Average of Prior {ltm_pds} Months: {to_usd(ltm_avg_sales)}"

if len(prev_total_sales) == 2:
    tot_fn = f"Current reporting month shown in green.  Prior {ltm_pds} month is shown in orange."
    prior_txt=f"Last Month: {to_usd(ltm_avg_sales)}"
elif len(prev_total_sales) == 1:
    tot_fn = f"Current reporting month shown in green (there are no prior months with available data)."
    prior_txt = ""
elif len(prev_total_sales) <= 13:
    tot_fn = f"Current reporting month shown in green.  Prior {ltm_pds} months are shown in orange."
else:
    tot_fn = f"Current reporting month shown in green.  Prior {ltm_pds} months are shown in orange.  Earlier months are shown in blue."


barlist = plt.bar(fixax, prev_total_sales, align='center')

plt.xlabel(f"Month\n\n{tot_fn} Close to see sales by product.", fontname='times new roman',
           fontweight='bold', fontsize='12', horizontalalignment='center')

plt.ylabel("Total Sales ($)", fontname='times new roman', fontweight='bold',
           fontsize='12', verticalalignment='center')

ax.get_yaxis().set_major_formatter(
    tck.FuncFormatter(lambda y, p: format(int(y), ',')))

for tick in ax.get_xticklabels():
    tick.set_fontname('times new roman')

for tick in ax.get_yticklabels():
    tick.set_fontname('times new roman')

plt.title(f"Total Sales Report\n\n{cur_month} {cur_year}: {to_usd(cur_total_sales)}\n{prior_txt}",
          fontname='times new roman', fontweight='bold', fontsize='14')

barlist[-1].set_color('g')
for x in range(2, 2 + ltm_pds):
    barlist[-x].set_color('orange')



plt.show()






user_top = 3 #TODO: let user specify number of products

print('-----------------------')
print(f"TOP {user_top} SELLING PRODUCTS:")

rank=0
for i, rows in cur_prod_sales.iteritems():
    rank+=1
    if rank <= user_top:
        print(f"  {rank}) {i}: {to_usd(rows)}")


print('-----------------------')
print('VISUALIZING THE DATA...')

fig, ax = plt.subplots()

plt.barh(cur_prod_sales.index, cur_prod_sales, align='center')

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
