import fileinput

def traverse(increment, treemap):
    width  = len(treemap[0])
    height = len(treemap)
    x, y, trees  = 0, 0, 0

    while True:
        x += increment[0]
        y += increment[1]
        if y >= height:
            break
        if treemap[y][x%width] == '#':
            trees += 1

    return trees


def main():
    treemap = list(map(str.strip, fileinput.input()))

    slopes = [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
    ]


    ans1 = traverse(slopes[1], treemap)
    ans2 = 1
    for k in slopes:
        ans2 *= traverse(k, treemap)
    
    print(ans1, ans2)

main()