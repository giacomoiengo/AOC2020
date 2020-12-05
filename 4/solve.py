import fileinput
import re

def checkHGT(value):
    if value.endswith('cm'):
        x = int(value[0:-2])
        return (x <= 193  and x >= 150)

    if value.endswith('in'):
        x = int(value[0:-2])
        return (x <= 76  and x >= 59)
    
    return False


filters = {
    'byr' : lambda x: int(x) <= 2002 and int(x) >= 1920,
    'iyr' : lambda x: int(x) <= 2020 and int(x) >= 2010,
    'eyr' : lambda x: int(x) <= 2030 and int(x) >= 2020,
    'hgt' : checkHGT,
    'hcl' : re.compile('^#[0-9|a-f]{6}$'),
    'ecl' : re.compile('amb|blu|brn|gry|grn|hzl|oth'),
    'pid' : re.compile('^[0-9]{9}$'),
    'cid' : lambda x: True
}



def validPassport(passport, filters):
    valids = []
    hascid = 'cid' in passport.keys()
    for k,v in passport.items():
        if callable(filters[k]):
            valids.append(filters[k](v))
        else:
            valids.append(bool(filters[k].match(v)))
    
    return (all(valids) and len(valids) == 8) or\
           (all(valids) and len(valids) == 7 and not hascid)



        

def main():
    plist = ''.join(tuple(fileinput.input()))
    plist = plist.split('\n\n')
    pmaps = []
    for line in plist:
        line = [value.split(':') for value in line.replace('\n', ' ').split()]
        pmaps.append(dict(line))

    ans = len([x for x in pmaps if validPassport(x, filters)])
    print(ans)

main()