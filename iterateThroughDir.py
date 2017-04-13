import os
rootdir = 'test/'

print os.walk(rootdir)
print [x[0] for x in os.walk(rootdir)]

for subdir, dirs, files in os.walk(rootdir):
     for file in files:
        if file.endswith(".tbl"):
             print(os.path.join(subdir, file))