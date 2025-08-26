try:
    score = float(input('Enter score: '))
except:
    print("Error, please enter a number.")
    quit()

if score > 0.00 and score < 1.00:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Error, out of range")
