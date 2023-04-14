from bisect import bisect_left
import sys

input = sys.stdin.readline

while True:
    n = input()

    if not n:
        break

    n = int(n)
    Lis = list(map(int, input().split()))
    answer = []
		
    for i in range(n):
				# answer에 들어갈 index s
        s = bisect_left(answer, Lis[i])
				
				# 지금까지 들어간 수 보다 작으면 교체
        if s != len(answer):
            answer[s] = Lis[i]
				# 지금까지 들어간 수보다 크면 추가
        else:
            answer.append(Lis[i])
    
    print(len(answer))