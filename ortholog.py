import sys
import MySQLdb


#connects to SQL databse
db = MySQLdb.connect(host="bm185s-mysql.ucsd.edu",user="j2moreno", passwd="Azsxdcf1", db="j2moreno_db")  

#creates cursor object
cursor = db.cursor()

#gets all the rows in the E_coli db
cursor.execute('SELECT * FROM blast_E_coli_1')

curr = db.cursor()

#gets number of rows in E coli
numRows = int(cursor.rowcount)

IDconnect = []
qseqid = set()
bitscore = []
dictionary = dict()

#iterate through all rows
for i in range(numRows):
 
  #gets the first row
  row = cursor.fetchone()

  #uses the query ID to find its best hit with the highest bitscore
  curr.execute("""SELECT * FROM blast_E_coli_1 WHERE qseqid=%s ORDER BY bitscore DESC""", (row[0],))
  
  #get that top hit 
  row1 = curr.fetchone()
  
  #dtermines if we have already gone through the same gene
  if row1[0] in qseqid:
    continue
  else:
    qseqid.add(row1[0])

  #appends a tuple with the query ID and the subject ID
  IDconnect.append((row1[0],row1[1]))

  #stores the best bitscores
  bitscore.append(int(row1[4]))

#goes through the second genome
secondCursor = db.cursor();
secondCursor.execute('SELECT * FROM blast_A_tum_1') 

curr = db.cursor()

numRows = int(secondCursor.rowcount)


for i in range(numRows):
  row = secondCursor.fetchone()    

  #uses the query ID to find its best hit with the highest bitscore                                                   
  curr.execute("""SELECT * FROM blast_A_tum_1 WHERE qseqid=%s ORDER BY bitscore DESC""", (row[0],))
  row1 = curr.fetchone()

  combin = (row1[1],row1[0])

  #determines if the coverage is > than 60%
  if float(row1[14]) > 0.6:

    #if the tuple already exists than we found an ortholog 
    if combin in IDconnect:
      print row1[1] + '\t' + row1[0] + '\t' + 'ortholog'
      IDconnect.remove(combin)

    #no ortholog found  
    else:
      continue



