import sys


def reverse():
    line = input()
    list = line.split()

    result = []

    for i in list:
        if len(i) % 2 != 0:
            i = i[::-1]
            result.append(i)
            continue
        result.append(i)
    return result


result = reverse()
output = ""
for i in result:
    output = output + " " + i
output = output[1:]
print(output)