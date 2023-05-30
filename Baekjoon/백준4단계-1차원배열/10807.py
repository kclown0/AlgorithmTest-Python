N = int(input()) # N = 8 # 배열의 길이 
V = list(map(int, input().split())) # V = [1,2,3,4,5, 3, 3, 3] #배열
n = int(input()) # n = 3 #배열에서 찾는 정수

count = 0
for i in range(N):
    if V[i] == n:
        count = count +1
    else :
        count = count
print(count)

#검색결과
# n = int(input())
# n_list = list(map(int, input().split()))
# v = int(input())

# print(n_list.count(v))