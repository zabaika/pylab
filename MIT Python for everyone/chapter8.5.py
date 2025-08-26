workdir = "C:\\Users\\Zabaika\\YandexDisk\\Coursera\\Python\\"

while True:
    try:
        fname = raw_input("Enter file name: ")
        fh = open(workdir + fname)
        break
    except:
        print "Wrong file name, please enter another"

count = 0
for line in fh:
    if line.startswith('From '):
        line = line.strip().split()
        try:
            print line[1]
            count = count + 1
        except:
            continue
print "There were", count, "lines in the file with From as the first word"
