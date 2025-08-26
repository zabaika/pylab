import sqlite3

try:
    conn = sqlite3.connect('/Users/work_advisa/Yandex.Disk.localized/Coursera/Python/chapter14.sqlite')
    cur = conn.cursor()
except:
    print "Can't connect", conn
    quit()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = '/Users/work_advisa/Yandex.Disk.localized/Coursera/Python/mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    domain = line.strip().split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES ( ?, 1 )''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
                    (domain,))
        # This statement commits outstanding changes to disk each
        # time through the loop - the program can be made faster
        # by moving the commit so it runs only after the loop completes
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print "Counts:"
for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

cur.close()
