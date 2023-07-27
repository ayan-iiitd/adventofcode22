with open('2_2input', 'r') as file_opener:
    filecontents = file_opener.readlines()

# for l in filecontents:
#     print(len(l.strip()), l)

label = {'A': 1,
          'B': 2,
          'C': 3,
          'X': -1,
          'Y': 0,
          'Z': 1}
score = 0

for l in filecontents:
    
    a = label[l[0]]
    b = label[l[2]]

    if b == -1:
        if a == 1:
            score += 3
        elif a == 2:
            score += 1
        elif a == 3:
            score += 2
    
    if b == 0:
        score += 3
        if a == 1:
            score += 1
        elif a == 2:
            score += 2
        elif a == 3:
            score += 3
    
    if b == 1:
        score += 6
        if a == 1:
            score += 2
        elif a == 2:
            score += 3
        elif a == 3:
            score += 1







print(score)



