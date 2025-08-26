workdir = "C:\\Users\\Zabaika\\YandexDisk\\Coursera\\Python\\"
lst = list()
while True:
    try:
        fname = input("Enter file name: ")
        fh = open(workdir + fname)
        break
    except:
        print("Wrong file name, please enter another")

for line in fh:
    thisline = line.strip().split()
    for word in thisline:
        if word in lst: continue
        lst.append(word)
lst.sort()
print(lst)
