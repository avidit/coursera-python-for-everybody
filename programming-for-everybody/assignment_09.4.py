
name = raw_input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
email = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        start = words[1]
        email[start] = email.get(start, 0) + 1

committer = None
count = None

for sender in email:
    if committer is None or count < email[sender]:
        committer = sender
        count = email[sender]
print committer, count