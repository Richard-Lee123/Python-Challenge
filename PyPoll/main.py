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
    total_votes = [item[2] for item in data]
    print(list(set(total_votes)))
    
    for row in data:
        num_rows += 1

        # total += str(row[2])
    print(f"Total Votes: {num_rows}")
    # print(total)

    # col = []
    # for row in csvreader:
    #     col.append(row[2])
    # print(col)



#     for row in csvreader:
#         Candidate = str(row[2])
#         if Candidate == row[2]:
#             cand_data(row)

# name_count = 0

# def cand_data(cand_stats):

#     name = str(cand_stats[2])

#     name_count += str(name)
#     print(name)