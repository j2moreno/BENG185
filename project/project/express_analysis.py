import sys
import MySQLdb

#connects to SQL databse
db = MySQLdb.connect(host="bm185s-mysql.ucsd.edu",user="j2moreno", passwd="Azsxdcf1", db="j2moreno_db")  

#creates cursor object
cursor = db.cursor()

#HIV_2
cursor.execute('SELECT regulation, test_raw, control_raw,test_normal,control_normal,symbol,GO FROM HIV_2_expression')

#HIV_1
#cursor.execute('SELECT regulation, test_raw, control_raw,test_normal,control_normal,symbol,GO FROM HIV_1_expression')

#gets number of rows in E coli
#numRows = int(cursor.rowcount)

up_raw_test = []
up_raw_control = []
up_normal_test = []                                                             
up_normal_control = []   

down_raw_test = []
down_raw_control = []
down_normal_test = []
down_normal_control = []

rows = cursor.fetchall()
upGenes = []
downGenes = []


for i in range(len(rows)):  
  if i == 0:
    continue
  

  if rows[i][0] == 'up':
    up_raw_test.append(rows[i][1])
    up_raw_control.append(rows[i][2])
    up_normal_test.append(rows[i][3])
    up_normal_control.append(rows[i][4])
    upGenes.append(rows[i][5])

  elif rows[i][0] == 'down':
    down_raw_test.append(rows[i][1])
    down_raw_control.append(rows[i][2])
    down_normal_test.append(rows[i][3])
    down_normal_control.append(rows[i][4])
    downGenes.append(rows[i][5])
  else:
    continue



#print '\n'.join(upGenes)

#print 'raw_test' + '\t' + 'raw_control' + '\t' + 'normal_test' + '\t' + 'normal_control'

#for i in range(len(down_raw_test)):
  #print str(up_raw_test[i]) + '\t' + str(up_raw_control[i]) + '\t' + str(up_normal_test[i]) + '\t' + str(up_normal_control[i])
#  print str(down_raw_test[i]) + '\t' + str(down_raw_control[i]) + '\t' + str(down_normal_test[i]) + '\t' + str(down_normal_control[i])

 
