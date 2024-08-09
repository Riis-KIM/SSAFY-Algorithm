T=int(input())

arr=[]
for _ in range(T):
    arr.append(list(map(int, input().split())))

# 정렬
arr.sort()
arr_max,arr_max_index=0,0

# 최댓값 인덱스, 최대값 저장
for i in range(T):
    if arr_max<arr[i][1]:
        arr_max=arr[i][1]
        arr_max_index=i

#초기화
high_x,high_y=arr[0][0],arr[0][1]
result=0

# 최대값 왼쪽 영역 계산
for i in range(1,arr_max_index+1):
    if high_y<arr[i][1]:
        result+=(arr[i][0]-high_x)*high_y
        high_x,high_y=arr[i][0],arr[i][1]

# 최대값 추가
result+=arr[arr_max_index][1]

# 최대값 초기화
high_x,high_y= arr[T - 1][0], arr[T - 1][1]
# 최대값 오른쪽 영역 계산
for i in range(T - 1, arr_max_index - 1, -1):
    if high_y<=arr[i][1]:
        result+=(high_x-arr[i][0])*high_y
        high_x,high_y=arr[i][0],arr[i][1]

print(result)