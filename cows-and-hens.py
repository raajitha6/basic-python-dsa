legs=int(input("no. of legs:"))
heads=int(input("no. of heads:"))
flag=False
for cows in range(heads+1):
    hens=heads-cows
    cal_legs=cows*4+hens*2
    if cal_legs==legs:
        flag=True
        break
if flag:
    print("Cows:",cows)
    print("Hens:",hens)
else:
    print("No solution")