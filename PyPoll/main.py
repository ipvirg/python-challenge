# PyPoll Challenge
# Module for OS
import os

# Module for subprocess/terminal output
# import subprocess
# with open("output.txt", "w+") as output:
#    subprocess.call(["python", "./main.py"], stdout=output)

# Module for reading CSV file
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    #print(csvreader)

    #for row in csvreader:
    #    print(row)

# The total number of votes cast
    voter_id = []
    county_name = []
    candidate_name = []
    total_votes = 0 
    
    for row in csvreader:
        candidate_name.append(row[2])
        total_votes +=  1

    # print(candidate_name)

    khan_total = 0
    correy_total = 0
    li_total = 0
    otooley_total = 0
    for x in candidate_name:
        if x == "Khan":
            khan_total += 1
        
        elif x == "Correy":
            correy_total += 1 

        elif x == "Li":
            li_total += 1
        elif x == "O'Tooley": 
            otooley_total += 1

    print(str(khan_total))
    print(str(correy_total))
    print(str(li_total))
    print(str(otooley_total))

    khan_vote_percentage = round((khan_total/(total_votes - 1)), 3) 
    correy_vote_percentage = round((correy_total/(total_votes -1)), 3)
    li_vote_percentage = round((li_total/(total_votes -1)), 3)
    otooley_vote_percentage = round((otooley_total/(total_votes -1)), 3)

    candidate_vote_count_list = [(khan_total), (correy_total), (li_total), (otooley_total)]
    winner_candidate = max(candidate_vote_count_list)
    
    print(winner_candidate)
    print(candidate_vote_count_list)

    print(str(khan_vote_percentage))

    #print(str(total_votes - 1))

# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won

# print(candidate_name)


# The winner of the election based on popular vote.


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes - 1))
print("-------------------------")
print("Khan: " + "{:.3%}".format(khan_vote_percentage) + " (" + str(khan_total) + ")")
print("Correy: " + "{:.3%}".format(correy_vote_percentage) + " (" + str(correy_total) + ")")
print("Li: " + "{:.3%}".format(li_vote_percentage) + " (" + str(li_total) + ")")
print("O'Tooley: " + "{:.3%}".format(otooley_vote_percentage) + " (" + str(otooley_total) + ")") 
print("-------------------------")
print("Winner: ")
print("-------------------------")


#  Election Results
#  -------------------------
# Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
# Winner: Khan
#  -------------------------

