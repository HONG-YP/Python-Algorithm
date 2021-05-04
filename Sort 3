N, K = map(int, input().split())
A_input = list(map(int, input().split()))
B_input = list(map(int, input().split()))

A_arr = sorted(A_input)
B_arr = sorted(B_input, reverse = True)

for i in range(K):
    if A_arr[i] < B_arr[i]:
        A_arr[i], B_arr[i] = B_arr[i], A_arr[i]
    else:
        break

print(sum(A_arr))
