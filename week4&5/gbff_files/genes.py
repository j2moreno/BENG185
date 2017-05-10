import sys
from Bio import SeqIO
import gzip
import os

filename = sys.argv[1] #reads the compressed gz file
decompressedFile = gzip.open(filename,'rb')#opens the gz file for reading

replicon_number = 1
genome_id = 1
record = SeqIO.read(decompressedFile, "genbank") #reads the file
arrayToPrint = [] #holds all the info to print
gene_id = 1

for feature in record.features:
  if feature.type == 'CDS':
    stringToParse = str(feature.location) 
    element = stringToParse.split('(')
    coordinates = element[0] #gets coordinates 
    strand = element[1][0]
    
    #determines on which strand the gene is on
    if strand == '+':
      strand = 'F'

    else:
      strand = 'R'
    coordinates =  coordinates.split(':')
    
    try:
      length = int(coordinates[1][:-1]) - int(coordinates[0][1:])
    except ValueError as e:
      length = 0
   
    name = feature.qualifiers.get('gene')[0]
    locus = feature.qualifiers.get('locus_tag')[0]
    try:
      product = feature.qualifiers.get('product')[0]
    except TypeError:
      product = '-'
    
    #determines whether a gene has a protein id or wheteher it is a psuedo gene
    try:
       protein_id = feature.qualifiers.get('protein_id')[0]
    except TypeError:
      protein_id = 'psuedo'
  
 
    exons = 0
    #counts the number of exons
    for exon in feature.location.parts:
      exons += 1
    
    #append appropiate fields to print 
    arrayToPrint.append(gene_id)
    arrayToPrint.append(genome_id)  
    arrayToPrint.append(replicon_number)
    arrayToPrint.append(locus)  
    arrayToPrint.append(protein_id)
    arrayToPrint.append(name)  
    arrayToPrint.append(strand)  
    arrayToPrint.append(exons)  
    arrayToPrint.append(length)  
    arrayToPrint.append(product)  

    print '\t'.join(str(x) for x in arrayToPrint)
    arrayToPrint = []
    gene_id += 1
    

filename2 = sys.argv[2] #reads the 2nd compressed genBank file
decompressedFile2 = gzip.open(filename2,'rb')#opens the gz file for reading
replicon_number = 1
genome_id = 2



for record2 in SeqIO.parse(decompressedFile2, "genbank"): #reads the file
  arrayToPrint2 = [] #holds all the info to print
  for feature in record2.features:
    if feature.type == 'CDS': #gets source of file
       stringToParse = str(feature.location)
       element = stringToParse.split('(')       
       coordinates = element[0] #gets coordinates?  
       strand = element[1][0] 

       #determines which strand the gene is on
       if strand == '+':                                                           
         strand = 'F'                                                                                                                                               
       else:                                                                       
         strand = 'R' 
       coordinates =  coordinates.split(':')   

       try:                                                                        
         length = int(coordinates[1][:-1]) - int(coordinates[0][1:])               
       except ValueError as e:                                                     
         length = 0   
       
       name = '-'
       locus = feature.qualifiers.get('locus_tag')[0]
       product = feature.qualifiers.get('product') 
       
       
       #determines whether a gene has a protein id or wheteher it is a psuedo gene
       try: 
         protein_id = feature.qualifiers.get('protein_id')[0]
       except TypeError:
         protein_id = 'psuedo'
       
       #counts the number of exons
       exons = 0
       for exon in feature.location.parts:
         exons +=1

       #append appropiate fields to print 
       arrayToPrint2.append(gene_id)
       arrayToPrint2.append(genome_id)
       arrayToPrint2.append(replicon_number) 
       arrayToPrint2.append(locus)
       arrayToPrint2.append(protein_id)
       arrayToPrint2.append(locus) 
       arrayToPrint2.append(strand) 
       arrayToPrint2.append(exons) 
       arrayToPrint2.append(length) 
       arrayToPrint2.append(product[0]) 

       print '\t'.join(str(x) for x in arrayToPrint2)

       arrayToPrint2 = []
       gene_id +=1
        
  replicon_number+=1
#name = feature.qualifiers.get('organism')[0]
