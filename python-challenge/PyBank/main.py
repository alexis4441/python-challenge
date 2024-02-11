import os
import csv

csvpath = os.path.join('C:\\', 'Users', 'alexi', 'Desktop', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')


total_months = []
nettotal_profit = []
change_profit_losses = []

#open csv file and read through rows
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)
        for row in csvreader:

                total_months.append(row[0])
                nettotal_profit.append(int(row[1]))

#Find the net total amount
        for x in range(len(nettotal_profit)-1):
            change_profit_losses.append(nettotal_profit[x+1]-nettotal_profit[x])

#Changes in "Profit/Losses" over entire period and calculate the average
        average_change = sum(change_profit_losses)/len(change_profit_losses)

#Find Greatest Increase and Decrease over the entire period
        total = len(total_months)
        greatest_increase = max(change_profit_losses)
        greatest_decrease = min(change_profit_losses)



print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(nettotal_profit)}")
print(f"Average Change: ${str(round(average_change,2))}")

#Add date and amount
print(f"Greatest Increase in Profits: " + str(total_months[change_profit_losses.index(max(change_profit_losses))+1]) + " " + "($" + str(greatest_increase) + ")")
print(f"Greatest Decrease in Profits: " + str(total_months[change_profit_losses.index(min(change_profit_losses))+1]) + " " + "($" + str(greatest_decrease) + ")")

#export a text file
file = open("PyBank.txt","w")
file.write("Financial Analysis" + "\n")
file.write("----------------------------" + "\n")
file.write(f"Total Months: {len(total_months)}" + "\n")
file.write(f"Average Change: ${str(round(average_change,2))}" + "\n")
file.write(f"Greatest Increase in Profits: " + str(total_months[change_profit_losses.index(max(change_profit_losses))+1]) + " " + "($" + str(greatest_increase) + ")" + "\n")
file.write(f"Greatest Decrease in Profits: " + str(total_months[change_profit_losses.index(min(change_profit_losses))+1]) + " " + "($" + str(greatest_decrease) + ")" + "\n")
file.close()
