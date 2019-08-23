import sys

N = input()
length = len(N)
N_list = []
final = []
list = ""
list1 = ""

for i in N:
    N_list.append(i)

for i in N_list:
    list = list + " " + i

final.append(list)

for i in range(0, length - 1):
    if i > 0:
        for m in range(0, i):
            list1 = list1 + " " + N_list[m]

    list1 = list1 + " " + N_list[i] + N_list[i + 1]
    if (i + 1) < (length - 1):
        for j in range(i + 1, length - 1):
            list1 = list1 + " " + N_list[j + 1]
    final.append(list1)
    list1 = ""

print(N_list)
