input_text = open("input1.txt", "r")
output_text = open("output1.txt", "w")
section_divide = input_text.read().split('$AMJ') #Split the sections according to the common beginning($AMJ)
prog = '$AMJ'+section_divide[2]
# output_text.write(prog)

print(prog)

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

data = ''.join(remove_nl[16:]).split('$DTA')[1].split('$')[0] #This will get the data inside the $DTA and $END section

instr_data = str_instr + data

instr_data_4 = [instr_data[i:i+4] for i in range(0, len(instr_data), 4)]  #To divide the instruction and data set into 4 equal parts

print(instr_data_4)
    



