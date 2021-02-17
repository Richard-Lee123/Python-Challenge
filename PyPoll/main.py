import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

with open (election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    # print(csvreader)

    csv_header = next(csvreader)
    # print(csv_header)

    num_rows = 0
    total = 0

    data = list(csvreader)
    total_votes = [item[0] for item in data]
    # print(total_votes)
    
    for row in data:
        num_rows += 1

        total += int(row[0])

    print(f"Total Votes: {num_rows}")
