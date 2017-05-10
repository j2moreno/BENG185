from __future__ import division
import sys

#script that adds the scov caluclation at the end of blasted genomes

filename = sys.argv[1] #sequence lengths and lengths separted file by tab
filename2 = sys.argv[2] #outputted blast .out file

file = open(filename, 'r')
data = file.read().splitlines()
array = []

#caluclates scov using first file
for element in data:
  element = element.split('\t')
  value = int(element[1])/int(element[0])
  array.append( round(value,2))

file = open(filename2, 'r')
data = file.read().splitlines()
array2 = []

#appends scov to the end of the 2nd file passed
for i in range(len(data)):
  print data[i] + '\t' + str(array[i])

