dict01 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
val = []
# for i in dict01.keys():
#     val.append(i)
# item = dict01.items()
int = input()
for i in int:
    val.append(i)
for j in range(len(int)-1):
    if val[j] >= val[j+1]:
        b = val[j]+val[j+1]
    