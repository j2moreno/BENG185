import os
rootdir = 'dirtree/'

#print [x[0] for x in os.walk(rootdir)]
array =  next(os.walk(rootdir))[1]

i = 0

for subdir, dirs, files in os.walk(rootdir):
       for file in files:
                 if file.endswith(".tbl"):
                                
                                openedfile = open(os.path.join(subdir, file), 'r')
                                data = openedfile.readline()
                                data2 = openedfile.readline()
                                data3 = openedfile.readline()
                                print array[i] + '\t' +  data3.split('\t')[3]
                                i +=1
                                break

