# def update_pos(r, c, value, board, con):
#     if con[r][c]:
#         for c in con[r][c]:
#             board[c[0]][c[1]] = value
#     else:
#         board[r][c] = value
#     return board


# def update_val(val1, val2, board, con):
#     for i in range(1, 51):
#         for j in range(1, 51):
#             if board[i][j] == val1:
#                 if con[i][c]:
#                     for c in con[r][c]:
#                         board[c[0]][c[1]] = val2
#                 else:
#                     board[c[0]][c[1]] = val2
#     return board


# def merge(r1, c1, r2, c2, board, con):
#     for c in con[r1][c1]:
#         con[c[]]

#     con[r1][c1].append([r2, c2])
#     con[r2][c2].append([r1, c1])

#     if board[r1][c1]:
#         board[r2][c2] = board[r1][c1]
#     else:
#         board[r1][c1] = board[r2][c2]


# def solution(commands):
#     board = [[""] * 51 for _ in range(51)]
#     connected = [([] for _ in range(51)) for _ in range(51)]
#     answer = []

#     for c in commands:
#         if c[0] == "UDPATE":
#             if len(c) == 4:
#                 board = update_pos(c[1], c[2], c[3], board, connected)
#             else:
#                 board = update_val(c[1], c[2], board, connected)
#         elif c[0] == "MERGE":
#             board = merge(c[1], c[2], c[3], c[4], board, connected)
#         # elif c[0] == "UNMERGE":
#             # board = unmerge(c[1], c[2], board, connected)
#         else:
#             print(board[c[1]][c[2]])

#     return answer
