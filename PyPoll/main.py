import os
import csv

pypoll_csv = os.path.join("Resources", "election_data.csv")

with open(pypoll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csv_reader)
    
    #Set variable and dictionary values
    total_votes = 0
    candidates = {}
    most_votes = 0
    winner = ""

    #Loop through data
    for row in csv_reader:
        #Get total votes cast
        total_votes = total_votes + 1
        
        #Assign candidate column to variable
        candidate = row[2]

        #Add candidates as keys and tally votes for dictionary
        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        else:
            candidates[candidate] = 1
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    
    #Loop through dictionary to print each candidate and their vote total and percent total
    for candidate, votes in candidates.items():
        print(f"{candidate}: {round(((votes / total_votes) * 100),3)}% ({votes})")
       
       #Find candidate with highest vote count
        if votes > most_votes:
            most_votes = votes 
            winner = candidate
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

#Export to textfile
output_path = os.path.join("Analysis", "analysis.txt")

with open(output_path, 'w') as analysis:
    analysis.write("Election Results")
    analysis.write("\n")
    analysis.write("-------------------------")
    analysis.write("\n")
    analysis.write(f"Total Votes: {total_votes}")
    analysis.write("\n")
    analysis.write("-------------------------")
    analysis.write("\n")
    for candidate, votes in candidates.items():
        analysis.write(f"{candidate}: {round(((votes / total_votes) * 100),3)}% ({votes})")
        analysis.write("\n")
    analysis.write("-------------------------")
    analysis.write("\n")
    analysis.write(f"Winner: {winner}")
    analysis.write("\n")
    analysis.write("-------------------------")

    