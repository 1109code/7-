def turn(key):
    m = len(key)
    turned = [[0] * m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            turned[j][m-i-1] = key[i][j]
            
    return turned
    
    
def solution(key, lock):
    answer = False
    
    m = len(key)    # key
    n = len(lock)   # lock
    
    # key 확장해서 lock 껴보기
    expand_key = [[0] * (m + 2 * n) for _ in range(m + 2 * n)]
                                                   
    # 확장 후 key 넣기
    for i in range(n, n + m):
        for j in range(n, n + m):
            expand_key[i][j] = key[i - n][j - n]
    
    # 겹치는 범위에서 모두 순회하며 check
    # 4번 회전
    for k in range(4):
        # 0부터 순회 시 아예 키 꽂지도 않음
        for i in range(1, n + m):
            for j in range(1, n + m):
                flag = True
                # 열쇠 검사, 한 번이라도 열쇠가 맞으면 탈출
                for s in range(n):
                    for t in range(n):
                        if lock[s][t] + expand_key[i + s][j + t] != 1:
                            flag = False
                            break
                    if flag == False:
                        break
                        
                if flag == True:
                    answer = True
                    break
            # 열쇠가 맞아서 나왔으면 탈출
            if answer == True:
                break
        if answer == True:
            break
            
        # 90도 회전
        expand_key = turn(expand_key)

    return answer