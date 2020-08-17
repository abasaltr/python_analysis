import os
import csv

file_path_source = os.path.join('resources', 'budget_data.csv')
file_path_result = os.path.join('analysis', 'result.txt')

count = 0
amount = 0
change = 0
total_var = 0

gpi = 0
gpi_rownum = 0
gld = 0
gld_rownum = 0

with open(file_path_source, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')    
    header = next(csvreader)
    
    date = []
    money = []
    for row in csvreader:    
        date.append(row[0])
        money.append(row[1])
        count += 1
        amount = amount + int(row[1])        

    i = 0
    variance = []
    for row in money:
        if (i + 1) < count:
            change = int(money[i+1]) - int(money[i])       
            variance.append(str(change))
            if change > gpi:
                gpi = change
                gpi_rownum = i + 1
            elif change < gld:
                gld = change
                gld_rownum = i + 1
            i += 1

    for row in variance:
        total_var = total_var + int(row)      

    avg_var = round((total_var / (count-1)), 2)  

print("", "\n")
print("Financial Analysis")
print("-"*40)
print(f"Total Months: {count}")
print(f"Total Amount: ${amount}")
print("Average Change: ${:.2f}".format(avg_var))
print(f"Greatest Increase in Profits: {date[gpi_rownum]} (${gpi})")
print(f"Greatest Decrease in Profits: {date[gld_rownum]} (${gld})")

with open(file_path_result, 'w') as textfile:
    textfile.write("Financial Analysis \n")
    textfile.write("-"*40 + "\n")
    textfile.write(f"Total Months: {count} \n")
    textfile.write(f"Total Amount: ${amount} \n")
    textfile.write("Average Change: ${:.2f} \n".format(avg_var))
    textfile.write(f"Greatest Increase in Profits: {date[gpi_rownum]} (${gpi}) \n")
    textfile.write(f"Greatest Decrease in Profits: {date[gld_rownum]} (${gld}) \n")

textfile.close()


