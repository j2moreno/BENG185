import sys
from Bio import SeqIO
import gzip
import os

#since the 2nd genome doesn't have a functions section i didn't include it

filename = sys.argv[1] #reads the compressed genBank file
decompressedFile = gzip.open(filename,'rb')#opens the gz file for reading

replicon_number = 1
genome_id = 1
record = SeqIO.read(decompressedFile, "genbank") #reads the file
arrayToPrint = [] #holds all the info to print

gene_id = 1
for feature in record.features:
  if feature.type == 'CDS':
     
 	#gets the function of the gene 
    try:
      function = feature.qualifiers.get('function')[0]
    except TypeError:
      function = '-'
    print str(gene_id) + '\t' + function
    
    gene_id +=1

