# Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z.
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
# Compare your results with the tables at ikipedia.org/wiki/Letter_frequencies.

from string import punctuation, whitespace, digits

workdir = "C:\\Users\\Zabaika\\YandexDisk\\Coursera\\Python\\"
while True:
    try:
        fname = input("Enter file name: ")
        if len(fname) < 1: fname = "words.txt"
        fh = open(workdir + fname)
        break
    except:
        print('Cannot open file:', fname, '. Please try, again.')

ignore = punctuation + whitespace + digits
letters = dict()
for line in fh:
    line = line.translate(None, ignore).lower()
    for letter in line:
        letters[letter] = letters.get(letter, 0) + 1

final_list = sorted([(v, k) for k, v in list(letters.items())], reverse=True)
print(('\n'.join(map(str,final_list))))
fh.close()