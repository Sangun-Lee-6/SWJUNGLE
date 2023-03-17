import sys

Y = int(sys.stdin.readline())


if (Y%4==0 and Y%100 != 0):
    print(1)
elif (Y%100 == 0 and Y%400 != 0):
    print(0)
elif (Y%400 ==0):
    print(1)
else : 
    print(0)

