N = int(input())
K = list(map(int, input().split()))

d = [0]*100

# 다이나믹 프로그래밍 진행 (Bottom up)
d[0] = K[0]
d[1] = max(K[0], K[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2]+K[i])

print(d[N-1])
