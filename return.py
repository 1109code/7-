from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]

    for r in roads:
        graph[r[0]].append(r[1])
        graph[r[1]].append(r[0])

    ans = [-1 for _ in range(n + 1)]
    d = deque([[destination, 0]])
    ans[destination] = 0
    visited = [0 for _ in range(n + 1)]

    while d:
        cur = d.popleft()
        visited[cur[0]] = 1

        for child in graph[cur[0]]:
            if ans[child] == -1:
                ans[child] = cur[1] + 1

            if visited[child] == 0:
                d.append([child, cur[1] + 1])

    for s in sources:
        answer.append(ans[s])

    return answer
