import sys

inp = sys.stdin.read()

newinp = ""
for i in range(len(inp)):
    if inp[i] == "X":
        newinp += " "
    else:
        newinp += inp[i]
print(newinp)
