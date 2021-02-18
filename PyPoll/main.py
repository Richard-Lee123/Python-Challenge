import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

with open (election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    # print(csvreader)

    csv_header = next(csvreader)
    # print(csv_header)

    num_rows = 0
    dictt = {}

    data = list(csvreader)
    
    for row in data:

        num_rows += 1
        if row[2] not in dictt:
            dictt[row[2]]=0
        dictt[row[2]] = dictt[row[2]]+1
    finalfinal = [{'Candidate':row,'Percentage of votes': f"{round((dictt[row]/num_rows)*100,3)}%", 'Vote Count': dictt[row]}for row in dictt]
    print(f"Total Votes: {num_rows}")
    print(finalfinal)
    
    ##breaking down the steps    
    # final_list = [{'Candidate': row, 'Votes': dictt[row]} for row in dictt]
    # finalname = [{'Candidate':row}for row in dictt]
    # finalcount = [{'Votes': dictt[row]} for row in dictt]
    # percentage = [{'Perc': dictt[row]/num_rows} for row in dictt]
    # print(final_list)
    # print(finalname)
    # print(finalcount)
    # print(percentage)



