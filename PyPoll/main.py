# Import modules to create file paths across operating system and to read CSV file
import os
import csv

# Assign paths by concatenating arguments for the source and result file
file_path_source = os.path.join('resources', 'election_data.csv')
file_path_result = os.path.join('analysis', 'result.txt')

# Initialize variable
vote_total = 0 

# Read the CSV file, specify delimiter and variable that holds contents
# Read the header row first and then declare a candidate list used for data in the "Candidate" column 
with open(file_path_source, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')    
    header = next(csvreader)
    candidate = []

    # Read each row of data after the header, 
    # and then append the candidate name to its corresponding list
    # Assign vote total counter by incrementing it by one for each row 
    # to determine the total number of votes included in the dataset
    for row in csvreader:
        candidate.append(row[2])
        vote_total += 1

    # Sort the candidate list alphabetically by name
    # and then initialize an index variable used for identifying a row number and 
    # initialize a vote tally variable used for determing total votes and 
    # declare a list for assigning total votes per candidate name
    candidate.sort()
    i = 0
    tally = 1
    vote_name = {}

    # Read each row of data within the candidate list to calculate the
    # total votes per name by incrementing index and vote tally by one for each row the name doesn't change
    # When the name changes, the tally will be assigned to the candidate name in the vote_name list
    # and then reset back to zero for the next iteration of candidate name to tally votes for
    for row in candidate:
        if (i + 1) < vote_total:
            if candidate[i+1] != candidate[i]:
                vote_name[tally] = candidate[i]
                tally = 0
            i += 1
            tally += 1
        else:  
            vote_name[tally] = candidate[i]

# Defined function that prints candidate detail to either the terminal or exports to file
# Passing arguments include the candidate vote_name listing, total votes, output file, and output location message
# Initialize a boolean flag used to determine the winner for the highest vote candidate
def print_summary(listing, votes, outfile, outloc):
    flag = True

    # Read each row of data within the candidate listing sorted by highest to lowest number of votes
    # Calculate percentage of votes for candidates by dividing the entire total votes by each vote totals
    # Output the candidate listing by name, total votes and percentage based on condition of location message
    for row in sorted (listing, reverse=True):
        percent = int(row) / votes
        if outloc == "terminal":
            print(f"{listing[row]}:  " + "{:.3%}".format(percent) + f"  ({row})")
        elif outloc == "export":
            outfile.write(f"{listing[row]}:  " + "{:.3%}".format(percent) + f"  ({row}) \n")
        
        # Assign the winner to the candidate in the first iteration for having the highest votes 
        # and then change the flag status to disable reassigning another candidate
        if flag is True:
            winner = listing[row]
            flag = False

    # Output the winner based on condition of location message
    if outloc == "terminal":
        print("-"*40)
        print(f"Winner: {winner}")
        print("-"*40)
    elif outloc == "export":
        outfile.write("-"*40 + "\n")
        outfile.write(f"Winner: {winner} \n")
        outfile.write("-"*40 + "\n")

# Output the results to the textfile
# Call the summary function to export candidate detail and winner to file
with open(file_path_result, 'w') as textfile:
    textfile.write("Election Results \n")
    textfile.write("-"*40 + "\n")
    textfile.write(f"Total Votes: {vote_total} \n") 
    textfile.write("-"*40 + "\n")
    print_summary(vote_name, vote_total, textfile, "export")

# Output the results to the terminal
# Call the summary function to print candidate detail and winner to terminal
print("\n")
print("Election Results")
print("-"*40)
print(f"Total Votes: {vote_total}") 
print("-"*40)
print_summary(vote_name, vote_total, textfile, "terminal")

# Close the result file
textfile.close()