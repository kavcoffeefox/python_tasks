def modify_list(l):
    l1 = [i//2 for i in l if i%2 == 0]
    l.clear()
    l.extend(l1)
