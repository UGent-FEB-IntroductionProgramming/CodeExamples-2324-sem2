def exists(key, alist):
    for i in range(len(alist)):
        if alist[i] == key:
            return True
    return False

x = [5,7,8,9]
print(exists(7,x))
