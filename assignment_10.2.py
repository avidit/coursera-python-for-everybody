
name = raw_input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
times = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        time.split()
        hour = time[:2]
        times[hour] = times.get(hour, 0) + 1

lst = list()
for k, v in times.items():
    lst.append((k, v))
    lst.sort()

for k, v in lst:
    print k, v