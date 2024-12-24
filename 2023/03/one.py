arr = open("in.txt").readlines()

big = []
for i, line in enumerate(arr):
    newline = []
    for j, x in enumerate(arr[i]):
        if x in ".*/+$#!@#$%^&*()[]=-_":
            newline.append(x)
        else:
            if j == 0:
                continue
            if arr[i][j-1] in "0123456789":
                newline[-1] = newline[-1] + x
            else:
                newline.append(x)
    newline = newline[:-1]
    big.append(newline)

for line in arr:
    for char in line:
        exi
