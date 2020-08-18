import os
import csv

file_path_source = os.path.join('resources', 'election_data.csv')
file_path_result = os.path.join('analysis', 'result.txt')

vote_total = 0 

with open(file_path_source, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')    
    header = next(csvreader)

    county = []
    candidate = []
    for row in csvreader:
        county.append(row[1])
        candidate.append(row[2])
        vote_total += 1

    candidate.sort()
    i = 0
    tally = 1
    vote_name = {}

    for row in candidate:
        if (i + 1) < vote_total:
            if candidate[i+1] != candidate[i]:
                vote_name[tally] = candidate[i]
                tally = 0
            i += 1
            tally += 1
        else:  
            vote_name[tally] = candidate[i]

print("", "\n")
print("Election Results")
print("-"*40)
print(f"Total Votes: {vote_total}") 
print("-"*40)

with open(file_path_result, 'w') as textfile:
    textfile.write("Election Results \n")
    textfile.write("-"*40 + "\n")
    textfile.write(f"Total Votes: {vote_total} \n") 
    textfile.write("-"*40 + "\n")

    flag = True
    for row in sorted (vote_name, reverse=True):
        percent = int(row) / vote_total
        print(f"{vote_name[row]}:  " + "{:.3%}".format(percent) + f"  ({row})")
        textfile.write(f"{vote_name[row]}:  " + "{:.3%}".format(percent) + f"  ({row}) \n")
        
        if flag == True:
            winner = vote_name[row]
            flag = False   

    print("-"*40)
    print(f"Winner: {winner}")
    print("-"*40)

    textfile.write("-"*40 + "\n")
    textfile.write(f"Winner: {winner} \n")
    textfile.write("-"*40 + "\n")

textfile.close()