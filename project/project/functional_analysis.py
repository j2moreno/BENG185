import sys
import MySQLdb

#connects to SQL databse
db = MySQLdb.connect(host="bm185s-mysql.ucsd.edu",user="j2moreno", passwd="Azsxdcf1", db="j2moreno_db")  

#creates cursor object
cursor = db.cursor()

cursor.execute('SELECT regulation,symbol FROM HIV_2_expression')
#cursor.execute('SELECT regulation,symbol FROM HIV_1_expression')
rows = cursor.fetchall()
upGenes = []
downGenes = []

for i in range(len(rows)):
  if rows[i][0] == 'up':
    upGenes.append(rows[i][1])

  elif rows[i][0] == 'down':
    downGenes.append(rows[i][1])

  else: 
    continue


upTerms = []
upOntology = []
for element in upGenes:
  
  sqlCall = 'SELECT Onto,Term,Fold,pvalue,fdr,enrich FROM HIV_2_functions WHERE genes LIKE %s'
  args=[element+'%']
  cursor.execute(sqlCall,args)
  row = cursor.fetchone()
  if row == None:
    continue
  if row[0] != None or row[0] !='Ontology':
    upOntology.append(row[0])
    upTerms.append(row[1])


downTerms = []
downOnto = []

for element in downGenes:

  sqlCall = 'SELECT Onto,Term,Fold,pvalue,fdr,enrich FROM HIV_2_functions WHERE genes LIKE %s'  
  args=[element+'%']       
  cursor.execute(sqlCall,args)
  row = cursor.fetchone()
  
  if row == None:
    continue
  if row[0] != None or row[0] != 'Ontology':
    downOnto.append(row[0])
    downTerms.append(row[1])

print 'Upregulated Ontology'
print '\n'.join(upOntology)

'''
print 'Downregulated Ontology'
print '\n'.join(downOnto)
'''

