# 그리디 예제 2
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

# 단순 문제풀이 2
# M/(K+1) -> 수열의 반복 횟수
# 반복 횟수에 K를 곱해준 것이 가장 큰 수의 반복 횟수
# 나누어 떨어지지 않는 경우를 고려하여 M%(K+1)을 더해줌
count = int(M/(K+1)) * K
print(count)
count += M % (K+1)
print(count)

# count와 first를 곱해주어 가장 큰수의 전체 합을 구해줌
# M에서 count를 뺀 값을 second와 곱해주어 그 다음 큰수의 전체 합을 구해줌
count_num += (count) * first
count_num += (M-count) * second

print(count_num)
