# -*- coding: utf-8 -*-
"""
Template for enigma machine challange
See https://py-enigma.readthedocs.io/en/latest/guide.html#building-your-enigma-machine
for more information
"""


from enigma.machine import EnigmaMachine
from sys import stdin, stderr

#All Wehrmacht models
LIST_OF_ROTORS = ['I','II','III','IV', 'V']
#Kriegsmarine M3 & M4
#LIST_OF_ROTORS = ['I','II','III', 'IV', 'V', 'VI', 'VII', 'VIII']

#X is not in use, to make your life easier
ALPHABET=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']

#there are more reflectors, but this will be bad enough for you to deal with.
LIST_OF_REFLECTORS = ['B', 'C']

message = stdin.read().rstrip("\n")

#splugs = ['LO', 'KI', 'JU', 'HY', 'GT', 'FR', 'DE', 'SW', 'QA']
srotors = ['I', 'IV', 'V']
grotors = ['II', 'III']
sreflectors = ['B', 'C']
srings = ['W', 'H']

temp = []
trotors = []
trings = []
talph = []

for srotor in srotors:
    temp = [srotor, grotors[0], grotors[1]]
    #trotors.append(temp)
    temp = [srotor, grotors[1], grotors[0]]
    #trotors.append(temp)
    temp = [grotors[0], srotor, grotors[1]]
    #trotors.append(temp)
    temp = [grotors[1], srotor, grotors[0]]
    #trotors.append(temp)
    temp = [grotors[0], grotors[1], srotor]
    #trotors.append(temp)
    temp = [grotors[1], grotors[0], srotor]
    trotors.append(temp)

for let in ALPHABET:
    if let not in srings:
        temp = [let, srings[0], srings[1]]
        trings.append(temp)
        temp = [let, srings[1], srings[0]]
        trings.append(temp)
        temp = [srings[0], let, srings[1]]
        trings.append(temp)
        temp = [srings[1], let, srings[0]]
        trings.append(temp)
        temp = [srings[0], srings[1], let]
        trings.append(temp)
        temp = [srings[1], srings[0], let]
        trings.append(temp)

"""
temp = [srotors[0], srotors[1], srotors[2]]
trotors.append(temp)
temp = [srotors[0], srotors[2], srotors[1]]
trotors.append(temp)
temp = [srotors[1], srotors[0], srotors[2]]
trotors.append(temp)
temp = [srotors[1], srotors[2], srotors[0]]
trotors.append(temp)
temp = [srotors[2], srotors[0], srotors[1]]
trotors.append(temp)
temp = [srotors[2], srotors[1], srotors[0]]
trotors.append(temp)

temp = [srings[0], srings[1], srings[2]]
trings.append(temp)
temp = [srings[0], srings[2], srings[1]]
trings.append(temp)
temp = [srings[1], srings[0], srings[2]]
trings.append(temp)
temp = [srings[1], srings[2], srings[0]]
trings.append(temp)
temp = [srings[2], srings[0], srings[1]]
trings.append(temp)
temp = [srings[2], srings[1], srings[0]]
trings.append(temp)

usedalpha = []
for plug in splugs:
    usedalpha.append(plug[0])
    usedalpha.append(plug[1])

for let1 in ALPHABET:
    for let2 in ALPHABET:
        if let1 not in usedalpha and let2 not in usedalpha and let1 != let2:
            temp = '{}{}'.format(let1, let2)
            talph.append(temp)
talph = talph[:5]
"""

for rincon in trings:
    for rotcon in trotors:
        machine = EnigmaMachine.from_key_sheet(
            rotors='{} {} {}'.format(rotcon[0], rotcon[1], rotcon[2]),
            reflector='C',
            ring_settings='{} {} {}'.format(rincon[0], rincon[1], rincon[2]),
            plugboard_settings='ZM AS QW DF ER CV BN GH TY JK')
        decrypted_message = machine.process_text(message)
        print(decrypted_message)



#This is one way to create an enigma machine, there are others ;)
machine = EnigmaMachine.from_key_sheet(
    rotors='I II III',
    reflector='C',
    ring_settings='M O O',
    plugboard_settings='QZ WG EC RV TB YN UM IK OL PA')
    
decrypted_message = machine.process_text(message)
print(decrypted_message)

