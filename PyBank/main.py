import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# def print_total(budget_data)


#open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")



    # # reading the headers
    # csv_header = next(csv_file)
    # print(f"Header: {csv_header}")
