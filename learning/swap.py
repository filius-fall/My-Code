def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

if __name__ == "__main__":
 print(swap(int(input()),int(input())))
