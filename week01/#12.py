import sys


def score(n):
    
    if n ==0:
        return 0
    elif n>0:
        return n + score(n-1)




n = int(sys.stdin.readline())

for i in range(n):
    
    input_list = list(map(str,sys.stdin.readline().rstrip()))

    input_list.append('X')

    total = 0

    for i in range(len(input_list)):
        
        try : 
        
          if input_list[i] == 'X':
              
              num_O = input_list[:i].count('O')

              total += score(num_O)

              input_list[:i] = 'X'*len(input_list[:i])
        except:
            break
    
    print(total)

