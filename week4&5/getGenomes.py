import os

#script that gets 3 randomly chosen genome from the uniprot database
#outputs genomes into separated directories


os.system('wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/README')
os.system('wget -P genome1 ftp://ftp.uniprot.org:21/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Bacteria/UP000000212_*')
os.system('wget -P genome2 ftp://ftp.uniprot.org:21/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Bacteria/UP000000214_*')
os.system('wget -P genome3 ftp://ftp.uniprot.org:21/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Bacteria/UP000000223_*')
#os.system('wget ftp://ftp.uniprot.org:21/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Bacteria/UP000000212_1234_*')


