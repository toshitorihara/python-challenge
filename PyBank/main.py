import os
import csv

csvpath = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")
total = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:       
        total = total + int(row[1])

multiline_str = (
    "Financial Analysis\n"
    "----------------------------\n"
    "Total Months: len(row[0]) 86\n"
    f"Total: ${str(total)} \n"
    "Average Change: $ \n"
    "Greatest Increase in Profits: ($) \n"
    "Greatest Decrease in Profits: ($) \n"  
)
print(multiline_str)

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
# =======
# import os
# import csv
# csv_file = os.path.join("Resources", "bank.csv")
# with open('bank.csv', newline='') as csvfile:
# plreader = csv.reader(csvfile, delimiter=' ')
# for row in plreader:
#   print(', '.join(row))
