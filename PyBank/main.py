# Modules
import os
import csv

# Prompt user for video lookup
profit_loss = input("What months are you looking for? ")

# Set path for file
csvpath = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

# Bonus
# ------------------------------------------
# Set variable to check if we found the video
found = False

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == profit_loss:
            print(row[0] + " has recorded a profit/loss of " + row[1])

            # BONUS: Set variable to confirm we have found the video
            found = True

            # BONUS: Stop at first results to avoid duplicates
            break

    # If the video is never found, alert the user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
