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

for feature in record.features:
    if feature.type == 'source': #gets source of file
          name = feature.qualifiers.get('organism')[0]#name of organism 

structure = record.annotations['topology']

#append appropiate fields 
arrayToPrint.append(replicon_number)
arrayToPrint.append(genome_id)
arrayToPrint.append(name)
arrayToPrint.append('chromosome')
arrayToPrint.append(structure)
arrayToPrint.append(2)
arrayToPrint.append(int(record.annotations['contig'][17:-1]))   
arrayToPrint.append(record.annotations['accessions'][0])
arrayToPrint.append(record.annotations['date'])

print '\t'.join(str(x) for x in arrayToPrint)


filename2 = sys.argv[2] #reads the 2nd compressed genBank file
decompressedFile2 = gzip.open(filename2,'rb')#opens the gz file for reading
replicon_number = 2
genome_id = 2

for record2 in SeqIO.parse(decompressedFile2, "genbank"): #reads the file
  arrayToPrint2 = [] #holds all the info to print
  
  for feature in record2.features:

    if feature.type == 'source': #gets source of file
      name = feature.qualifiers.get('organism')[0]

      #used to get structure and type of gene
      if feature.qualifiers.get('chromosome') != None:
        structure = feature.qualifiers.get('chromosome')[0]
        replicon_type = 'chromosome'

      else:
        structure = 'circular'
        replicon_type = 'plasmid'

  accession = record2.id
  accession = accession.split('.')
  accession = accession[0]
  
  arrayToPrint2.append(replicon_number)
  arrayToPrint2.append(genome_id)
  arrayToPrint2.append(name)
  arrayToPrint2.append(replicon_type)
  arrayToPrint2.append(structure)
  arrayToPrint2.append(1)
  arrayToPrint2.append(len(record2.seq)) 
  arrayToPrint2.append(accession) 
  arrayToPrint2.append(record.annotations['date'])   

  print '\t'.join(str(x) for x in arrayToPrint2)
  replicon_number += 1
