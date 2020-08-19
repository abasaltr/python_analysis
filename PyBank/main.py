# Import modules to create file paths across operating system and to read CSV file
import os
import csv

# Assign paths by concatenating arguments for the source and result file
file_path_source = os.path.join('resources', 'budget_data.csv')
file_path_result = os.path.join('analysis', 'result.txt')

# Initialize the following variables 
count = 0
amount = 0
change = 0
total_var = 0

# Use for calculating greatest increase in profits and decrease in losses
gpi = 0
gpi_rownum = 0
gld = 0
gld_rownum = 0

# Read the CSV file, specify delimiter and variable that holds contents
# Read the header row first and then declare a date list used for data in the "Date" column 
# and a money list used for data in the "Profit/Losses" column of the CSV file   
with open(file_path_source, 'r') as csvfile:   
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    date = []
    money = []

    # Read each row of data after the header, 
    # and then append the value for each date and amount to its corresponding lists
    # Assign counter by incrementing it by one for each row 
    # to determine the total number of months included in the dataset
    # Assign amount by summing each row amount to previous rows total amount
    # to determine the net total amount of "Profit/Losses" over the entire period
    for row in csvreader:
        date.append(row[0])  
        money.append(row[1])
        count += 1
        amount = amount + int(row[1])        

    # Initialize an index variable used for identifying a row number and 
    # declare a variance list for assigning the changes in "Profit/Losses"
    i = 0
    variance = []

    # Read each row of data within the "Profit/Losses" column
    # Calculate the change by subtracting the amount at current row from the next row
    # and appending it to the variance list and then for each iteration increment index by one
    # Assign the current gpi and gld and its row number based on the condition that 
    # if the current change is greater or lower then the previously calculated change
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

    # Read each row of changes within the variance list to calculate the 
    # net total amount over the entire period by summing its value for each row
    for row in variance:
        total_var = total_var + int(row)      

    # Calulate the average of the changes by dividing the net total amount by total months
    # and then rounding it to two decimal places
    avg_var = round((total_var / (count-1)), 2)  

# Output the results to the terminal
print("\n")
print("Financial Analysis")
print("-"*40)
print(f"Total Months: {count}")
print(f"Total Amount: ${amount}")
print("Average Change: ${:.2f}".format(avg_var))
print(f"Greatest Increase in Profits: {date[gpi_rownum]} (${gpi})")
print(f"Greatest Decrease in Losses: {date[gld_rownum]} (${gld})")

# Output the results to the textfile
with open(file_path_result, 'w') as textfile:
    textfile.write("Financial Analysis \n")
    textfile.write("-"*40 + "\n")
    textfile.write(f"Total Months: {count} \n")
    textfile.write(f"Total Amount: ${amount} \n")
    textfile.write("Average Change: ${:.2f} \n".format(avg_var))
    textfile.write(f"Greatest Increase in Profits: {date[gpi_rownum]} (${gpi}) \n")
    textfile.write(f"Greatest Decrease in Losses: {date[gld_rownum]} (${gld}) \n")

# Close the result file
textfile.close()