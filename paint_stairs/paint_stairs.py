import sys
try:
    num_steps = int(sys.argv[1])
except:
    print("Error! No valid param")

tr_rez = ""
for i in range(num_steps):
    for j in range(num_steps):
           tr_rez += " " if j + 1 < (num_steps - i) else "#"
    print(tr_rez)
    tr_rez = ""

