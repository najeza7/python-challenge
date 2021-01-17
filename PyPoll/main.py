# Import modules
import os
import csv


# Set path
csvpath = os.path.join(".","Resources","election_data.csv")

total_votes = 0
candidates = []
kvotes = 0
cvotes = 0
ovotes = 0
lvotes = 0

# Open the cvs file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        total_votes +=1
        candidates.append(row[2])
        if row[2] == "O'Tooley":
            ovotes +=1
        elif row[2] == "Correy":
            cvotes += 1
        elif row[2] == "Khan":
            kvotes += 1
        else:
            lvotes += 1

w_name = ["O'Tooley" , "Correy", "Khan", "Li"] 
w_votes = [ovotes, cvotes, kvotes, lvotes]
ls_cand = list(set(candidates))
total_votes = ovotes + cvotes + kvotes + lvotes
opercentage = (ovotes/total_votes)*100
kpercentage = (kvotes/total_votes)*100
lpercentage = (lvotes/total_votes)*100
cpercentage = (cvotes/total_votes)*100
winner = max(w_votes)
i_winner = w_votes.index(winner)


print ("Election Results")
print ("-------------------------")
print (f"Total Votes: {total_votes}")
print ("-------------------------")
print(f"Khan: {kpercentage}% ({kvotes})")
print(f"Correy: {cpercentage}% ({cvotes})")
print(f"Li: {lpercentage}% ({lvotes})")
print(f"O'Tooley: {opercentage}% ({ovotes})")
print ("-------------------------")
print (f"Winner: {w_name[i_winner]} ")
print ("-------------------------")

# Specify the path for the new file
output_path = os.path.join(".", "analysis", "analysis_pypoll.txt")

# Write into the new text file
with open (output_path, "w") as txt_file:
    print ("Election Results", file = txt_file)
    print ("-------------------------", file = txt_file)
    print (f"Total Votes: {total_votes}", file = txt_file)
    print ("-------------------------", file = txt_file)
    print(f"Khan: {kpercentage}% ({kvotes})", file = txt_file)
    print(f"Correy: {cpercentage}% ({cvotes})", file = txt_file)
    print(f"Li: {lpercentage}% ({lvotes})", file = txt_file)
    print(f"O'Tooley: {opercentage}% ({ovotes})", file = txt_file)
    print ("-------------------------", file = txt_file)
    print (f"Winner: {w_name[i_winner]} ", file = txt_file)
    print ("-------------------------", file = txt_file)

    