#Module 3 Challenge: PyPoll
#RyanJames Code Submission

#Environment: Activate PythonData

#Import the module:
import os
#Import the reading files:
import csv 

#Hard code the working directory:
#Creates a user friendly working directory regardless of operating system
csvpath=os.path.join('..','Resources','election_data.csv')

#Set variables in code
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_total_count = 0
winning_count_percentage = 0

#Open csvfile as "read me":
with open(csvpath,'r') as csvfile:
    #Create an iterable object that holds all of our csv data.
    csvreader = csv.reader(csvfile)
    print(csvreader)




   
    



