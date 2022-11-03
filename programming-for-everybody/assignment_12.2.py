"""
In this assignment you will write a Python program similar to 
http://www.pythonlearn.com/code/urllink2.py. 
The program will use urllib to read the HTML from the data files below, 
and parse the data, extracting numbers and compute the sum of the numbers in the file.
We provide two files for this assignment. 
One is a sample file where we give you the sum for your testing and
the other is the actual data you need to process for the assignment.

Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2482)
Actual data: http://python-data.dr-chuck.net/comments_189894.html (Sum ends with 24)
"""

import urllib
from BeautifulSoup import *

html = urllib.urlopen('http://python-data.dr-chuck.net/comments_189894.html').read()
soup = BeautifulSoup(html)
tags = soup('span')
sum = 0
count = 0
for tag in tags:
   count += 1
   sum += int(tag.contents[0])
print "Count", count
print "Sum", sum