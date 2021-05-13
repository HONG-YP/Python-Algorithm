# 숫자 카드 게임

N, M = map(int, input().split())

result = 0

for i in range(N):
    arr = list(map(int, input().split()))
    min_data = min(arr)

    result = max(result, min_data)

print(result)
