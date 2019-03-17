from textwrap import wrap #To divide the instruction set into 4 equal parts

input_text = open("input1.txt", "r")
output_text = open("output1.txt", "w")
section_divide = input_text.read().split('$AMJ') #Split the sections according to the common beginning($AMJ)
prog = '$AMJ'+section_divide[1]
# output_text.write(prog)

instr_set = []
remove_nl = []

for x in prog:
    remove_nl.append(x)
for x in remove_nl:
    if(x == '\n'):
        remove_nl.remove(x)

for x in remove_nl[16:]:
    if(x == 'H'):
        break
    else:
        instr_set.append(x)

str_instr = ''.join(instr_set)
print(wrap(str_instr, 4))