# 7.2 Write a program that prompts for a file name
# then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

import re

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
	fh = open(fname)
except:
	print 'File not found !!'
	exit()
count = 0
sum = 0
for line in fh:
	line = line.rstrip()
	if not line.startswith("X-DSPAM-Confidence:") : continue
	sum += float(re.findall("\d+.\d+", line)[0])
	count += 1
print "Average spam confidence: ",sum/count
