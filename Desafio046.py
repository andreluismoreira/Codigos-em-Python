from time import sleep
for c in range(10, 0, -1):
    print('{}'.format(c))
    sleep(1)
print("\033[1;30mBOOOM !!!")
