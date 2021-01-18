# Import modules
import os
import csv


# Set path
csvpath = os.path.join(".","Resources","budget_data.csv")

# Initialize and define variables we will need
months = 0 #variable to store the total months
total = 0   #variable to store the sum of profit/losses
prof_loss = [] #list to save the profit/losses
month_ls = [] #list to save months 

# Open the csv file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader) #skip the header
    
    # Loop to calculate the total number of months, the sum of profit/losses and to convert the columns
    # into lists
    for row in csvreader:
        months += 1
        total += int(row[1])
        prof_loss.append(int(row[1])) 
        month_ls.append(row[0])
    
    # Calculate the change between months and save it in a list
    dif = [prof_loss[i+1]-prof_loss[i] for i in range(len(prof_loss)-1)]
    
    # Calculate the average change
    average = sum(dif)/len(dif) 

    # Erase the first month of the list
    month_dif = [month_ls[i+1] for i in range(len(month_ls)-1)]
    
    # Get the greatest increase in profits
    max_increase = max(dif)
    
    # Get the greatest decrease in profits
    max_decrease = min(dif)

    # Get the index where the greatest increase in profits is stored
    i_increase = dif.index(max_increase)
    
    # Get the index where the greatest decrease in profits is stored
    i_decrease = dif.index(max_decrease)

# Print results in terminal
print ("Financial Analysis")
print ("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${round(average,2)}")
print(f"Greatest Increase in Profits: {month_dif[i_increase]} (${max_increase})")
print(f"Greatest Decrease in Profits: {month_dif[i_decrease]} (${max_decrease})")


# Specify the path for the new file
output_path = os.path.join(".", "analysis", "analysis_pybank.txt")

# Write into the new text file
with open (output_path, "w") as txt_file:
    print ("Financial Analysis", file = txt_file)
    print ("----------------------------", file = txt_file)
    print(f"Total Months: {months}", file = txt_file)
    print(f"Total: ${total}", file = txt_file)
    print(f"Average Change: ${round(average,2)}", file = txt_file)
    print(f"Greatest Increase in Profits: {month_dif[i_increase]} (${max_increase})", file = txt_file)
    print(f"Greatest Decrease in Profits: {month_dif[i_decrease]} (${max_decrease})", file = txt_file)

