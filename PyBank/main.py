import os
import csv

<<<<<<< HEAD
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader) 
    revenue = []
    date = []
    rev_change = []
    #total = 0
    #total_months = 0

    for row in csvreader:
        revenue.append(float(row[1]))
        date.append(row[0])
        #total = total + int(row[1])
        #total_months+= 1

    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = round(sum(rev_change)/len(rev_change),2)
        max_rev_change = round(max(rev_change))
        min_rev_change = round(min(rev_change))
        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])

multiline_str = (
"Financial Analysis\n"
"----------------------------\n"
f"Total Months: {len(date)}\n"
f"Total: ${round(sum(revenue))}\n"
f"Average Change: ${avg_rev_change}\n"
f"Greatest Increase in Profits: {max_rev_change_date} (${max_rev_change})\n"
f"Greatest Decrease in Profits: {min_rev_change_date} (${min_rev_change})\n"  
)
print(multiline_str)

output_text = os.path.join("analysis", "financial_analysis.txt")
file1 = open(output_text, "w")
file1.write(multiline_str)
file1.close()
=======
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
    "Total Months: 86\n"
    f"Total: ${str(total)} \n"  
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
>>>>>>> f213fd4162910aab7afb81d8497beceee8fdadfc
