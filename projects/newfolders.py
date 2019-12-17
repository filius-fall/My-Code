import os
def filec(outer,inner):
    print('Type the path which ends with /')
    path = input()
    for i in range(1,outer+1):
        folder_name = 'folder' + str(i)
        new_path = os.path.join(path,folder_name)
        os.mkdir(new_path)
        for j in range(1,inner+1):
            inner_folder = 'subfolder' + str(j)
            inner_path = os.path.join(new_path,inner_folder)
            os.mkdir(inner_path)
print('enter no of outer folders')
o = int(input())
print('enter no of inner folders')
i = int(input())
s = filec(o,i)
