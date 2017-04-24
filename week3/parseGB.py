import sys
from Bio import SeqIO
import gzip

filename = sys.argv[1] #reads the compressed gz file

decompressedFile = gzip.open(filename,'rb')#opens the gz file for reading


record = SeqIO.read(decompressedFile, "genbank") #reads the file
for feature in record.features:
	arrayToPrint = []#holds all the info to print

	if feature.type == 'source': #gets source of file
		tax_id = feature.qualifiers.get('db_xref')[0][6:] #gets tax_id

	if feature.type == 'CDS': #only interested in CDS types

		stringToParse = str(feature.location) 
		element = stringToParse.split('(')
		coordinates = element[0] #gets coordinates 
		strand = element[1][0] #gets whether gene is on the forward or reverse strand 
		
		#if protein id doesn't exisit it is a psuedo gene
		if feature.qualifiers.get('protein_id') == None: 
			protein_id = 'PSUEDO'

		else:
			protein_id = feature.qualifiers.get('protein_id')[0]

		#if no EC number but a dash 
		if feature.qualifiers.get('EC_number') == None:
			EC_number = '-'
		else:
			EC_number = feature.qualifiers.get('EC_number')[0]

		#gets external information
		external = feature.qualifiers.get('db_xref')

		#appends all these elements into array to print
		arrayToPrint.append(protein_id)
		arrayToPrint.append(coordinates)
		arrayToPrint.append(strand)
		arrayToPrint.append(feature.qualifiers.get('gene')[0])
		arrayToPrint.append(feature.qualifiers.get('locus_tag')[0])
		arrayToPrint.append(feature.qualifiers.get('gene_synonym'))
		arrayToPrint.append(feature.qualifiers.get('product'))
		arrayToPrint.append(tax_id)
		arrayToPrint.append(EC_number)
		arrayToPrint.append(external)
		
		#print contents of array 
		print '\t'.join(str(x) for x in arrayToPrint)


