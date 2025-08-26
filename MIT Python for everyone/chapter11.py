# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
import re

workdir = "C:\\Users\\Zabaika\\YandexDisk\\Coursera\\Python\\"
filename = 'regex_sum_241034.txt'

try:
    fh = open(workdir + filename)
except:
    print('Cannot open file:', filename, '. Please try, again.')
summa = int(0)
for line in fh:
    tmp = re.findall('[0-9]+', line)
    for num in tmp:
        summa = summa + int(num)
print(summa)
