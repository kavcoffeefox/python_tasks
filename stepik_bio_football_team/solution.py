c_teams = int(input())
res_team = {}
for _ in range(c_teams):
    line = input().split(";")
    if line[0] not in res_team.keys():
        res_team[line[0]] = [0,0,0,0]
    if line[2] not in res_team.keys():
        res_team[line[2]] = [0,0,0,0]
    res_team[line[0]][0] = res_team[line[0]][0] + 1
    res_team[line[2]][0] = res_team[line[2]][0] + 1
    if int(line[1]) > int(line[3]):
        res_team[line[0]][1] = res_team[line[0]][1] + 1
        res_team[line[2]][3] = res_team[line[2]][3] + 1
    elif int(line[1]) == int(line[3]):
        res_team[line[0]][2] = res_team[line[0]][2] + 1
        res_team[line[2]][2] = res_team[line[2]][2] + 1
    else:
        res_team[line[0]][3] = res_team[line[0]][3] + 1
        res_team[line[2]][1] = res_team[line[2]][1] + 1
for i in res_team.keys():
    print("{}:{} {} {} {} {}".format(i,res_team[i][0],res_team[i][1], res_team[i][2], res_team[i][3], str(res_team[i][1]*3+res_team[i][2]*1)))
