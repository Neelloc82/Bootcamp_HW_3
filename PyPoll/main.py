import os

import csv

csvpath = os.path.join('election_data.csv')

votes = []
vote_candidates = []
candidates = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader, None)

    for row in csvreader:
        votes.append(row[0])
        vote_candidates.append(row[2])

total_votes = len(votes)

#print(total_votes)


for candidate in vote_candidates:
    if candidate not in candidates:
        candidates.append(candidate)

#print(candidates)

Khan_total = vote_candidates.count("Khan")
Correy_total = vote_candidates.count("Correy")
Li_total = vote_candidates.count("Li")
OTooley_total = vote_candidates.count("O'Tooley")

#for candidate in vote_candidates:
    #if row[2] == str'Khan'
        #Kahn_total = Khan_total + 1
    #elif row[2] == str("Correy")
        #Correy_total = Correy_total + 1
    #elif row[2] == str("Li")
        #Li_total = Li_total + 1
    #elif row[2] == str("O'Tooley")
       # OTooley_total = OTooley_total + 1

#print(Khan_total)
#print(Correy_total)
#print(Li_total)
#print(OTooley_total)

Khan_raw_percent = round(Khan_total / total_votes, 4)
Correy_raw_percent = round(Correy_total / total_votes, 4)
Li_raw_percent = round(Li_total / total_votes, 4)
OTooley_raw_percent = round(OTooley_total / total_votes, 4)

Khan_percent = ("{:.2%}".format(Khan_raw_percent))
Correy_percent = ("{:.2%}".format(Correy_raw_percent))
Li_percent = ("{:.2%}".format(Li_raw_percent))
OTooley_percent = ("{:.2%}".format(OTooley_raw_percent))

#print(Khan_percent)
#print(Correy_percent)
#print(Li_percent)
#print(OTooley_percent)

output_path = os.path.join('PyPoll_Output.csv')

with open(output_path, 'w') as writefile:
    writefile.writelines('Election Results\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Totl Votes: ' + str(total_votes) + '\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Khan: ' + str(Khan_total) + '  ' + str(Khan_percent) + '\n')
    writefile.writelines('Correy: ' + str(Correy_total) + '  ' + str(Correy_percent) + '\n')
    writefile.writelines('Li: ' + str(Li_total) + '  ' + str(Li_percent) + '\n')
    writefile.writelines("O'Tooley: " + str(OTooley_total) + '  ' + str(OTooley_percent) + '\n')    
    writefile.writelines('----------------------------' + '\n')   
    writefile.writelines("Winner: Khan" + '\n')
    
    

with open(output_path, 'r') as readfile:
    print(readfile.read())









