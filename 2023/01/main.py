words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def rep(line):
    print(line)
    newline = line
    s = ""
    for x in line:
        if not isinstance(x, str):
            s = ""
            continue
        if len #reset string
        s += x
        print(s)

        if s in words:
            newline.replace(s, str(words.index(s) + 1), 1)
            s = ""

    return newline


def calibration(line):
    line = rep(line)

    for x in line:
        try:
            int(x)
            break
        except:
            continue
    for y in line[::-1]:
        try:
            int(y)
            break
        except:
            continue

    return int(f"{x}{y}")

ans = 0
for line in open("in.txt").readlines():
    ans += calibration(line)
    exit(0)

print(ans)
