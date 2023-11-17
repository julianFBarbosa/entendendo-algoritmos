def regressive(i):
    
    if i < 0:
        return
    print(i)
    regressive(i - 1)
    
# regressive(5)


def fat(i):
    print(i)
    if i == 1: 
        return 1
    return i * fat(i - 1)

print(fat(4))