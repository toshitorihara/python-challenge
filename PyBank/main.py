import os
import csv

profit_loss = input("What months are you looking for? ")
csvpath = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")
found = False
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if row[0] == profit_loss:
            print(row[0] + " has recorded a profit/loss of " + row[1])
            found = True
            break
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
=======
import os
import csv
csv_file = os.path.join("Resources", "bank.csv")
with open('bank.csv', newline='') as csvfile:
plreader = csv.reader(csvfile, delimiter=' ')
for row in plreader:
  print(', '.join(row))
