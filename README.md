# python-challenge
    Data Visualization Module 3 Challenge 
        With this challenge, I have demonstrated my ability to import CSV files; read and write files;
        use variables, lists, and dictionaries; and loop through datasets and structures. 

        This challenge consists of two datasets, for which I have written two separate scripts. Details on both datasets are listed below: 

        PyBank 
            In the PyBank folder, my script is found in main.py. The output .txt can be found in the Analysis subfolder, file analysis.txt. 
            The contents of analysis.txt are copy and pasted here. 

                Financial Analysis
                ----------------------------
                Total Months: 86
                Total: $22564198
                Average Change: $-8311.11
                Greatest Increase in Profits: Aug-16 ($1862002)
                Greatest Decrease in Profits: Feb-14 ($-1825558)

        PyPoll
             In the PyPoll folder, my script is found in main.py. The output .txt can be found in the Analysis subfolder, file analysis.txt. 
             The contents of analysis.txt are copy and pasted here.

                Election Results
                -------------------------
                Total Votes: 369711
                -------------------------
                Charles Casper Stockham: 23.049% (85213)
                Diana DeGette: 73.812% (272892)
                Raymon Anthony Doane: 3.139% (11606)
                -------------------------
                Winner: Diana DeGette
                -------------------------

        Note: 
            I referenced the webpage https://www.pythontutorial.net/python-basics/python-write-text-file/ to learn how to write to a text file. 
            This website showed me I could set my print statements to strings and store them in a list so I could reduce the lines of code
            needed to write to .txt, as I did in PyBank/main.py.  
            Additionally, line 37 of PyPoll/main.py was written with assistance from ChatGPT. I was stuck on iterating through the dictionary
            and had ChatGPT explain the correct syntax. Line 37 and 38 included here for reference: 
                    for candidate, votes in candidates.items():
                        print(f"{candidate}: {round(((votes / total_votes) * 100),3)}% ({votes})")
