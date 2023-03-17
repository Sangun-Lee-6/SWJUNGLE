import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
input_list = list(map(int,sys.stdin.readline().split()))

cards_list = list(combinations(input_list, 3))

result_list = []

for cards in cards_list:
    
    result = M - sum(cards)

    if result >= 0:
        result_list.append(result)

output = min(result_list)

sum_cards = (output - M) * -1

print(sum_cards)


        
