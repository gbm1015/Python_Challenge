import os
import csv

budget_data = os.path.join("Resources","budget_data.csv")

# Lists to store data
date = []
profit_losses = []

# Open budget_data as csv file
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    # Note that csv file has a header row
    header = next(csvreader)

    For row in csvreader:

        # Add date column information to csvreader file
        date.append(row[0])
        # Add profit/losses column information to csvreader file
        profit_losses.append(int(row[1]))

# Determine total number of months included in the budget_data csv file
total_months = len(date)

# Determine the net total amount of "Profit/Losses" over the entire period
total_profit_losses = sum(profit_losses)

# Determine the amount of change in profit/losses from month-to-month
profit_loss_change = []
For i in range (2,len(profit_losses))
    profit_loss_change.append(profit_losses[i]-profit_losses[i-1])

# Determine the average of the changes in "Profit/Losses" over the entire period
average_profit_loss_change = (sum(profit_loss_change))/((total_months)-1)



