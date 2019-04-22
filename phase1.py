import pprint
import itertools as it

buffer = ""
R = ""
C = 0
output = ""
SI = 0
card = 0

def grouper(iterable, n, fillvalue=None):   #function to make chunks of lists from itertools recipes book
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return it.zip_longest(*args, fillvalue="    ")


def READ(n):                                #function to execute GD command
    n = str(n)
    temp1 = int(n[0])
    temp2 = int(n[1])
    if(temp2 == 0):
        buffer = "".join(str_instr[temp1][0:9])

def WRITE(n):                               #function to execute PD command
    n = str(n)
    temp1 = int(n[0])
    temp2 = int(n[1])
    if(temp2 == 0):
        output = "".join(str_instr[temp1][0:9])
    output_text.write(output)

def TERMINATE():                            #function to terminate current program
    pass

def MOS(n, start_var):                      #Master function
    if(n == 1):
        READ(start_var)
    elif(n == 2):
        WRITE(start_var)
    elif(n == 3):
        # TERMINATE()
        pass

def EXECUTEUSERPROGRAM(user_prog):          #Slave mode functions to implement all operations
    IC = 0
    IR = ''
    user_prog_4 = [user_prog[i:i+4] for i in range(0, len(user_prog), 4)]
    for x in user_prog_4:
        IR = x[0:2]
        start_var = x[2:]
        i = int(x[2])
        k = int(x[3])
        IC = IC + 1
        if IR == 'LR':
            R = "".join(str_instr[i][k])

        elif IR == 'SR':
            str_instr[i][k] = R

        elif IR == 'CR':
            if R == str_instr[i][k]:
                C = 1
            else:
                C = 0

        elif IR == 'BT':
            if C == 1:
                IC = start_var

        elif IR == 'GD':
            SI = 1
            MOS(SI, start_var)

        elif IR == 'PD':
            SI = 2
            MOS(SI, start_var)

        elif IR == 'H ':
            SI = 3
            MOS(SI, start_var = 0)

        else:
            print("Something went wrong")         


pp = pprint.PrettyPrinter(indent=4)     #initializing pprint function
# input & output files initialized
input_text = open("input1.txt", "r")  
output_text = open("output1.txt", "a")
section_divide = input_text.read().split('$AMJ') #Split the sections according to the common beginning($AMJ)

for x in section_divide:                    #Loop to load and execute each program, one at a time

    card = card + 1    
    prog = '$AMJ'+section_divide[card]

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

    instr_set.append('H   ')
    str_instr = ''.join(instr_set)

    user_prog = str_instr

    data = ''.join(remove_nl[16:]).split('$DTA')[1].split('$')[0] #This will get the data inside the $DTA and $END section

    str_instr_4 = [str_instr[i:i+4] for i in range(0, len(str_instr), 4)]

    str_instr = list(grouper(str_instr_4, 10))
    for x in after_H[1:-1]:
        x = [x[i:i+4] for i in range(0, len(x), 4)]
        x = list(grouper(x, 10))
        str_instr.extend(x)

    empty = '        '
    str_empty_4 = [empty[i:i+4] for i in range(0,len(empty), 4)]
    while len(str_instr) != 10:
        x = list(grouper(str_empty_4,10))
        str_instr.extend(x)

    # execution of program will start here
    EXECUTEUSERPROGRAM(user_prog)
