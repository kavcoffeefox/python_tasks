with open("data.txt", "r") as f:
    string = f.read()
res = dict()
word,max_count = "", 0
for i in string.lower().split():
    if i in res.keys():
        res[i] = res[i] + 1
    else:
        res[i] = 1
for i in res.keys():
    if res[i] > max_count:
        max_count = res[i]
        word = i
print("{} {}".format(word, max_count))
