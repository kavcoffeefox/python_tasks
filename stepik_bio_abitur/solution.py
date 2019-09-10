mt, ph, ru = list(), list(), list()
with open("result.txt", "w") as rf:
    with open("data.txt", "r") as f:
        for i in f:
            l = list(map(int, i.split(";")[1:]))
            mt.append(l[0])
            ph.append(l[1])
            ru.append(l[2])
            rf.write(str(sum(l)/len(l)) + "\n")
    rf.write(" ".join(map(str, [sum(mt)/len(mt), sum(ph)/len(ph), sum(ru)/len(ru)])))
