def tringle(r,c):
    if r==0:
        return
    if (c<r ):
        print('* ',end = " ")
        tringle(r,c+1)
    else:
        print()
        tringle(r-1,0)

print(tringle(4,0))