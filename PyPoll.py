import csv
import os

#os.listdir()
path = "/Users/rubyjiang/Desktop/Analysis Projects/Election_Analysis"
file_to_load = os.path.join(path,"Resources","election_results.csv")
file_to_save = os.path.join(path,"analysis","election_analysis.txt")
open(file_to_save, "w")

candidate_votes = {}

candidate_options = []

total_votes = 0

winning_candidate = ""

winning_count = 0

winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
  

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
# 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
  # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
  # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
# Print the candidate list.
#print(candidate_options)
# Print the candidate vote dictionary.
#print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    # Winning Candidate and Winning Count Tracker
       # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)    
    #  Save the candidate results to our text file.
        txt_file.write(candidate_results)    
    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)    
#To do: print out the winning candidate, vote count and percentage to terminal.
   # votes to the terminal.
 # Save the winning candidate's results to the text file.
txt_file.write(winning_candidate_summary)

 