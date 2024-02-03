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
                v=v.split(":")
                res.append(v[0])
            else:
                res.append("")
        if len(line2)>2:
            res.append(line2)
        else:
            res.append("")
print(','.join(map(str, res)))