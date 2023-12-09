# Write your code here :-)

def timecon(secs):
    t = int(secs)
    if t >= 86400:
        days = int(t/86400)
        t = t%86400
        print(days, "d", end=" ")
    if t >= 3600:
        hours = int(t/3600)
        t = t%3600
        print(hours, "h", end=" ")
    if t >= 60:
        mins = int(t/60)
        t = t%60
        print(mins, "m", end=" ")
    print(t, "s")

while True:
    secs = input("Time?")
    timecon(secs)

