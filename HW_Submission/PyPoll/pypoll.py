# Modules
import csv

# Set path for file
csvpath = "Resources/election_data.csv"

# Variable
vote_count = 0
candidate_dict = {}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # loop the CSV
    for row in csvreader:
    

        # count votes
        vote_count += 1

        #add to candidate dictionary
        row_candidate = row[2]
        if row_candidate in candidate_dict.keys():
            candidate_dict[row_candidate] += 1
        else:
            candidate_dict[row_candidate] = 1



print(vote_count)
print(candidate_dict)

# create our output

output = f"""Election Results
-----------------------------
Total Votes: {vote_count}
-----------------------------\n"""

max_candidate = ""
max_votes = 0

for candidate in candidate_dict.keys():
    # get votes
    votes = candidate_dict[candidate]
    perc = 100 * (votes / vote_count)

    line = f"{candidate}: {round(perc, 3)}% ({votes})\n"
    output += line

    if votes > max_votes:
        max_candidate = candidate
        max_votes = votes

last_line = f"""---------------------
Winner: {max_candidate}
-------------------------"""

output += last_line

print(output)

with(open("pypoll_output_sarkis.txt", 'w') as f):
    f.write(output)
