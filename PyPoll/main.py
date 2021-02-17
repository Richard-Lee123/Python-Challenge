import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

with open (election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    # print(csvreader)

    csv_header = next(csvreader)
    # print(csv_header)

    