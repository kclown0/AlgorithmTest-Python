X = int(input())
N = int(input())

sum = 0
for i in range(N):
    a, b = map(int, input().split())
    sum += a*b
#     print(sum) ex) N =2 , 200 5 >>> 1000 
#                           100 5 >>> 1500
# print(sum) >>> 1500  
if sum == X:
    print('Yes')
else:
    print('No')
