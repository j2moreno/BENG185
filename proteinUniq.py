'''
Problem: 

For the first 2000 different reference proteins in column 1,
extract all their inferred binding partners (column 2), and 
report for each reference protein a) the candidate binding 
partner with the highest probability of interaction, and b) 
the total number of candidate binding partners for that 
reference protein.
'''

import sys
import bz2

#takes a bz2 file to read
filename = sys.argv[1]
bz_file = bz2.BZ2File(filename)
data = bz_file.readlines()

i = 0
array = []
dictProtein = dict()

#for loop that gets the 1st 2000 unique proteins in the file
for element in data:

	element = element.replace('\n', '')
	element = element.split('\t')
	
	if element[0] in dictProtein.keys():
		dictProtein[element[0]].append((element[1], element[3]))
	else:
		dictProtein[element[0]] = [(element[1], element[3])]

	if len(dictProtein) > 2000:
		break

#sorts the 2000 unique proteins by highest probable interaction
for values in dictProtein.values():
	sorted(values, key=lambda x: x[1])

#print the most probable protein-protein interaction 
#along with its probablitity 
for key, values in dictProtein.items():
	print key + '\t' + values[len(values)-1][0] + '\t' + values[len(values)-1][1] + '\t'


max = 0
protein = ''
protein2 = ''

#Gets the protein with the highest number
#of protein to protein interactions
for key in dictProtein.keys():
	if len(dictProtein[key]) > max:
		protein = key

		max = len(dictProtein[key])

#prints the protein along with the number of proteins it interacts with
print protein,dictProtein[protein][len(dictProtein[protein])-1], max 
