import sys

#function that returns the reverse compliment of the string given
def reverseComp(text):

  reverseStack = [] #holds the reverse compliment of the string in the form of a stack 

  for i in range(len(text)): # for every letter in text
    if text[i] == "A":
      reverseStack.append('T')
    elif text[i] == 'T':
      reverseStack.append('A')
    elif text[i] == 'C':
      reverseStack.append('G')
    elif text[i] == 'G':
      reverseStack.append('C')

  reverseComplement = []
  for i in range(len(reverseStack)):
    #pops from stack to get reverse compliement 
    reverseComplement.append(reverseStack.pop()) 

   #returns reverse compliement in the form of a string  
  return("".join(str(x) for x in reverseComplement))

#function that prints DNA sequence and continues the sequence
#every 70 nuclotides
def insert_newlines(string, every=70):
    lines = []
    
    for i in xrange(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)

filename = sys.argv[1] # argument 1 which is for the Protein Table
file = open(filename, 'r')

data = file.readlines()
start = [] # holds all start positions 
end = []# holds all end positions 
reverse = [] #holds whether the gene is on the forward or reverse strand
locus = [] #holds locus's 
tag = [] #holds the locus's tags
name = [] #holds the name of the gene


#appends the appropiate elements to each array
for element in data:
  element = element.replace('\n', '') #gets rid of newline character
  element = element.split('\t')# gets rid of tabs

  #the appending step for each 
  start.append(element[2])
  end.append(element[3])
  reverse.append(element[4])
  locus.append(element[6])
  tag.append(element[7])
  name.append(element[8])

filename2 = sys.argv[2] #reads genome file 
DNA = "" #string that builds to be the whole genome
with open(filename2) as GENOME:
    for line in GENOME:
        if line.find(">") != 0: #skip the header of the genome fa file
            DNA += line.strip() #concatenate genome sequences into a 0-indexing string

#goes through appropiate fields and prints out name of gene, 
#locus title, locus tag, followed by the sequence 
for i in range(1, len(start)):
  if reverse[i] == '-': #checks if it is on the reverse strand 
    seq = reverseComp(DNA[int(start[i])-1: int(end[i])])
    print '>' + name[i] + '|' + locus[i] + '|' + tag[i]
    print insert_newlines(seq)
    
  else: #checks if the gene is on the froward strand 
    print '>' + name[i] + '|' + locus[i] + '|' + tag[i]
    seq = DNA[int(start[i])-1: int(end[i])]
    print insert_newlines(seq)
    