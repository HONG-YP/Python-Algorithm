# 그리디 예제 1
# 큰 수의 법칙

# N, M, K를 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

# 정렬 후 가장 큰 수와 그 다음으로 큰수를 변수에 정의
data.sort()
first = data[N-1]
second = data[N-2]

# 결과변수 0으로 초기화
count_num = 0

# 단순 문제풀이 1
# K만큼 for문을 돌려서 M이 0이라면 break, 아니라면 count_num에 first를 계속 더하여줌
# 더해줄때마다 M에서 1을 뺌
# M이 0이라면 break, 아니라면 count_num에 second를 계속 더하여줌
# 더해줄때마다 M에서 1을 뺌
# 위의 과정을 M이 0이되어 break 될때까지 반복
while True:
    for i in range(K):
        if M == 0:
            break
        count_num += first
        M -= 1
    if M == 0:
        break
    count_num += second
    M -= 1

print(count_num)
