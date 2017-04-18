import os

#begins at the given directory 
rootdir = 'dirtree/' 

#gets all file names within the rootdir 
array =  next(os.walk(rootdir))[1]

i = 0
#recursively go through all files and get only .tbl files
for subdir, dirs, files in os.walk(rootdir):
       for file in files:
                 if file.endswith(".tbl"):

                                openedfile = open(os.path.join(subdir, file), 'r')
                                #keeps reading line until it gets to approipiate column
                                data = openedfile.readline()
                                data2 = openedfile.readline()
                                data3 = openedfile.readline()
                                
                                #prints name of file and its value
                                print array[i] + '\t' +  data3.split('\t')[3]
                                i +=1
                                break

