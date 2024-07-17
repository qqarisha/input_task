min_len = 99999999999999999
for n in range(6, 10):
    s = '1' * 5 + '4' * 2 + '2' * n

    while '12' in s or '4' in s:
        if '12' in s:
            s = s.replace('12', '')
        else:
            s = s.replace('4', '')
        if len(s) > 3:
            s = s[:2] + s[3:] + s[2]
    min_len = min(len(s), min_len)
print(min_len)

