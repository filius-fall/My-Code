import os
path = '/home/rams/Desktop/'
for a in range(11):
    f = 'folder'+str(a)
    g = os.path.join(path,f)
    os.mkdir(g)
    for b in range(101):
        h = 'innerfolder_' + str(b)
        i = os.path.join(g,h)
        os.mkdir(i)
        if b%7 == 0:
            j = i + '//james.txt'
            txtfile = open(j , 'w+')
            for c in range(b+1):
                txtfile.write("bond \n")
            txtfile.close()