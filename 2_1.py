with open('2_1input', 'r') as file_opener:
    filecontents = file_opener.readlines()

# for l in filecontents:
#     print(len(l.strip()), l)

label = {'A': 1,
          'B': 2,
          'C': 3,
          'X': 1,
          'Y': 2,
          'Z': 3}
score = 0

for l in filecontents:
    a = label[l[0]]
    b = label[l[2]]

    score += b

    if b == 1:
        if a == 3:
            score += 6
        elif a == 1:
            score += 3
        else:
            score += 0

    if b == 2:
        if a == 1:
            score += 6
        elif a == 2:
            score += 3
        else:
            score += 0
    
    if b == 3:
        if a == 2:
            score += 6
        elif a == 3:
            score += 3
        else:
            score += 0





print(score)



