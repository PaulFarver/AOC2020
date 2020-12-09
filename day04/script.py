import re

fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

validators = {
    'byr': lambda v: int(v) >= 1920 and int(v) <= 2002,
    'iyr': lambda v: int(v) >= 2010 and int(v) <= 2020,
    'eyr': lambda v: int(v) >= 2020 and int(v) <= 2030,
    'hgt': lambda v: (v[-2:] == 'cm' and int(v[:-2]) >= 150 and int(v[:-2]) <= 193) or v[-2:] == 'in' and int(v[:-2]) >= 59 and int(v[:-2]) <= 76,
    'hcl': lambda v: re.match('^#[a-f0-9]{6}$', v),
    'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda v: re.match('^[0-9]{9}$', v)
}


def val(passport):
    for f in fields:
        if f not in passport:
            return False
        if not validators[f](passport[f]):
            return False
    return True

F = open("input.txt", "r")
valid = 0
for l in re.sub(r'\n(\S)', r' \1', F.read()).splitlines():
    passport = {}
    for value in l.split():
        passport[value.split(":")[0]] = value.split(":")[1]
    if val(passport):
        print("valid:  ", passport)
        valid += 1
    else:
        print("invalid:", passport)
        
print(valid)