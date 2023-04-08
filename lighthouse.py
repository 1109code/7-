# 재귀 깊이 암기
import sys
sys.setrecursionlimit(1000000)

def light(node, tree, visited):
    visited[node] = True
    # 하위로만 내려가게
    children = [next_node for next_node in tree[node] if not visited[next_node]]
    # 기본적으로 켰을 때 껐을 때
    on, off = 1, 0
    # 자식 없으면 그냥 자신 켰거나 껐을 때(말단이니깐 0 or 1)
    if not children:
        return on, off
    
    else:
        for child in children:
            child_on, child_off = light(child, tree, visited)
            # 해당 노드를 켰을 때, 자식들을 켰을 때와 껐을 때 중 최소 값 더하기
            on += min(child_on, child_off)
            # 해당 노드를 껐을 때 ( 자식은 켰을 때임)
            off += child_on
        return on, off
        

def solution(n, lighthouse):
    # 암기
    
    answer = 0
    
    # 트리
    tree = [[] for _ in range(n + 1)]
    # 방문 확인
    visited = [0] * (n + 1)
    
    for l in lighthouse:
        tree[l[0]].append(l[1])
        tree[l[1]].append(l[0])
    
    # 첫 번째 노드를 켰을때, 껐을 때로 부터 시작
    answer = min(light(1, tree, visited))
    
    return answer