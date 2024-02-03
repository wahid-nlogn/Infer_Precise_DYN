res = []

with open('tmp.log') as f:
    while True:
        line = f.readline().strip()
        if not line:
            break

        if '()' in line:
            continue

        idx = line.find('->')
        line1 = line[:idx]
        line2 = line[idx:]
        for v in line1.split(', '):
            if ':' in v:
                res.append(1)
            else:
                res.append(0)
        if len(line2)>2:
            res.append(1)
        else:
            res.append(0)
print(','.join(map(str, res)))
