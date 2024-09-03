from collections import deque


def rotate(arr):
    # 1일 경우 시계방향, -1일 경우 반시계방향, 0 일경우 가만히
    for i in range(4):
        if arr[i] != 0:
            if arr[i] == 1:
                deques[i].appendleft(deques[i].pop())
            elif arr[i] == -1:
                deques[i].append(deques[i].popleft())


def rotate_topni(topni, dr):
    # 톱니바퀴가 도는 방향을 표시, 1 : 시계 -1 : 반시계 0 : 움직임X
    change = [0, 0, 0, 0]
    '''
    해당 문제는 1번 톱니바퀴가 돌아간다고 했을때 2번 톱니바퀴가 돌아가는 기준은 1번 톱니바퀴가 돌아가기 전
    맞닿아 있는 톱니의 표시가 다르면 2번 톱니바퀴도 돌아간다. 그렇기 때문에 톱니바퀴들을 돌리기 전에
    미리 돌려야 되는 톱니바퀴를 찾는 것이 필요함
    '''
    # 1번 톱니바퀴의 경우
    if topni == 1:
        change[0] = dr
        # 2번 톱니바퀴를 돌려야 하는지 판별
        if t1[2] != t2[6]:
            change[1] = dr*(-1)
            # 2번 톱니바퀴를 돌렸으니 3번 톱니바퀴도 돌려야 하는지 확인 필요
            if t2[2] != t3[6]:
                change[2] = dr
                # 3번을 돌렸으니 4번도 확인 필요
                if t3[2] != t4[6]:
                    change[3] = dr*(-1)

    # 2번 톱니바퀴의 경우
    elif topni == 2:
        change[1] = dr
        # 1번 돌려야하는지 확인
        if t2[6] != t1[2]:
            change[0] = dr*(-1)
        # 3번 돌려야 하는지 확인
        if t2[2] != t3[6]:
            change[2] = dr*(-1)
            # 3번 돌렸으니 4번도 돌려야하는지 확인
            if t3[2] != t4[6]:
                change[3] = dr

    # 3번 톱니바퀴의 경우
    elif topni == 3:
        change[2] = dr
        # 2번 확인
        if t3[6] != t2[2]:
            change[1] = dr*(-1)
            # 1번 확인
            if t2[6] != t1[2]:
                change[0] = dr
        # 4번 확인
        if t3[2] != t4[6]:
            change[3] = dr*(-1)

    # 4번 톱니바퀴의 경우
    elif topni == 4:
        change[3] = dr
        # 3번 확인
        if t4[6] != t3[2]:
            change[2] = dr*(-1)
            # 2번 확인
            if t3[6] != t2[2]:
                change[1] = dr
                # 1번 확인
                if t2[6] != t1[2]:
                    change[0] = dr*(-1)
    # 톱니를 돌림
    rotate(change)

# 덱 사용해서 톱니바퀴의 움직임 구현

deques = []
for _ in range(4):
    deques.append(deque(input()))

t1, t2, t3, t4 = deques

n = int(input())

for _ in range(n):
    topni, dr = map(int, input().split())
    rotate_topni(topni, dr)

# 정답
ans = int(t1[0]) * 1 + int(t2[0])*2 + int(t3[0])*4 + int(t4[0])*8

print(ans)