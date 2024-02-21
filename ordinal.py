# Write your code here :-)

def ordinal(x):
    suff = ""
    if (x%100) in (11, 12, 13):
        suff = "th"
    elif (x%10) == 1:
        suff = "st"
    elif (x%10) == 2:
        suff = "nd"
    elif (x%10) == 3:
        suff = "rd"
    else:
        suff = "th"
    return str(x) + suff


for i in range(1, 32):
    print(ordinal(i))


