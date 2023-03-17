import sys

C = int(sys.stdin.readline())

for i in range(C):
    
    input_list = list(map(int,sys.stdin.readline().split()))

    N = input_list[0]

    score_list = input_list[1:]

    mean = sum(score_list) / len(score_list)

    count = 0

    for score in score_list:
        
        if score > mean:
            
            count += 1
    
    result = (count / len(score_list)) *100

    print(f"{result:.3f}"+'%')

        


