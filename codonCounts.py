import sys
from itertools import product
import collections

filename = sys.argv[1] # reads the extractGenes.txt file 
file = open(filename, 'r')
data = file.readlines()

genes = [] #contains all genes
tags = []# contains the names of the gene
tagGene = dict()#dictionary holding tag to gene
for element in data:
	element = element.replace('\n', '')
	element = element.split('\t')

	tags.append(element[0])
	tagGene[element[0]] = element[1]

tags.sort() #sorts all the tags
tagGene = collections.OrderedDict(sorted(tagGene.items())) #sorts based off key
for value in tagGene.values():
	genes.append(value) #get all genes in roder by tag 

result = dict() #dictionary holding tag as key and number of times it appears
dictionary = dict() #reuseabnle dictionary holding codon as key and how many times it appears in a given gene
overall = dict() #overall total number of times codons appears 
allCodons = [] #holds all codons
totalNumberCodons = 0 # holds overall number of codons in genome

#produces all 64 codons and adds them to their respestive dictionaries 
for codon in product('ATCG', repeat=3):
	codon = ''.join(codon)
	dictionary[codon] = 0
	overall[codon] = 0

#sorts dictionary 
dictionary = collections.OrderedDict(sorted(dictionary.items()))


#puts all the tags in result
for tag in tags:
	result[tag] = []

#sorts result 
result = collections.OrderedDict(sorted(result.items()))

#separates all genes into 3 and extracts number of codons in each 
for i in range(len(genes)):
	#if gene not divisible by 3 dont include 
	if len(genes[i]) % 3 != 0:
		continue

	gene = genes[i]
	tag = tags[i]

	#divides gene by 3 and adds count for each codon
	for j in range(0, len(gene), 3):
		kmer = gene[j:j+3] #gets codon
		dictionary[kmer]+= 1 
		overall[kmer] +=1
		totalNumberCodons +=1
		
	#append counts to the result dictionary 
	for key in dictionary.keys():
		result[tag].append(dictionary[key])

	#resets all values in reuseable dictionary to 0 
	dictionary = dictionary.fromkeys(dictionary, 0)

#adds codons to all codons array 
for key in dictionary.keys():
	allCodons.append(key)

#print header
print 'Gene' + '\t' + '\t'.join(str(x) for x in allCodons) + '\t' + 'Length'


number = 0

#print results 
for key in result.keys():
	print key + '\t' + '\t'.join(str(x) for x in result[key]) + '\t' + str(len(genes[number])/3)
	number += 1

total = [] #contains total counts for all codons for all genes
overall = collections.OrderedDict(sorted(overall.items()))
for key in overall.keys():
	total.append(overall[key])

#prints Total stats
print 'Total' + '\t' + '\t'.join(str(x) for x in total) + '\t' + str(totalNumberCodons)



	


	


