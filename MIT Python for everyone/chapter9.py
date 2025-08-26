workdir = "C:\\Users\\Zabaika\\YandexDisk\\Coursera\\Python\\"

while True:
    try:
        fname = raw_input("Enter file name: ")
        if len(fname) < 1: fname = "mbox-short.txt"
        fh = open(workdir + fname)
        break
    except:
        print "Wrong file name, please enter another"
senders = dict()
for line in fh:
    if line.startswith('From '):
        line = line.strip().split()
        try:
            senders[line[1]] = senders.get(line[1], 0) + 1
        except:
            continue
email = None
biggest_count = None
for mail, count in senders.items():
    if email is None or biggest_count < senders[mail]:
        email = mail
        biggest_count = count
print email, biggest_count
