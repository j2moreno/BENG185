import sys
import bz2

filename = sys.argv[1]



bz_file = bz2.BZ2File(filename)
data = bz_file.readlines()

#data = file.readlines()

i = 0
array = []
dictProtein = dict()
for element in data:

	element = element.replace('\n', '')
	element = element.split('\t')
	
	
	if element[0] in dictProtein.keys():
		dictProtein[element[0]].append((element[1], element[3]))
	else:
		dictProtein[element[0]] = [(element[1], element[3])]

	if len(dictProtein) > 2000:
		break


for values in dictProtein.values():
	sorted(values, key=lambda x: x[1])

for key, values in dictProtein.items():
	print key + '\t' + values[len(values)-1][0] + '\t' + values[len(values)-1][1] + '\t'

max = 0
protein = ''
protein2 = ''
for key in dictProtein.keys():
	if len(dictProtein[key]) > max:
		protein = key

		max = len(dictProtein[key])

print protein,dictProtein[protein][len(dictProtein[protein])-1], max 
