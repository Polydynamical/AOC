import math
def main(line):
    _gmax = -math.inf
    _rmax = -math.inf
    _bmax = -math.inf

    line = line.split(": ")[1]
    line = line.split("\n")[0]
    for game in line.split("; "):
        rd = game.split(", ")
        for i, op in enumerate(rd):
            op = op.split(" ")
            if op[1] == "green":
                _gmax = max(_gmax, int(op[0]))
            elif op[1] == "blue":
                _bmax = max(_bmax, int(op[0]))
            elif op[1] == "red":
                _rmax = max(_rmax, int(op[0]))
        
    return _gmax * _bmax * _rmax
ans = 0
for line in open("in.txt").readlines():
    ans += main(line)
    
print(ans)
