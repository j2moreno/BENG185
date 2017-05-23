import sys
import MySQLdb

#access DB
db = MySQLdb.connect(host="bm185s-mysql.ucsd.edu",user="j2moreno", passwd="Azsxdcf1", db="j2moreno_db")

cursor = db.cursor()
curr = db.cursor()

#read in genes in operons file
filename = sys.argv[1]
file = open(filename, 'r')
data = file.readlines()
array = []

#reads in genes and their correspnding locus_tag names fiel
filename2 = sys.argv[2]                                                          
file2 = open(filename2,'r')                                                      
data2 = file2.readlines()                                                        
geneDict = dict()    


for element in data2:                                                            
  element = element.replace('\n', '')                                           
  element = element.split('\t')                                                 
  geneDict[element[0]] = element[1]   

for element in data:
  element = element.replace('\n', '')
  element = element.split(',')
  for i in range(len( element)):
    locus = geneDict[element[i]]
    element[i] = locus 

  array.append(element)

operonsCoor = []
distances = []

#gets positive control distances and stores them in distances
for i in range(len(array)):
  q = array[i]
  cursor.execute("""SELECT g.gene_id,e.left_position,e.right_position,g.strand FROM realGenes g JOIN exons e USING(gene_id) WHERE g.locus_tag IN %s ORDER BY  e.left_position ASC""", (q,))
  
  #cursor.execute('SELECT g.gene_id,e.left_position,e.right_position,g.strand FROM realGenes g JOIN exons e USING(gene_id) WHERE g.locus_tag IN (' + ','.join(map(str,array[0])) + ') ORDER BY e.left_position ASC')
  exons = cursor.fetchall()
  if len(exons) == 1:
    operonsCoor.append((exons[0][1],exons[0][2]))
    continue
  else:
    if len(exons) != 0:
      operonsCoor.append((exons[0][1],exons[len(exons)-1][2]))
    for i in range(1,len(exons)):
      left = exons[i][1]
      right = exons[i-1][2]
      dist = left - right + 1
      distances.append(str(dist))

#deletes some values that are outliers
operons = sorted(operonsCoor, key=lambda tup: tup[0])
for i in range(5):
  del operons[0]


operonDict = dict()
for i in range(len(operons)):
  operonDict[operons[i][0]] = operons[i][1]


#gets cooordinates of every gene in E.coli genome 
cursor.execute('SET @a=0')
cursor.execute('SELECT @a:=@a+1 as idx, g.gene_id,e.left_position,e.right_position,g.strand FROM realGenes g JOIN exons e USING(gene_id) WHERE g.genome_id=1 ORDER BY e.left_position ASC')
#lengthQ = len(cursor.fetchall())
rows = cursor.fetchall()

prevStrand = ''
rightOperon = 0
negDist = []


#calcualtes negative control distances and stores them in negDist
for i in range(len(rows)):
  left = rows[i][2]
  right = rows[i][3]
  currStrand = rows[i][4]
  
  if left in operonDict.keys():
    rightOperon = operonDict[int(left)]
    prevStrand = currStrand

  if right == rightOperon and currStrand == prevStrand:
    if rows[i+1][2] in operonDict.keys():
      tempLeft = rows[i+1][2]
      distance = tempLeft - rightOperon + 1
      negDist.append( str(distance))

#prints all the negative control distances
print '\n'.join(negDist)







#print '\n'.join(distances)
