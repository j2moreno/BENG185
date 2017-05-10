import sys
from Bio import SeqIO
import gzip

filename = sys.argv[1] #reads the compressed gz genBank file
decompressedFile = gzip.open(filename,'rb')#opens the gz file for reading

record = SeqIO.read(decompressedFile, "genbank") #reads the file
arrayToPrint = [] #holds all the info to print

#iterates through each geature extracting information
for feature in record.features:
    if feature.type == 'source': #gets source of file
          tax_id = feature.qualifiers.get('db_xref')[0][6:] #gets tax_id


arrayToPrint.append(1)#appends genome_id
arrayToPrint.append(record.description) #appends name of organism 
arrayToPrint.append( int(tax_id)) #appends tax_id
arrayToPrint.append( record.annotations['taxonomy'][0].lower())#domain of the organism 
arrayToPrint.append(1)#num of replicons
arrayToPrint.append(2)#num of genes
arrayToPrint.append(int(record.annotations['contig'][17:-1]))#size in bps
arrayToPrint.append('GCF_000005845.2')#

#print contents of array 
print '\t'.join(str(x) for x in arrayToPrint)
arrayToPrint = []

filename2 = sys.argv[2] #reads the 2nd compressed gz genBank file
decompressedFile2 = gzip.open(filename2,'rb')#opens the gz file for reading

arrayToPrint2 = [] #holds all the info to print

length = 0

#Since there are mutiple records in this genome we have to iterate through it
for record2 in SeqIO.parse(decompressedFile2, "genbank"): #reads the fil
  arrayToPrint2 = [] #holds all the info to print
  for feature in record2.features:
    if feature.type == 'source': #gets source of file                           
      tax_id = feature.qualifiers.get('db_xref')[0][6:] #gets tax_id        
  length += int(record2.annotations['contig'][19:-1])
  
  
#appends the same info as above but for a different genome
arrayToPrint2.append(2)
arrayToPrint2.append(record2.description) 
arrayToPrint2.append( int(tax_id))
arrayToPrint2.append( record2.annotations['taxonomy'][0].lower())
arrayToPrint2.append(4) 
arrayToPrint2.append(4)
arrayToPrint2.append(length)
arrayToPrint2.append('GCF_000576515.1')


#print contents of array 
print '\t'.join(str(x) for x in arrayToPrint2)

