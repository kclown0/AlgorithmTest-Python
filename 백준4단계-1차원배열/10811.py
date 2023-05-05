N,M = map(int, input().split())
basket = []

for i in range(N):   
    basket.append(i+1)

for i in range(M):
    n, m = map(int, input().split())
    
    result = basket[n-1:m]
    result.reverse()
    basket[n-1:m] = result

print(*basket)