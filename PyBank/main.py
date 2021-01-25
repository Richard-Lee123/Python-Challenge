import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')


    
with open (budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    num_rows = 0
    total = 0


    data = list(csvreader)
    prof_loss = [item[1] for item in data]
    # print(prof_loss)

    for row in data:
        # print(row)

        print("-------------------------")
        print("Financial Analysis")
        print("-------------------------")

        num_rows += 1
        print(f"Total Months: {num_rows}")
    
        total += int(row[1])
        print(f"Total: ${total}")
        
    
    #creating the list
    t= prof_loss
    
    #converting str into int
    t_int = [int(i) for i in t] 
    # print(t_int) 

    #finding the difference between values in list
    diff = [t_int[i+1]-t_int[i] for i in range(len(t_int)-1)]
    # print(diff)

    avg_change = sum(diff)/len(diff)
    print(f"Average Change: ${round(avg_change,2)}")

    great_inc = max(diff)
    print(f"Greatest Increase in Profits: ${great_inc}")

    great_dec = min(diff)
    print(f"greatest Decrease in Profits: ${great_dec}")


