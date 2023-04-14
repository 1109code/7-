from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    for r in roads:
        graph[r[0]].append(r[1])
        graph[r[1]].append(r[0])

    ans = [0 for _ in range(n + 1)]

    for s in sources:
        d = deque([])
        visited = [0 for _ in range(n + 1)]

        d.append([s, 0])
        flag = 0

        while d:
            cur = d.popleft()
            visited[cur[0]] = 1

            if cur[0] == destination:
                flag = 1
                answer.append(cur[1])
                ans[s] = cur[1]
                break

            # if ans[cur[0]] > 0:
            #     flag = 1
            #     ans[s] = cur[1] + ans[cur[0]]
            #     break

            for path in graph[cur[0]]:
                if visited[path] == 0 and ans[path] != -1:
                    d.append([path, cur[1] + 1])
                    visited[path] = 1

        if flag == 0:
            answer.append(-1)
            # ans[s] = -1

        # answer.append(ans[s])
    # print(ans)

    return answer
