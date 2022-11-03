largest = None
smallest = None

while True:
	try:
		inp = raw_input("Enter a number: ")
		if inp == 'done': break
		if len(inp) < 1: break
		num = float(inp)
	except:
		print 'Invalid input'
		continue
	
	if largest is None or num > largest: largest = num
	if smallest is None or num < smallest: smallest = num

print "Maximum is", int(largest)
print "Minimum is", int(smallest)