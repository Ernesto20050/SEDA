from ramdoms import ramdom, randint
dim = 5
largo =10
pos = [0]*dim

def paso (pos, dim):
    d = randint(0, dim-1)
    pos[d] += -1 if ramdom() < 0.5 else 1
    return pos
   
for t in range(largo):
    pos = paso(pos, din)
    print(pos)
