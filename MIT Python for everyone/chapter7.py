# Use the file name mbox-short.txt as the file name
workdir = "C:\\Users\\Zabaika\\YandexDisk\\Coursera\\Python\\"
count = 0
summa = 0
try:
    fname = input("Enter file name: ")
    fh = open(workdir + fname)
except:
    print("Wrong file name, please enter new")

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    count = count + 1
    summa = summa + float(line[line.find(':') + 1:])
print('Average spam confidence:',summa / count)
