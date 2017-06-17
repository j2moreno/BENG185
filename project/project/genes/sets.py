import sys
import MySQLdb

#connects to SQL databse
db = MySQLdb.connect(host="bm185s-mysql.ucsd.edu",user="j2moreno", passwd="Azsxdcf1", db="j2moreno_db")  

#creates cursor object
cursor = db.cursor()
curr = db.cursor()
#HIV_2
cursor.execute('SELECT symbol FROM HIV_2_expression')

#HIV_1
curr.execute('SELECT symbol FROM HIV_1_expression')


rowsHIV_1 = curr.fetchall()
rowsHIV_2 = cursor.fetchall()

genesHIV_1 = []
genesHIV_2 = []


for i in range(len(rowsHIV_1)):
  if genesHIV_1.append(rowsHIV_1[i][0]) != '': 
    genesHIV_1.append(rowsHIV_1[i][0])

for i in range(len(rowsHIV_2)):
  if genesHIV_2.append(rowsHIV_2[i][0]) != '': 
    genesHIV_2.append(rowsHIV_2[i][0]) 


sharedGenes = list(set(genesHIV_1).intersection(genesHIV_2))
print '\n'.join(sharedGenes)

