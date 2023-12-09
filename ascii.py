# Write your code here :-)

def chess(x,y):
    if x%2 == y%2:
        return "white"
    else:
        return "black"

for i in range(8):
    for j in range(8):
        print(chess(i, j) , end = " ")
    print()

while True:
    x = int(input())
    y = int(input())
    print(x, "/" , y , "=" , int(x/y) , "remainder" , x%y)
