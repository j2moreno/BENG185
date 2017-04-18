import sys 
import collections

filename = sys.argv[1] # reads the codonCounts.txt file
file = open(filename, 'r')
data = file.readlines()
del data[0] # deletes header form list data

array = [] #array holding everyline 
tags = [] #holds all gene tags
dictionary = dict()# holds tags as keys and its values are the individual codon counts for that gene

for element in data:
	element = element.replace('\n', '')
	element = element.split('\t')

	#ignores the gene that is wasn't divisble by 3
	if element[0] == 'b2891':
		continue
	array.append(element)
	tags.append(element[0])
	dictionary[element[0]] = element[1:-1]

del tags[len(tags)-1] #deletes total only interested in tags
totalCodonsInGenome = array[len(array)-1][65] #overall total number of codons in genome
totalForEachCodon = array[len(array)-1][1:65] #overall total numbers for each codon

dictionary = collections.OrderedDict(sorted(dictionary.items()))
del dictionary['Total']

lengthsOfEachGene = [] #holds the lengths of every single gene
for element in array:
	lengthsOfEachGene.append(element[65]) 

del lengthsOfEachGene[-1]# deletes last one since it is not needed

#Calulates CUI for each gene
for i in range(len(tags)):
	j = 0
	sum = 0

	for value in dictionary[tags[i]]:
		
		# number of codons in gene / gene length
		Q = float(value)/float(lengthsOfEachGene[i]) 

		#total of specific codon in genome / overall total of every codon in genome
		P = float(totalForEachCodon[j])/float(totalCodonsInGenome)
		j+=1
		temp = Q*P
		sum += temp #CUI

	#prints gene with its respective CUI 
	print tags[i] + '\t' + str(sum)








