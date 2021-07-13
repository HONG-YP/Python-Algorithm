N = int(input())
guild = list(map(int, input().split()))

guild.sort()

group = 0
result = 0

for i in guild:
  group += 1
  if i >= group:
    result += 1
    group = 0
    
print(result)

# KeyPoint
# 1. 오름차순 정렬
# 2. 데이터가 그룹의 수보다 크거나 같은지 확인
