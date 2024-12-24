def main(line):
    R = 12
    G = 13
    B = 14

    line = line.split(": ")[1]
    line = line.split("\n")[0]
    for game in line.split("; "):
        rd = game.split(", ")
        for i, op in enumerate(rd):
            op = op.split(" ")
            if op[1] == "green":
                if int(op[0]) > G:
                    return False
            elif op[1] == "blue":
                if int(op[0]) > B:
                    return False
            elif op[1] == "red":
                if int(op[0]) > R:
                    return False
        
    return True
ans = 0
for line in open("in.txt").readlines():
    if main(line):
        ans += int(line.split(" ")[1].split(":")[0])
print(ans)
