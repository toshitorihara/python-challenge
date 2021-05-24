import os
import csv
csv_file = os.path.join("Resources", "bank.csv")
with open('bank.csv', newline='') as csvfile:
plreader = csv.reader(csvfile, delimiter=' ')
for row in plreader:
  print(', '.join(row))
