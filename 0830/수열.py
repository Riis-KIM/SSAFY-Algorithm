# 날짜 수, 연속 날짜 수
N, K = map(int, input().split())

arr = list(map(int, input().split()))

firstsum = sum(arr[:K])
maxsum = firstsum
# 연속된 날짜 수 만큼 더해 최대값 저장
for i in range(1, N-K+1):
    firstsum = firstsum - arr[i-1] + arr[i+K-1]
    maxsum=max(maxsum, firstsum)

print(maxsum)