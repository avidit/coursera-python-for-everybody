fname = raw_input("Enter file name: ")
if len(fname) < 1: fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
	line = line.split()
	for words in line:
		if words in lst: continue 
		lst.append(words)
lst.sort()
print lst

