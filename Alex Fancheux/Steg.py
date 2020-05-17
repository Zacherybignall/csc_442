############################
# Name: Alex Faucheux
# Language: Python 3
#############################

from sys import stdout
import argparse

# Byte sequence that signifies the end of a file
SENTINEL = b'\x00\xff\x00\x00\xff\x00'


# Stores bytes into file
def store(wrapper, hidden, kind, offset, interval):
    # Embeds hidden file into wrapper
    for hbyte in hidden:
        # bit algorithm
        if kind == "-b":
            # Iterates a byte from the wrapper for each embedded bit
            for j in range(8):
                # Reserves all but last bit
                wrapper[offset] &= int(b'11111110', 2)
                # Reserves first hidden bit, shifts it to the right 7 places, and
                # inserts bit into current wrapper byte
                wrapper[offset] |= ((hbyte & int(b'10000000', 2)) >> 7)
                # Shifts hidden byte to the left once and reserves 8-bit size
                hbyte = (hbyte << 1) & (2 ** 8 - 1)
                offset += interval

        # Byte algorithm
        else:
            # set current wrapper byte to current hidden byte
            wrapper[offset] = hbyte
            offset += interval

    # Embeds sentinel byte sequence
    for sbyte in SENTINEL:
        # Bit algorithm - same as above
        if kind == '-b':
            for j in range(8):
                wrapper[offset] &= int(b'11111110', 2)
                wrapper[offset] |= ((sbyte & int(b'10000000', 2)) >> 7)
                sbyte = (sbyte << 1) & (2 ** 8 - 1)
                offset += interval

        # Byte algorithm - same as above
        else:
            wrapper[offset] = sbyte
            offset += interval


# Retrieved hidden file/message that is embedded into another file
def retrieve(wrapper, kind, offset, interval):
    # Stores the hidden message
    hidden_bytes = bytearray()

    # Bit algorithm
    if kind == '-b':
        sIndex = 0  # Sentinel index
        # temporary sequence when testing for sentinel
        temp = bytearray()

        # iterates through bytes in wrapper
        while offset < len(wrapper):
            b = 0
            # Iterates the next 8 bytes in wrapper to create one byte
            # Fetches value from last bit in each byte
            for j in range(8):
                # Reserves only the last bit from wrapper byte and joins with b
                b |= (wrapper[offset] & int(b'00000001', 2))
                offset += interval
                if j < 7:
                    # Shifts b to the left to provide space for the next bit
                    b = (b << 1) & (2 ** 8 - 1)

                if offset >= len(wrapper):
                    raise Exception("Reached end of file.  SENTINEL not found")

            # Checks to see if current byte assigned to b is in current SENTINEL index
            # if so, increment sentinel index, add byte to temporary list, and increment offset
            if b == SENTINEL[sIndex]:
                sIndex += 1
                temp.append(b)

            # Added to account for multiple 0s in a row for sentinel
            elif b == 0:
                sIndex = 1
                for byte in temp:
                    hidden_bytes.append(byte)
                temp = [b]

            # If b does not line with sentinel
            else:
                sIndex = 0
                # add temporarily stored bytes to the message byte array
                for byte in temp:
                    hidden_bytes.append(byte)
                temp = bytearray()

                # add current b to main array
                hidden_bytes.append(b)

            # If sentinel is found, break form loop
            if sIndex == len(SENTINEL):
                break

    # Retrieve byte algorithm
    else:
        # Iterate bytes in wrapper
        while offset < len(wrapper):
            sINDEX = 0
            temp = bytearray()

            # Iterates while current sentinel byte == wrapper byte
            while SENTINEL[sINDEX] == wrapper[offset]:
                temp.append(wrapper[offset])
                sINDEX += 1
                offset += interval
                if sINDEX == len(SENTINEL):
                    break
                if offset >= len(wrapper):
                    raise Exception("SENTINEL not found")

            if sINDEX == len(SENTINEL):
                break

            else:
                for byte in temp:
                    hidden_bytes.append(byte)

            hidden_bytes.append(wrapper[offset])
            offset += interval

    return hidden_bytes


if __name__ == "__main__":
    # Adds the support for argument handling
    # Add_help is false because "-h" is help which conflicts with "-h" for hidden
    parser = argparse.ArgumentParser(description="Steganography encoder/decoder", add_help=False)
    group1 = parser.add_mutually_exclusive_group()
    group2 = parser.add_mutually_exclusive_group()

    group1.add_argument("-s", "--store", action="store_true")
    group1.add_argument("-r", "--retrieve", action="store_true")

    group2.add_argument("-b", "--bit", action="store_true")
    group2.add_argument("-B", "--byte", action="store_true")

    parser.add_argument("-o", "--offset", type=int, default=0)
    parser.add_argument("-i", "--interval", type=int, default=1)
    parser.add_argument("-w", "--wrapper", type=str)
    parser.add_argument("-h", "--hidden", type=str)

    args = parser.parse_args()

    # Makes sure required parameters are met
    if (args.store or args.retrieve) and (args.bit or args.byte) and args.wrapper:
        # Opens the wrapper in binary and converts to bytearray to make it mutable
        wrapper = bytearray(open(args.wrapper, "rb").read())

        # if user chooses store, they also need to specify hidden
        if args.store and args.hidden:
            # Opens hidden file in binary.  No need to convert to bytearray.  No need to change the bytes
            hidden = open(args.hidden, "rb").read()
            store(wrapper, hidden, "-b" if args.bit else "-B",
                  args.offset, args.interval)

        # Retrieval option
        elif args.retrieve:
            wrapper = retrieve(wrapper, "-b" if args.bit else "-B", args.offset, args.interval)

        # If neither occurs, just exit the program
        else:
            exit(0)

        stdout.buffer.write(wrapper)
