def array(a, i=0):
    if i==len(a):
        return
    if i >= 0:
        print(a[i])
        printArray(a, i + 1)
        return

printArray([1,2,3,4,5])
