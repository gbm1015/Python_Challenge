# Dependencies
import os
import csv

# Identify path to csv data file for loading
election_data = os.path.join("Resources","election_data.csv")

# Open election_data as csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    # Note that csv file has a header row
    header = next(csvreader)

    # Start Total Votes counter
    total_votes = 0

    # Identify counters for determining the candidates and their respective votes
    candidate_options = []
    candidate_votes = {}

    # Calculate total number of votes cast as well as the list of candidates and their associated votes
    for row in csvreader:
        # Add 1 to the Total Votes counter
        total_votes = total_votes + 1

        # Extract the candidate's name from each row
        candidate_name = row[2]

        # Loop through candidates' names and add a new candidate to the counter when discovering a new one who is not on the options' list
        if candidate_name not in candidate_options:
            # Add the candidate name to the list of candidates in the running options
            candidate_options.append(candidate_name)
            # Start tracking that candidate's associated votes' counter
            candidate_votes[candidate_name] = 0
        # Add 1 vote to the identified candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Identify path for output data to analysis folder
output_file = os.path.join("Analysis","election_analysis.txt")

#Open the output file
with open(output_file,"w") as election_analysis_file:
    writer = election_analysis_file.write
    output=(" \n"
            f"Election Results\n"
            " \n"
            "------------------------------\n"
            f"Total Votes: {total_votes}\n"
            " \n"
            "------------------------------\n")
    print(output)
    election_analysis_file.write(output)

    # Identify winning candidate and votes
    winning_candidate = ""
    winning_count = 0

    # Calculate the percentage of votes associated with each candidate, and identify the winning candidate
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = round(float(votes)/float(total_votes)*100,3)
        output=(f"{candidate}: {vote_percentage}% ({votes})\n"
            " \n")
        print(output)
        election_analysis_file.write(output)
  
        # Identify winning candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

    output=("------------------------------\n"
            " \n"
            f"Winner: {winning_candidate}\n"
            " \n"
            "------------------------------\n")
    print(output)        
    election_analysis_file.write(output)
    


 


