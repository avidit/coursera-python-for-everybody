
x = raw_input("Enter Hours:")
y = raw_input("Enter Rate:")
hrs = float(x)
rate = float(y)
if hrs <= 40:
	pay = rate * hrs
if hrs > 40:
	pay = rate * 40 + (rate * 1.5 * (hrs - 40))
print pay
