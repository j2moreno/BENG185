import sys
from Bio import SeqIO
import gzip
import os

filename = sys.argv[1] #reads the compressed genBank file
decompressedFile = gzip.open(filename,'rb')#opens the gz file for reading

record = SeqIO.read(decompressedFile, "genbank") #reads the file
arrayToPrint = [] #holds all the info to print
gene_id = 1

for feature in record.features:
  if feature.type == 'CDS': #gets source of file
    stringToParse = str(feature.location) 
    element = stringToParse.split('(')
    coordinates = element[0] #gets coordinates 
    strand = element[1][0]

    #determines on strand the gene is on 
    if strand == '+':
      strand = 'F'
    else: 
      strand = 'R'

    coordinates =  coordinates.split(':')
    
    #gets the left, right, and length information
    try:
      right = int(coordinates[1][:-1])
      left = int(coordinates[0][1:])  
      length = right - left
    except ValueError as e:
      length = 0
      left = 0
      right = 0

    #gets number of exons
    try:
      exon = feature.qualifiers.get('gene')[0]
    except TypeError:
      exon = feature.qualifiers.get('locus_tag')
    
    #appends apporipate 
    arrayToPrint.append(gene_id)
    arrayToPrint.append(exon)
    arrayToPrint.append(left)
    arrayToPrint.append(right)
    arrayToPrint.append(length)

    print '\t'.join(str(x) for x in arrayToPrint)
    arrayToPrint = []
    gene_id +=1

filename2 = sys.argv[2] #reads the 2nd compressed genBank file
decompressedFile2 = gzip.open(filename2,'rb')#opens the gz file for reading
replicon_number = 1
gene_id = 1

for record2 in SeqIO.parse(decompressedFile2, "genbank"): #reads the file
  arrayToPrint2 = [] #holds all the info to print

  for feature in record2.features:
    if feature.type == 'CDS': #gets source of file
      stringToParse = str(feature.location)
      element = stringToParse.split('(')       
      coordinates = element[0] #gets coordinates
      strand = element[1][0]

      if strand == '+':
        strand = 'F'
      else:
        strand = 'R'
      coordinates =  coordinates.split(':')   

      try: 
        right = int(coordinates[1][:-1])
        left = int(coordinates[0][1:]) 
        length = right - left
      except ValueError as e:
        length = 0 
        left = 0
        right = 0

      #appends apporiate fields
      arrayToPrint2.append(gene_id)
      arrayToPrint2.append(exon) 
      arrayToPrint2.append(left) 
      arrayToPrint2.append(right) 
      arrayToPrint2.append(length) 

      print '\t'.join(str(x) for x in arrayToPrint2)
      arrayToPrint2 = []      
      gene_id +=1
              
