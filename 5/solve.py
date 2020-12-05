import fileinput

def f(start, index, bsp):
    amount = len(start)
    half   = amount // 2

    lower  = list(range(start[0], start[0] + half))
    higher = list(range(start[0] + half, start[-1]+1))

    if bsp[index] == 'F':
        nrange = lower
    
    elif bsp[index] == 'B':
        nrange = higher

    if index == len(bsp) - 1:
        return nrange

    return f(nrange, index+1, bsp)

def genSids(bsps):
    sids = set()
    srow  = list(range(0,2**7))
    scol  = list(range(0,2**3))
    
    for bsp in bsps:
        irow, icol = (bsp[0:-3], bsp[-3:])
        icol = icol.replace('L', 'F').replace('R', 'B')
        row = f(srow, 0, irow)[0]
        col = f(scol, 0, icol)[0]
        sids.add(row * 8 + col)

    return sids



def main():
    actualBsps   = list(map(str.strip,tuple(fileinput.input())))
    actualSids   = genSids(actualBsps)
    maxSid       = max(actualSids)
    possibleSids = set(range(0,maxSid+1))

    print(maxSid)
    print(possibleSids.difference(actualSids))
    

    

main()
