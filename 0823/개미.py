# 격자 크기 WxH
W, H = map(int, input().split())

# 시작 좌표 (x,y)
x, y = map(int, input().split())

# 이동 시간,
t = int(input())

end_x = 0
end_y = 0
# 가로 계산
tmp = (x+t)//W
# 홀수일때 -> 줄어드는중
if tmp % 2 == 1:
    end_x = W - (x+t) % W
else:
    end_x = (x+t) % W

# 세로 계산
tmp_y = (y+t)//H

if tmp_y%2 == 1:
    end_y = H - (y+t) % H
else:
    end_y = (y+t) % H

print(end_x, end_y)