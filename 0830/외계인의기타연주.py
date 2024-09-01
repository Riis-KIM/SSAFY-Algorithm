import sys

# 음의 수 N,  프렛 수 P
N, P = map(int, input().split())

guitar = {}
cnt = 0

for _ in range(N):
    # 기타줄, 프렛
    a, b = map(int,sys.stdin.readline().split())
    # 기타줄 확인
    if not guitar.get(a):
        guitar.setdefault(a, [b])
        cnt += 1
    # 플렛에 손가락 추가
    if b not in guitar[a]:
        guitar[a].append(b)
        cnt += 1
    # 최대 프렛이 아닐경우 --> 큰 숫자 삭제 필요
    tmp = []
    for item in guitar[a]:
        if item > b:
            tmp.append(item)

    for item in tmp:
        guitar[a].remove(item)
        cnt += 1

print(cnt)
