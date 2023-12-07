# Write your code here :-)
f = open('input.txt')
lines = f.readlines()
output = []
total = 0
for line in lines:
    is_first_num = True
    for chr in line:
        if chr.isdigit():
            last_num = chr
            if is_first_num:
                first_num = chr
                is_first_num = False
    num = int(first_num + last_num)
    output.append(num)
    total = total + num
print(output)
print(total)
