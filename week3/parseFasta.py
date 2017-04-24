import sys
from Bio import SeqIO
import gzip

filename = sys.argv[1] #reads the compressed gz file

decompressedFile = gzip.open(filename,'rb')#opens the gz file for reading

#reads the file and puts entries in a array format
record = list(SeqIO.parse(decompressedFile, "fasta"))

#for every entry in the fasta file print Accession and sequence separated by a tab
for element in record:
	print element.id + '\t' + element.seq