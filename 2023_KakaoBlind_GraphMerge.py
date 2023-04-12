parent = [[0, 0] * 51 for _ in range(51)]
board = [['EMPTY'] * 51 for _ in range(51)]


def find(r, c):
    if parent[r][c] == [r, c]:
        return [r, c]
    pr, pc = parent[r][c]
    return find(pr, pc)


def union(r1, c1, r2, c2):
    parent[r2][c2] = parent[r1][c1]


def update_rc(r, c, val):
    pr, pc = find(r, c)
    board[pr][pc] = val


def update_val(val1, val2):
    for i in range(1, 51):
        for j in range(1, 51):
            pr, pc = find(i, j)
            if board[pr][pc] == val1:
                board[pr][pc] = val2


def merge(r1, c1, r2, c2):
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)

    if [r1, c1] == [r2, c2]:
        return
    elif board[r1][c1] != "EMPTY":
        union(r1, c1, r2, c2)
    else:
        union(r2, c2, r1, c1)


def unmerge(r, c):
    pr, pc = find(r, c)
    msg = board[pr][pc]

    merge_list = []
    for i in range(1, 51):
        for j in range(1, 51):
            pi, pj = find(i, j)
            if parent[pi][pj] == [pr, pc]:
                merge_list.append([i, j])

    for i, j in merge_list:
        parent[i][j] = [i, j]
        if [i, j] == [r, c]:
            board[i][j] = msg
        else:
            board[i][j] = "EMPTY"


def solution(commands):
    answer = []
    for i in range(1, 51):
        for j in range(1, 51):
            parent[i][j] = [i, j]

    for c in commands:
        c = c.split(" ")
        if c[0] == "UPDATE":
            if len(c) == 4:
                update_rc(int(c[1]), int(c[2]), c[3])
            else:
                update_val(c[1], c[2])

        elif c[0] == "MERGE":
            merge(int(c[1]), int(c[2]), int(c[3]), int(c[4]))

        elif c[0] == "UNMERGE":
            unmerge(int(c[1]), int(c[2]))

        else:
            pr, pc = find(int(c[1]), int(c[2]))
            answer.append(board[pr][pc])

    return answer
