
n = int(input())
for i in range(n):
    num, s = input().split() #num과 s가 n만큼 입력을 받는다.
    str = ""
    for i in s:              #문자열만큼 곱해준다.      
        str += int(num) * i
    print(str)