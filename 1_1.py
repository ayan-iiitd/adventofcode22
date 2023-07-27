with open('1_input', 'r') as file_opener:
    filecontents = file_opener.readlines()

cals = []
cal_cur = 0

for l in filecontents:

    if l != '\n':
        cal_cur += int(l)
    
    else:
        cals.append(cal_cur)
        cal_cur = 0

print(max(cals))