import inspect
inp = open("in.txt").readlines()

fxns = inp[1:599]
parts = inp[600:]

FF = []
i = 0
"""
for fxn in fxns:
    name = fxn.split("{")[0]
    conditions = fxn.split("{")[1].split("}")[0].split(",")

    actions = []
    for cond in conditions:
        req = cond.split(":")[0]
        print(req)
        print(cond)

        try:
            do = cond.split(":")[1]
            def fun1(): eval(do + "()")
            actions.append(fun1)
        except:
            def fun1(): eval(req + "()")
            actions.append(fun1)

        i += 1
        print(conditions)

        print(actions)
    for action in actions:
        print(inspect.getsource(action))
"""
for part in parts:
    x, m, a, s = part[1:-2].replace("x=", "").replace("m=","").replace("a=","").replace("s=","").split(",")
    x, m, a, s = int(x), int(m), int(a), int(s)

    for fxn in fxns:
        check(x, m, a, s)
    exit(0)
