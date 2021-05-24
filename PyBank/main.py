import os
import csv
with open('bank.csv', newline='') as csvfile:
plreader = csv.reader(csvfile, delimiter=' ')
for row in plreader:
  print(', '.join(row))
