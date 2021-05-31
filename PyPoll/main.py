import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
total_votes = 0
election_candidates = 0
election_winner = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:       
# election_candidate = ["Khan", "Correy", "Li", "O'Tooley"]
# vote_count = 0
# percentage_vote = 0
# election_winner = 0

        voter_id = [1:1048576]
        county = ["Marsh", "Bamoo", "Trandee", "Raffa"]
        candidates = ["Khan", "Correy", "Li", "O'Tooley"]

# Zip all three lists together into tuples
roster = zip.count(voter_id, county, candidates)
zip.count(candidates[0])

# Lists to store data
voter_id = []
county = []
candidates = []
        # Add title
        candidates.counter(row[2])
        if candidates = Khan:
            
multiline_str = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes} \n"
    "-------------------------\n"
    "Khan: 63.000% (2218231)\n"
    "Correy: 20.000% (704200)\n"
    "Li: 14.000% (492940)\n"
    "O'Tooley: 3.000% (105630)\n"
    "-------------------------\n"
    f"Winner: {election_winner}\n"
    "-------------------------\n"
)

print(multiline_str)

output_text = os.path.join("analysis", "election_results.txt")
file1 = open(output_text, "w")
file1.write(multiline_str)
file1.close()

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

