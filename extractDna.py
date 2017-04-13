import sys

def reverseComp(text):
  reverseStack = []
  for i in range(len(text)):
    if text[i] == "A":
      ##text.replace(text[i], 'T')
      reverseStack.append('T')
    elif text[i] == 'T':
      #text.replace(text[i], 'A')
      reverseStack.append('A')
      
    elif text[i] == 'C':
      reverseStack.append('G')
    elif text[i] == 'G':
      reverseStack.append('C')

  reverseComplement = []
  for i in range(len(reverseStack)):
    reverseComplement.append(reverseStack.pop())
  return("".join(str(x) for x in reverseComplement))

def insert_newlines(string, every=70):
    lines = []
    for i in xrange(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)

filename = sys.argv[1]
file = open(filename, 'r')

data = file.readlines()
start = []
end = []
reverse = []
locus = []
tag = []
name = []

for element in data:
  element = element.replace('\n', '')
  element = element.split('\t')
  start.append(element[2])
  end.append(element[3])
  reverse.append(element[4])
  locus.append(element[6])
  tag.append(element[7])
  name.append(element[8])

filename2 = sys.argv[2]
DNA = ""
with open(filename2) as GENOME:
    for line in GENOME:
        if line.find(">") != 0: #skip the header of the genome fa file
            DNA += line.strip() #concatenate genome sequences into a 0-indexing string


for i in range(1, len(start)):
  if reverse[i] == '-':
    seq = reverseComp(DNA[int(start[i])-1: int(end[i])])
    print '>' + name[i] + '|' + locus[i] + '|' + tag[i]
    print insert_newlines(seq)
    
  else:
    print '>' + name[i] + '|' + locus[i] + '|' + tag[i]
    seq = DNA[int(start[i])-1: int(end[i])]
    print insert_newlines(seq)
    

#print start[1], end[1], reverse[1], locus[1], tag[1], name[1]
