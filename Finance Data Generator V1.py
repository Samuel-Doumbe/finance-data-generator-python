#Finance Data Generator V1

import random
import csv
import datetime


#categories
revenue_cat=["Product Sales","Service Revenue","Other Income"]
expenses_cat=["Payroll","Rent","Utilities","Marketing","Logistics","Travel","Other"]
revenue_amount=[]
expenses_amount=[]

#List to hold records
rows=[]
#Transaction id
trsnx_id=1
trnsx_count=0

#User input for year and month
year=int(input("Enter the year : "))
month=int(input("Enter the month (1-12) : "))

#Revenue loop
for cat1 in revenue_cat:
    for i in range(random.randint(15,50)): #generate 10 revenue records (lines) per category
        cat_amount1=random.randint(50000,500000)
        random_day=random.randint(1,28)
        date_val=datetime.date(year,month,random_day)
        revenue_amount.append(cat_amount1)
        rows.append((trsnx_id,date_val.isoformat(),"Revenue",cat1,cat_amount1,"Auto Generated"))
        trsnx_id+=1
        trnsx_count+=1


for cat2 in expenses_cat:
    for i in range(random.randint(15,50)): #generate 10 expense records (lines) per category
        cat_amount2=random.randint(5000,150000)
        random_day=random.randint(1,28)
        date_val=datetime.date(year,month,random_day)
        expenses_amount.append(cat_amount2)
        rows.append((trsnx_id,date_val.isoformat(),"Expense",cat2,cat_amount2, "Auto Generated"))
        trsnx_id+=1
        trnsx_count+=1

with open("finance_data_generator_v1.csv",'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["trsnx_id","date","type","category","amount","description"])
    writer.writerows(rows)

#Finance Summary:
print("\n--- Monthly Finance Summary_v1 --- ")
total_revenue=sum(revenue_amount)
total_expenses=sum(expenses_amount)
profit=total_revenue - total_expenses
if total_revenue > 0:
    profit_margin=profit/total_revenue
else:
    profit_margin=0
print(f"""Period : {year}-{month:02d}
      Total Revenue: {round(total_revenue,2)}
      Total Expenses: {round(total_expenses,2)}
      Profit: {round(profit,2)}
      Profit Margin: {profit_margin:.1%}
      """)

#Open new csv for monthly summary
with open("monthly_summary_v1.csv",'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["year","month","total_revenue","total_expenses","profit","profit_margin","transaction_count"])
    writer.writerow([year,month,total_revenue,total_expenses,profit,profit_margin,trnsx_count])

print(rows[:5])








