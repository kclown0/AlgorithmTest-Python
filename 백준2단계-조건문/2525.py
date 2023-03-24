H, M = map(int, input().split())
C = int(input())

if M + C < 60 :
    print(H, M+C)
elif H+(M+C)//60 > 23 :
    print(H+(M+C)//60 - 24, (M+C)%60)    
else :
    print(H+(M+C)//60, (M+C)%60)