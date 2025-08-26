def print_by_count(dict):
    final_list = sorted([(v, k) for k, v in list(dict.items())], reverse=True)
    for count, hour in final_list:
        print(hour, count)


workdir = "C:\\Users\\Zabaika\\YandexDisk\\Coursera\\Python\\"
while True:
    try:
        fname = input("Enter file name: ")
        if len(fname) < 1: fname = "mbox-short.txt"
        fh = open(workdir + fname)
        break
    except:
        print("Wrong file name, please enter another")

hours = dict()
for line in fh:
    if line.startswith('From '):
        line = line.strip().split()
        try:
            tmp_hour = line[5].split(':')[0]
            hours[tmp_hour] = hours.get(tmp_hour, 0) + 1
        except:
            continue

for key in sorted(hours):
    print(key, hours[key])
