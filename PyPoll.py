import csv
import os

#os.listdir()
#path = "/Users/rubyjiang/Desktop/Analysis Projects"
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")
open(file_to_save, "w")

total_votes = 0
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
  

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes +=1
print(total_votes)

 # Print the candidate name from each row.
#candidate_name = row[2]

        