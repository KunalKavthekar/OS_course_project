import pprint
import itertools as it

def grouper(iterable, n, fillvalue=None):   #function to make chunks of lists from itertools recipes book
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return it.zip_longest(*args, fillvalue="    ")

pp = pprint.PrettyPrinter(indent=4)     #initializing pprint function
input_text = open("input1.txt", "r")   #file read from full path
# input_text = open("input1.txt", "r")
output_text = open("output1.txt", "w")
section_divide = input_text.read().split('$AMJ') #Split the sections according to the common beginning($AMJ)
prog = '$AMJ'+section_divide[2] #changed from [2] to [1] as interpreter throws index error 

#Kunal, this will give you data before H
i_need_till_H = []
for x in prog:
    if x == 'H':
        break
    i_need_till_H.append(x)

i_need_till_H = [x.replace('\n', '') for x in i_need_till_H]
i_need_till_H = "".join(i_need_till_H)

#This will give you data after H
after_H = prog.split('$DTA')[1].split('$')[0]
after_H = ''.join(after_H)
after_H = after_H.split("\n")
    
output_text.write(prog)

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

# print(str_instr)

data = ''.join(remove_nl[16:]).split('$DTA')[1].split('$')[0] #This will get the data inside the $DTA and $END section

# instr_data_4 = [instr_data[i:i+4] for i in range(0, len(instr_data), 4)]  #To divide the instruction and data set into 4 equal parts
# creating seperate lists for instruction set and data.
str_instr_4 = [str_instr[i:i+4] for i in range(0, len(str_instr), 4)]
# data_4 = [data[i:i+4] for i in range(0, len(data), 4)]
str_instr = list(grouper(str_instr_4, 10))
for x in after_H[1:-1]:
    x = [x[i:i+4] for i in range(0, len(x), 4)]
    x = list(grouper(x, 10))
    str_instr.append(x)
pp.pprint(str_instr)

# using grouper function to create uniform chunks
# part_1 = list(grouper(str_instr_4, 10))
# part_2 = list(grouper(data_4, 10))

# instr_data_4 = str_instr_4 + data_4
# puting them together to create final stack
# instr_data_4 = part_1 + part_2  
# pp.pprint(instr_data_4)

# execution of program will start here
