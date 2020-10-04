import csv# Path to collect data from the Resources folderelection_data = '/Users/madhuvenkidusamy/Documents/Data Science Bootcamp/Homeworks/python-challenge/PyPoll/Resources/election_data.csv'candidate = []# Read in the CSV filewith open(election_data) as csvfile:    csvreader = csv.reader(csvfile)        next(csvreader) #this line skips the header        #read the columns of the csv as lists    for row in csvreader:        candidate.append(row[2])         total_votes = len(candidate)candidate_list = set(candidate) # see entire set of candidates who are running# gives number of votes each candidate gotvote_counts = []vote_counts.append(candidate.count('Correy')) # Correy vote sharevote_counts.append(candidate.count('Khan')) # Khan vote sharevote_counts.append(candidate.count('Li')) # Li vote sharevote_counts.append(candidate.count("O'Tooley")) # O'Tooley vote share# set vote counts and vote percents into a dictionarycounts = {'Khan': vote_counts[1], 'Correy': vote_counts[0], 'Li': vote_counts[2], "O'Tooley": vote_counts[3]}percent_counts = {'Khan': "{:.3%}".format(vote_counts[1]/total_votes), 'Correy': "{:.3%}".format(vote_counts[0]/total_votes), 'Li': "{:.3%}".format(vote_counts[2]/total_votes), "O'Tooley": "{:.3%}".format(vote_counts[3]/total_votes)}# gives winner of electionwinner = max(counts, key=counts.get)# print out resultsprint('\nElection Results\n--------------------------')print('Total Votes: ' + str(total_votes) + '\n--------------------------')print('Khan: ' + str(percent_counts['Khan']) + ' (' + str(counts['Khan']) + ')')print('Correy: ' + str(percent_counts['Correy']) + ' (' + str(counts['Correy']) + ')')print('Li: ' + str(percent_counts['Li']) + ' (' + str(counts['Li']) + ')')print("O'Tooley: " + str(percent_counts["O'Tooley"]) + ' (' + str(counts["O'Tooley"]) + ')')print('--------------------------\nWinner: ' + winner)print('--------------------------')# print results to text filef = open("/Users/madhuvenkidusamy/Documents/Data Science Bootcamp/Homeworks/python-challenge/PyPoll/analysis/analysis.txt", "x")f.write('\nElection Results\n--------------------------')f.write('Total Votes: ' + str(total_votes) + '\n--------------------------')f.write('Khan: ' + str(percent_counts['Khan']) + ' (' + str(counts['Khan']) + ')')f.write('Correy: ' + str(percent_counts['Correy']) + ' (' + str(counts['Correy']) + ')')f.write('Li: ' + str(percent_counts['Li']) + ' (' + str(counts['Li']) + ')')f.write("O'Tooley: " + str(percent_counts["O'Tooley"]) + ' (' + str(counts["O'Tooley"]) + ')')f.write('--------------------------\nWinner: ' + winner)f.write('--------------------------')f.close()