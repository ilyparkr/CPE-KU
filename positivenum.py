def PositiveNum(nlist):
    x = list(map(int, nlist))
    total = [n for n in x if n > 0]
    return sum(total)

msg = input()
nlist = msg.split()
print(PositiveNum(nlist))