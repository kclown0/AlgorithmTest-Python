N,M = map(int, input().split())
basket = []

for i in range(N):   
    basket.append(i+1)

for i in range(M):
    n, m = map(int, input().split())
    basket[n-1], basket[m-1] = basket[m-1], basket[n-1]

print(*basket) ## 리스트 [] 없애야함!!!!
