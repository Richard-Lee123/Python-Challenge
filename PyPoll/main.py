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
    dictt = {}

    data = list(csvreader)
    # total_votes = [item[2] for item in data]
    # print(list(set(total_votes)))
    
    # for row in data:
        # num_rows += 1

    #     # total += str(row[2])
    # print(f"Total Votes: {num_rows}")
    # # print(total)



    for row in data:

        num_rows += 1
        if row[2] not in dictt:
            dictt[row[2]]=0
        dictt[row[2]] = dictt[row[2]]+1

    # final_list = [{'Candidate': row, 'Votes': dictt[row]} for row in dictt]
    finalname = [{'Candidate':row}for row in dictt]
    finalcount = [{'Votes': dictt[row]} for row in dictt]
    percentage = [{'Perc': dictt[row]/num_rows} for row in dictt]
    print(finalname)
    print(finalcount)
    print(percentage)
    print(f"Total Votes: {num_rows}")
    # print(final_list)
    print(dictt[row[2]])
    
    # holder = 0

    # def cand_data(cand_stats):

    #     name = str(cand_stats[2])
    #     can_id = str(cand_stats[0])
    #     county = str(cand_stats[1])

