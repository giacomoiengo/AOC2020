import fileinput

def parseInput(file):
    for line in file:
        line = line.replace(' ', '')
        
        letter     = line.split(':')[0][-1]
        nmin, nmax = tuple(map(int, line.split(':')[0][0:-1].split('-')))
        password   = line.split(':')[1]

        yield (nmin, nmax, letter, password)


def main():
    ans1 = 0
    ans2 = 0

    for nmin, nmax, letter, password in parseInput(fileinput.input()):

        if password.count(letter) in range(nmin, nmax+1):
            ans1 += 1

        nmin -= 1
        nmax -= 1

        if (password[nmin] == letter) ^ (password[nmax] == letter):
            ans2 += 1


    print(ans1)
    print(ans2)

main()