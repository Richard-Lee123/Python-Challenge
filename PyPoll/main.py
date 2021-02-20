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
        
    vote_stats = [{'Candidate':row,
                    'Percentage of votes': f"{round((dictt[row]/num_rows)*100,3)}%",
                    'Vote Count': dictt[row]}for row in dictt]

    #Finding the winner 
    a = vote_stats[0]['Percentage of votes']
    b = vote_stats[1]['Percentage of votes']
    c = vote_stats[2]['Percentage of votes']
    d = vote_stats[3]['Percentage of votes']

    if a>b and a>c and a>d:
        winner = vote_stats[0]['Candidate']
    elif b>a and b>c and b>d:
        winner = vote_stats[1]['Candidate']
    elif c>a and c>b and c>d:
        winner = vote_stats[2]['Candidate']
    else: 
        winner = vote_stats[3]['Candidate']


    # final results to print    

    print("Election Results")
    print("------------------------------------------------------------------------------------")
    print(f"Total Votes: {num_rows}")
    print("------------------------------------------------------------------------------------")
    print(vote_stats[0])
    print(vote_stats[1])
    print(vote_stats[2])
    print(vote_stats[3])
    print("------------------------------------------------------------------------------------")
    print(f"Winner: {winner}")
    print("------------------------------------------------------------------------------------")

    ##breaking down the steps    
    # final_list = [{'Candidate': row, 'Votes': dictt[row]} for row in dictt]
    # finalname = [{'Candidate':row}for row in dictt]
    # finalcount = [{'Votes': dictt[row]} for row in dictt]
    # percentage = [{'Perc': dictt[row]/num_rows} for row in dictt]
    # print(final_list)
    # print(finalname)
    # print(finalcount)
    # print(percentage)

f_results = os.path.join("Resources","Results.txt")

with open(f_results,'w') as text_file:

    print("Election Results", file = text_file)
    print("------------------------------------------------------------------------------------", file = text_file)
    print(f"Total Votes: {num_rows}", file = text_file)
    print("------------------------------------------------------------------------------------", file = text_file)
    print(vote_stats[0], file = text_file)
    print(vote_stats[1], file = text_file)
    print(vote_stats[2], file = text_file)
    print(vote_stats[3], file = text_file)
    print("------------------------------------------------------------------------------------", file = text_file)
    print(f"Winner: {winner}", file = text_file)
    print("------------------------------------------------------------------------------------", file = text_file)