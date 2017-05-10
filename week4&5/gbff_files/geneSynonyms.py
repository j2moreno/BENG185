import sys
from Bio import SeqIO
import gzip

#genome 2 didnt have syonyms so i didnt include it 

filename = sys.argv[1] #reads the compressed gz file
decompressedFile = gzip.open(filename,'rb')#opens the gz file for reading

short_name = 'E_coli_K12_MG1655'
record = SeqIO.read(decompressedFile, "genbank") #reads the file
arrayToPrint = [] #holds all the info to print
gene_id = 1

for feature in record.features:   
  if feature.type == 'gene': #gets source of file
  
    #gets the synonyms
    synonym = feature.qualifiers.get('gene_synonym')[0]
    arrayToPrint.append(gene_id)
    arrayToPrint.append(synonym)

    print '\t'.join(str(x) for x in arrayToPrint)
    arrayToPrint = []
    gene_id += 1
'''
filename2 = sys.argv[2] #reads the compressed gz file
decompressedFile2 = gzip.open(filename2,'rb')#opens the gz file for reading
replicon_number = 1
genome_id = 2

for record2 in SeqIO.parse(decompressedFile2, "genbank"): #reads the file
  arrayToPrint2 = [] #holds all the info to print
  for feature in record2.features:
    if feature.type == 'gene': #gets source of file
      try:
        gene_id = feature.qualifiers.get('db_xref')[1]
        gene_id = gene_id.split(':')
        gene_id = gene_id[1] 

      except TypeError:
        gene_id = '-'
      try:

        synonym = feature.qualifiers.get('gene_synonym')[0] 
      except TypeError:
        synonym = '-'
      arrayToPrint2.append(gene_id) 
      arrayToPrint2.append(synonym)
      
      print '\t'.join(str(x) for x in arrayToPrint2)                               

      arrayToPrint2 = []
'''      
      #name = feature.qualifiers.get('organism')[0]
