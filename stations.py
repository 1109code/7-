from math import ceil

def solution(n, stations, w):
    answer = 0

    # 커버 범위
    cover_range = w * 2 + 1
    # 안닿는 곳
    start = 1
    # 기 설치된 기지국 순회
    for st in stations:
        # 해당 기지국 이전에 설치해야 하는 기지국 수 계산
        cnt = ceil(((st - w) - start) / cover_range)
        # 왼쪽이 이미 다 커버 된 곳일 때
        if cnt > 0:
            answer += cnt
        # 다음 기지국 커버 안된 시작 점
        start = st + w + 1

    # 오른쪽에 기지국 남아 있으면
    if n >= start:
        answer += ceil((n - start + 1) / cover_range)

    return answer