import os
import gzip 
from Bio import SwissProt

#Using bipython libararies, downloads genome
os.system('wget -P Archaea ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/taxonomic_divisions/uniprot_sprot_archaea.dat.gz')

#opens the zipped genome file
handle = gzip.open('Archaea/uniprot_sprot_archaea.dat.gz', 'rt')

organism = []

#prints taxonomy, organism name, and classification
for record in SwissProt.parse(handle):
  
  print record.taxonomy_id[0] + '\t' + record.organism + '\t' +  record.organism_classification[0]
  
  




