import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

with open(pybank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)
    
    #Set variable values
    total_months = 0
    total_profit_losses = 0
    sum_profit_losses = 0
    greatest_increase = 0
    greatest_decrease = 999999999999999999999

    #Loop through data
    for row in csv_reader:
        #Calculate total months
        total_months = total_months + 1
        
        #Create variable for Profit/Losses column and calculate total
        profit_losses = row[1]
        total_profit_losses = total_profit_losses + int(profit_losses)

        #Calculate average profit/losses
        if total_months > 1:
            change = int(profit_losses) - int(last_profit_losses)

            sum_profit_losses = sum_profit_losses + change
            avg_profit_losses = sum_profit_losses / (total_months -1)
            
            #Find month with the greatest increase in profit
            if change > greatest_increase:
                    greatest_increase = change 
                    greatest_increase_month = row[0]

            #Find month with the greatest decrease in profit
            if change < greatest_decrease: 
                    greatest_decrease = change
                    greatest_decrease_month = row[0]
        
        #Record profit/losses to be referenced on next loop
        last_profit_losses = row[1]
    
    months = f"Total Months: {total_months}"
    total = f"Total: ${total_profit_losses}"
    avg_change = f"Average Change: ${round(avg_profit_losses,2)}"
    increase = f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})"
    decrease = f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})"
    print("Financial Analysis")
    print("----------------------------")
    print(months)
    print(total)
    print(avg_change)
    print(increase)
    print(decrease)

#Export to textfile
output_path = os.path.join("Analysis", "analysis.txt")

with open(output_path, 'w') as analysis: 

    analysis.write("Financial Analysis")  
    analysis.write("\n")
    analysis.write("----------------------------")  
    analysis.write("\n")
    lines = [months, total, avg_change, increase, decrease]

    for line in lines: 
         analysis.write(line)
         analysis.write("\n")