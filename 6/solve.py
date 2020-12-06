import fileinput

def main():
    content = ''.join(tuple(fileinput.input()))
    content = [group.split() for group in content.split('\n\n')]

    ans1 = 0
    ans2 = 0
    for group in content:
        sgroup = [set(p) for p in group]
        ans1  += len(set.union       (*sgroup))
        ans2  += len(set.intersection(*sgroup))


    print(ans1)
    print(ans2)
    
main()