# PyBank Challenge
# Module for OS
import os

# Module for subprocess/terminal output
import subprocess
with open("output.txt", "w+") as output:
    subprocess.call(["python", "./main.py"], stdout=output)

# Module for reading CSV file
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    #for row in csvreader:
    #    print(row)

    # Get total number of months
    data = list(csvreader)
    total_months = len(data) - 1
     
    # Get total net amount of Profit/Loss
    total_net_amount = 0
    separated_month = []
    separated_amount = []
    
    for row in data:
        separated_month.append(row[0])
        separated_amount.append(row[1])
    
    separated_month.pop(0)
    separated_amount.pop(0)
        
    int_separated_amount = [int(x) for x in separated_amount]

    total_net_amount = sum(int_separated_amount)

    # Get the average change in Profit/Loss
    average_change = 0
    separated_month.pop(0)
    monthly_change_list = [int_separated_amount[i+1] - int_separated_amount[i] for i in range(len(int_separated_amount) -1)]
    average_change = sum(monthly_change_list)/len(monthly_change_list)
   
    # Get the greatest increase in profits (date and amount) over the entire period

    s_month, m_change_list = separated_month, monthly_change_list    
      
    greatest_increase = max(m_change_list)
    greatest_increase_index = m_change_list.index(max(m_change_list))

   
    # Get the greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(monthly_change_list)
    greatest_decrease_index = monthly_change_list.index(min(monthly_change_list))

    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months:" + str(total_months))
    print("Total:$"+ str(total_net_amount))
    print("Average Change:$" + str(round(average_change, 2)))
    print("Greatest Increase in Profits: " + s_month[greatest_increase_index] + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + s_month[greatest_decrease_index] + " ($" + str(greatest_decrease) + ")")