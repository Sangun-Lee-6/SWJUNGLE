import sys

x,y,w,h = map(int, sys.stdin.readline().split())

length_list = [x,y,w-x,h-y]

print(min(length_list))
