import re

workdir = "C:\\Users\\Zabaika\\YandexDisk\\Coursera\\Python\\"
print(sum([int(num) for num in re.findall('[0-9]+', open(workdir + 'regex_sum_241034.txt').read())]))
