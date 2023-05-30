n = int(input())
v = list(map(int,input().split()))
sum = 0
for i in range(n):
    sum = sum +(v[i]/max(v))
print(sum/n*100)