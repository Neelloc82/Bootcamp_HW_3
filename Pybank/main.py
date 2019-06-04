# import the os module
import os

# import the csv module and pull in file
import csv

# Set path for file 
csvpath = os.path.join('budget_data.csv')

# Lists to store data
months = []
profit = []



with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader, None)

    #budget_data_header = next(csvreader)
    #print(f"Budget Data Headers: {budget_data_header}")

    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))

total_months = len(months)

greatest_inc = profit[0]
greatest_dec = profit[0]
total_profit = 0

for x in range(len(profit)):
    if profit[x] >= greatest_inc:
        greatest_inc = profit[x]
        great_inc_month = months[x]
    elif profit[x] <= greatest_dec:
        greatest_dec = profit[x]
        great_dec_month = months[x]
    total_profit += profit[x]

average_change = round(total_profit/total_months, 2)

output_path = os.path.join('PyBank_Output.csv')

with open(output_path, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total: $' + str(total_profit) + '\n')
    writefile.writelines('Average Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Profits: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Profits: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')

with open(output_path, 'r') as readfile:
    print(readfile.read())






