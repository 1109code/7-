def turn(key):
    m = len(key)
    turned = [[0] * m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            turned[j][m-i-1] = key[i][j]
            
    return turned

# def move():

# 열쇠로 열어보기
# def check():
    
    
def solution(key, lock):
    answer = True
    # 비교를 위한 확장 lock 보드
    n = len(lock)
    board = [[0] * n * 3 for _ in range(n * 3)]
    
    # 겹치는 범위에서 모두 순회하며 check
    # 4중 for문?
    for i in range(1, 2 * n -1):
        for j in range(1, 2 * n - 1):
            
            for s in range(n, 2 * n - 1):
                for t in range(n, 2 * n - 1):
                    pass
    
    # 90도 회전
    key = turn(key)
    return answer