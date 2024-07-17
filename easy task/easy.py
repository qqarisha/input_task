s = '1' * 5 + '4' * 2 + '2' * 6

while '12' in s or '4' in s:
    if '12' in s:
        s = s.replace('12', '')
    else:
        s = s.replace('4', '')
    s = s[:2] + s[3:] + s[2]
print(s)

