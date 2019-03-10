f = open("input1.txt", "r")
f1 = open("output1.txt", "w")
str = f.read().split('$AMJ')
prog = '$AMJ'+str[1]
# # f1.write(prog)
# instr_set = prog.split('GD')
# print(instr_set)
nl = []
for x in prog:
    nl.append(x)
for x in nl:
    if(x == '\n'):
        nl.remove(x)
