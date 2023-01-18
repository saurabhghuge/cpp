class team:
            def __init__ (self , name):
                self.name = name
                self.points= 0
                self.diff = 0

t = int(input())
while(t):
    n = 12
    teamlist = []
    teamobjlist = []
    while(n):
        ht,hg,lol,ag,at= input().split(" ")
        if ht  not in teamlist:
            teamobj = team(ht)
            teamlist.append(ht)
            teamobjlist.append(teamobj)
            ind = teamlist.index(ht)
            d = int(hg) - int(ag)
            if d == 0:
                p = 1
            elif d > 0:
                p = 3
            else :
                p = 0
            teamobjlist[ind].points = teamobjlist[ind].points + p
            teamobjlist[ind].diff = teamobjlist[ind].diff + d
        else:
            ind= teamlist.index(ht)
            d = int(hg) - int(ag)
            if d == 0:
                p = 1
            elif d > 0:
                p = 3
            else :
                p = 0
            teamobjlist[ind].points = teamobjlist[ind].points + p
            teamobjlist[ind].diff = teamobjlist[ind].diff + d
        if at  not in teamlist:
            teamobj = team(at)
            teamlist.append(at)
            teamobjlist.append(teamobj)
            ind = teamlist.index(at)
            d = int(ag) - int(hg)
            if d == 0:
                p = 1
            elif d > 0:
                p = 3
            else :
                p = 0
            teamobjlist[ind].points = teamobjlist[ind].points + p
            teamobjlist[ind].diff = teamobjlist[ind].diff + d
        else:
            ind= teamlist.index(at)
            d = int(ag) - int(hg)
            if d == 0:
                p = 1
            elif d > 0:
                p = 3
            else :
                p = 0
            teamobjlist[ind].points = teamobjlist[ind].points + p
            teamobjlist[ind].diff = teamobjlist[ind].diff + d
        n = n-1

    for i in range(len(teamobjlist)):
        for j in range(i+1,len(teamobjlist)):
            if teamobjlist[j].points>= teamobjlist[i].points:
                if teamobjlist[j].points>teamobjlist[i].points:
                    temp = teamobjlist[i]
                    teamobjlist[i]=teamobjlist[j]
                    teamobjlist[j]= temp
                else:
                    if teamobjlist[j].diff > teamobjlist[i].diff:
                        temp = teamobjlist[i]
                        teamobjlist[i]=teamobjlist[j]
                        teamobjlist[j]= temp
        
    fin = teamobjlist[0].name + ' '+  teamobjlist[1].name
    print(fin)
    t = t-1