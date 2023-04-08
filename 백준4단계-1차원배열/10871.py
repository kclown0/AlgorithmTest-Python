#X보다 작은 수
A, X = map(int,input().split())
V = list(map(int,input().split()))
for i in range(A):
    if V[i] < X:
        print(V[i], end = " ")