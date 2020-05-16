from enigma.machine import EnigmaMachine
from sys import stdin, stderr

inp = stdin.read().rstrip("\n")
inpdata = []
inptemp = ''

for let in range(len(inp)):
    if inp[let] == ' ':
        inpdata.append(inptemp)
        inptemp = ''
    else:
        inptemp += inp[let]

print(len(inpdata))
"""
for i in range((len(inpdata) / 17)):
    machine = EnigmaMachine.from_key_sheet(
        rotors='{} {} {}'.format(inpdata[i], inpdata[i+1], inpdata[i+2]),
        reflector='{}'.format(inpdata[i+3]),
        ring_settings='{} {} {}'.format(inpdata[i+4], inpdata[i+5], inpdata[i+6]),
        plugboard_settings='{} {} {} {} {} {} {} {} {} {}'.format(inpdata[i+7], inpdata[i+8], inpdata[i+9], inpdata[i+10], inpdata[i+11], inpdata[i+12], inpdata[i+13], inpdata[i+14], inpdata[i+15], inpdata[i+16]))
    decrypted_message = machine.process_text(message)
    print(decrypted_message)
"""
