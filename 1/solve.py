import fileinput

def step1(numbers):
    for n1 in numbers:
        for n2 in numbers:
            if n1 + n2 == 2020:
                return n1*n2

def step2(numbers):
    for n1 in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if n1 + n2 + n3 == 2020:
                    return n1*n2*n3

def main():
    numbers = []
    for number in fileinput.input():
        numbers.append(int(number.strip()))
    print(step1(numbers))
    print(step2(numbers))

main()
            
