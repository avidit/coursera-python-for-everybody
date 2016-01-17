"""
In this assignment you will write a Python program somewhat similar to 
http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, 
read the JSON data from that URL using urllib and then parse and extract the 
comment counts from the JSON data, compute the sum of the numbers in the file 
and enter the sum below:
We provide two files for this assignment. One is a sample file where we give 
you the sum for your testing and the other is the actual data you need to 
process for the assignment.

Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2482)
Actual data: http://python-data.dr-chuck.net/comments_189895.json (Sum ends with 25)
"""
import json
import urllib

url = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
info = json.loads(data)

sum = 0
for user in info['comments']:
	sum += user['count']

print "Count: {}".format(len(info['comments']))
print "sum: {}".format(sum)
