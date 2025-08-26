def computepay(hours, rate):
    if hours > 40:
        ext_hours = hours - 40
        payment = ext_hours * rate * 1.5 + 40 * rate
    else:
        payment = hours * rate
    return payment


try:
    hours = float(raw_input('Enter hours: '))
    rate = float(raw_input('Enter rate: '))
except:
    print "Wrong number"
    quit()
result = computepay(hours, rate)
print result
