from sys import stdin

codebook = stdin.read()
cbdata = []
cbtemp = ''

for let in range(len(codebook)):
    if codebook[let] == ' ':
        cbdata.append(cbtemp)
        cbtemp = ''
    else:
        cbtemp += codebook[let]

rotors = ['I', 'III', 'II']

reflectors = ['B', 'C']

rings = ['F', 'O', 'M']

plugboard = ['QZ', 'WG', 'EC', 'RV', 'TB', 'YN', 'UM', 'IK', 'OL', 'PA']

sol = []
'''
for i in range(len(cbdata)):
    if cbdata[i] in rotors:
        if cbdata[i+1] in rotors:
            if cbdata[i+2] in rotors:
                if cbdata[i+3] in rings:
                    if cbdata[i+4] in rings:
                        if cbdata[i+5] in rings:
                            if cbdata[i+16] in reflectors:
                                sol.append(cbdata[i-1].lstrip('\n'))
                                for s in range(17):
                                    sol.append(cbdata[i+s])'''

for i in range(len(cbdata)):
    if cbdata[i] == plugboard[0]:
        if cbdata[i+1] == plugboard[1]:
            if cbdata[i+2] == plugboard[2]:
                if cbdata[i+3] == plugboard[3]:
                    if cbdata[i+4] == plugboard[4]:
                        if cbdata[i+5] == plugboard[5]:
                            if cbdata[i+6] == plugboard[6]:
                                if cbdata[i+7] == plugboard[7]:
                                    if cbdata[i+8] == plugboard[8]:
                                        if cbdata[i+9] == plugboard[9]:
                                            for s in range(8):
                                                sol.append(cbdata[i-7+s])

print(sol)
