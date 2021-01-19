# Import modules
import os
import csv


# Set path
csvpath = os.path.join(".","Resources","election_data.csv")

# Initialize and define variables we will need
total_votes = 0 #variable to count the total number of votes
candidates = [] #listo to save the column of candidates
kvotes = 0 #variable to store Khan votes
cvotes = 0 #variable to store Correy votes
ovotes = 0 #variable to store O'Tooley votes
lvotes = 0 #variable to store Li votes

# Open the csv file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    # Loop to calculate total number of votes, total votes for each candidate and save candidates column
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


ls_cand = list(set(candidates)) # List of the candidates who received votes
w_name = ["O'Tooley" , "Correy", "Khan", "Li"] # List with the names of the candidates
w_votes = [ovotes, cvotes, kvotes, lvotes] # List with the total votes for each candidates
opercentage = "{:.3f}".format((ovotes/total_votes)*100) # Calculate O'Tolley percentage and adding format
kpercentage = "{:.3f}".format((kvotes/total_votes)*100) # Calculate Kahn percentage and adding format
lpercentage = "{:.3f}".format((lvotes/total_votes)*100) # Calculate Li percentage and adding format
cpercentage = "{:.3f}".format((cvotes/total_votes)*100) # Calculate Correy percentage and adding format
winner = max(w_votes) #Identify the winner by votes
i_winner = w_votes.index(winner) #Getting the index of the winner to get it's name

# Print results in terminal
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
    
