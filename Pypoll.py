#data we need to retreive
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)
import os
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

## Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:


#write title
    txt_file.write("Counties in the Election\n---------------------\nArapahoe\nDenver\nJefferson")   

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print each row in the CSV file.
    for row in file_reader:
        print(row)
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print each row in the CSV file.
    for row in file_reader:
        print(row)
############## Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1 Initialize total vote counter
total_votes = 0

# declare new list for options and votes
candidate_options = []

#get candidates name from row in for loop/print name from each row
        #remove candidate_name = row[2]

#to put condidates with votes declare empty dict
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

     # print each row in the new csv file
    for row in file_reader:
        #2 Add to the total votes
        total_votes += 1

        # 3remove Print the total votes remove print(total_votes), instead print candidate name from each row
        candidate_name = row[2]

        # if candidate doesnt match any existing candidate...
        if candidate_name not in candidate_options:
            # then add candidate name to candidate list
            candidate_options.append(candidate_name)

            #2 then track that candidates vote count and set to 0
            candidate_votes[candidate_name] = 0

        #now add a vote to that candidate count(move this over to be in above for loop)
        candidate_votes[candidate_name] += 1
# now get %votes by looping thru count
# iterate through candidate list with a for loop
for candidate_name in candidate_votes:
    #retrieve can's vote count
    votes = candidate_votes[candidate_name]
    #calc %votes
    vote_percentage = float(votes) / float(total_votes) * 100
    #to do print winning cand, votes, % to terminal

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #print can name and %votes need to add vote count to terminal
    #need winning vote count and cand
    #need if vote >winning count using if and
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if T set winning_count = votes and winning_% =vote_percent
        winning_count = votes
        winning_percentage = vote_percentage
        #winning_candidate = cand_name
        winning_candidate = candidate_name
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
    

#print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


        
    
    # print the candidate list: removeprint(candidate_options)
    # then print candidate vote in dict remove print(candidate_votes)
    #add f string for percent
    # change print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")



#1 total # votes cast
#2 complete list of candidates who received votes
#3 % votes each candidate won
#4 total # votes each candidtae won
#5 the winner of the election based on popular votes

####### Import the datetime class from the datetime module. import datetime
# Use the now() attribute on the datetime class to get the present time. now = datetime.datetime.now()
# Print the present time. print("The time right now is ", now)


