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

    for row in csvreader:

        # Add date column information to csvreader file
        date.append(row[0])
        # Add profit/losses column information to csvreader file
        profit_losses.append(int(row[1]))

# Determine total number of months included in the budget_data csv file
total_months = len(date)

# Determine the net total amount of profit/losses over the entire period
total_profit_losses = sum(profit_losses)

# Determine the amount of change in profit/losses from month-to-month
profit_loss_change = []
for i in range (1,len(profit_losses)):
    profit_loss_change.append(profit_losses[i]-profit_losses[i-1])

# Determine the average of the changes in profit/losses over the entire period
average_profit_loss_change = round(sum(profit_loss_change)/(total_months-1),2)

# Determine the greatest increase amount in profits/losses (largest positive profit/losses change) over the entire period and associated date
greatest_increase_profit_loss_change = max(profit_loss_change)
month_year_greatest_increase_profit_loss_change = date[profit_loss_change.index(greatest_increase_profit_loss_change)+1]

# Determine the greatest decrease amount in profits/losses (largest negative profit/losses change) over the entire period and associated date
greatest_decrease_profit_loss_change = min(profit_loss_change)
month_year_greatest_decrease_profit_loss_change = date[profit_loss_change.index(greatest_decrease_profit_loss_change)+1]

#Set up output data to analysis folder
output_file = os.path.join("Analysis","financial_analysis.txt")

#Open the output file
with open(output_file,"w") as financial_analysis_file:
    writer = financial_analysis_file.write

    output=(" \n"
            f"Financial Analysis\n"
            " \n"
            "------------------------------\n"
            f"Total Months: {total_months}\n"
            " \n"
            f"Total: ${total_profit_losses}\n"
            " \n"
            f"Average Change: ${average_profit_loss_change}\n"
            " \n"
            f"Greatest Increase in Profits: {month_year_greatest_increase_profit_loss_change} (${greatest_increase_profit_loss_change})\n"
            " \n"
            f"Greatest Decrease in Profits: {month_year_greatest_decrease_profit_loss_change} (${greatest_decrease_profit_loss_change})\n" )
    financial_analysis_file.write(output)
    print(output)