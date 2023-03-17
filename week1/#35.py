import sys


dwarf_list = []

for i in range(9):
    
    dwarf = int(sys.stdin.readline().rstrip())
    dwarf_list.append(dwarf)

# print(dwarf_list)

X = sum(dwarf_list) - 100   # X : 범인 X1, X2 의 키를 더한 값 

for i in dwarf_list:
    
    index_dwarf = dwarf_list.index(i)

    another_dwarf_list = dwarf_list[index_dwarf+1:]

    for j in another_dwarf_list:
        
        if i + j == X:
            
            dwarf_list.remove(i)
            dwarf_list.remove(j)

            dwarf_list.sort()
            print(*dwarf_list, sep='\n')
            exit(0)                         # index 가 더 돌기 때문에 출력이 완료되면 exit(0) 으로 프로그램 종료
        

    
    
