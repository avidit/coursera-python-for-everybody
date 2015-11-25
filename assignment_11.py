"""
In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.

Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt (There are 116 values with a sum=597873)
Actual data: http://python-data.dr-chuck.net/regex_sum_189889.txt (There are 82 values and the sum ends with 933)
"""
import re

file = open('regex_sum_189889.txt')
lines = file.read()
sum = 0
num = re.findall('[0-9]+', lines)
for number in num:
  sum += int(number)
print sum