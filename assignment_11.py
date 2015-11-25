import re

file = open('regex_sum_189889.txt')
lines = file.read()
sum = 0
num = re.findall('[0-9]+', lines)
for number in num:
  sum += int(number)
print sum
