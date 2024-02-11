import os
import csv

election_csv = os.path.join('C:\\', 'Users', 'alexi', 'Desktop', 'python-challenge', 'PyPoll', 'Resources', 'election_data.csv')


#open csv file and read through rows
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    next(csvreader)
    data = list(csvreader)
    total_votes = len(data)

#create pyhton list() to return a list  
    candidates = list()
    counts = list()
    votes = list()
    percentage = list()

    for i in range (0,total_votes):
        candidate = data[i][2] #take data from "Candidate" section
        counts.append(candidate) #append = adds to list
        if candidate not in candidates: 
            candidates.append(candidate)
    candidate_count = len(candidates)

#find percentage of votes each candidate won + total number of votes
#votes count
    for j in range (0,candidate_count):
        candidate_name = candidates[j]
        votes.append(counts.count(candidate_name))

#percentage
        percent = votes[j] / total_votes
        percentage.append(percent)

#find the winner of the election
candidate_winner = votes.index(max(votes))    


print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for k in range (0,candidate_count): 
    print(f"{candidates[k]}: {percentage[k]:.3%} ({votes[k]})")
print("----------------------------")
print(f"Winner: {candidates[candidate_winner]}")
print("----------------------------")



#export a text file
file = open("PyPoll.txt", "w")
file.write("Election Results" + "\n")
file.write("----------------------------" + "\n")
file.write(f"Total Votes: {total_votes}" + "\n")
file.write("----------------------------" + "\n")
for k in range (0,candidate_count): 
    file.write(f"{candidates[k]}: {percentage[k]:.3%} ({votes[k]})" + "\n")
file.write("----------------------------" + "\n")
file.write(f"Winner: {candidates[candidate_winner]}" + "\n")
file.write("----------------------------" + "\n")
file.close()









