#Module 3 Challenge: PyBank
#RyanJames Code Submission

#Environment: Activate PythonData

#Import the module:
import os
#Import the reading files:
import csv 

#Hard code the working directory:
#Creates a user friendly working directory regardless of operating system.
csvpath=os.path.join('..','Resources','budget_data_pybank.csv')
with open(csvpath, newline='') as csvfile:
    #Create an iterable object that holds all of our csv data.
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #Lists to store:
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []

    #Print list headers to results to be stored in.
    print(f"Header: {csv_header}")   

#List Calculations:

#Total Number of Months   
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))
    #Prints(total_number_of_month)

 #Total Revenue Yeilded
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)
    #Prints(total_revenue)

 #Average Monthly Change in Revenue
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    monthly_change = Total / len(revenue_change)
    print(monthly_change)
    #Prints(monthly_change)
  
#Greatest Increase in Profits
    profit_increase = max(revenue_change)
    print(profit_increase)
    j = revenue_change.index(profit_increase)
    greatest_monthly_increase = month[j+1]
    #Prints(greatest_monthly_increase)
    
#Greatest Decrease in Profits
    profit_decrease = min(revenue_change)
    print(profit_decrease)
    k = revenue_change.index(profit_decrease)
    greatest_monthly_decrease = month[k+1]
    #Prints(greatest_monthly_decrease)

#Print Statements
print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')

#Total Months
print("Total Months: " + str(len(month)))
#Total Revenue in Period
print("Total: $ " + str(total_revenue)) 
#Average Monthly Change in Revenye
print("Average Change : $" + str(monthly_change))
#Greatest Increase in Profits
print(f"Greatest Increase in Profits: {greatest_monthly_increase} (${profit_increase})")
#Greatest Decrease in Profits
print(f"Greatest Decrease in Profits: {greatest_monthly_decrease} (${profit_decrease})")