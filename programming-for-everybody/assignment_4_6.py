def computepay(h,r):
	if h <= 40:
		p = r * h
	if h > 40:
		p = r * 40 + (r * 1.5 * (h - 40))
	return p

x = raw_input("Enter Hours:")
y = raw_input("Enter Rate:")
hrs = float(x)
rate = float(y)

pay = computepay(hrs, rate)
print pay