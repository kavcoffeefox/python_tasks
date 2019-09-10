mas = {j+1: [] for j in range(11)}
with open("data.tsv", "r") as f:
    for i in f:
        k = i.split("\t")
        mas[int(k[0])].append(int(k[2]))
for j in mas.keys():
    if len(mas[j]):
        print("{} {}".format(j, sum(mas[j])/len(mas[j])))
    else:
        print("{} -".format(j))
