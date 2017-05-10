import sys
from Bio import SeqIO
import gzip
import os

filename = sys.argv[1] #reads the compressed genBank file
decompressedFile = gzip.open(filename,'rb')#opens the gz file for reading

replicon_number = 1
genome_id = 1
record = SeqIO.read(decompressedFile, "genbank") #reads the file
arrayToPrint = [] #holds all the info to print
gene_id = 1


for feature in record.features:
  if feature.type == 'CDS':
    externArray = feature.qualifiers.get('db_xref')

    #determine whether a gene has a protein id or is a psuedo gene
    try: 
      protein_id = feature.qualifiers.get('protein_id')[0]
    except TypeError:
      protein_id = 'psuedo'
    
    #append protein id to print 
    protein_id = 'protein_id:' + protein_id
    externArray.append(protein_id)

    #prints all extenrnal references line by line
    for element in externArray:
      element = element.split(':')
      toAdd = element[0]
      toAdd2 = element[1]
      arrayToPrint.append(gene_id)
      arrayToPrint.append(toAdd)
      arrayToPrint.append(toAdd2)
      print '\t'.join(str(x) for x in arrayToPrint)
      arrayToPrint = []
    gene_id += 1


filename = sys.argv[2] #reads the compressed gz file                            
decompressedFile2 = gzip.open(filename,'rb')#opens the gz file for reading       
replicon_number = 1                                                           
genome_id = 1                                                                                 
arrayToPrint = [] #holds all the info to print          

gene_id = 1                                                                     

for record in SeqIO.parse(decompressedFile2, "genbank"):
  for feature in record.features:  

    #gets externeal references                                                
    if feature.type == 'source':
      externArray = feature.qualifiers.get('db_xref')  
    if feature.type == 'CDS':

      #determine whether a gene has a protein id or is a psuedo gene
      try:
        protein_id = feature.qualifiers.get('protein_id')[0]
      except TypeError:
        protein_id = 'psuedo'

      #append protein id to print 
      protein_id = 'protein_id:' + protein_id
      externArray.append(protein_id)

      #prints all extenrnal references line by line
      for element in externArray:
        element = element.split(':')
        toAdd = element[0]
        toAdd2 = element[1]
        arrayToPrint.append(gene_id)
        arrayToPrint.append(toAdd)
        arrayToPrint.append(toAdd2)
        print '\t'.join(str(x) for x in arrayToPrint)
        arrayToPrint = []
    
  gene_id += 1


