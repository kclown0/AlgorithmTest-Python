A, B, C = map(int, input().split())

if A == B == C :
    print(10000+A*1000)
elif A == B or A == C:
    print(1000+ A*100)
elif B == C :
    print(1000+ B*100)
elif A > B and A > C:
    print(A*100)
elif B > C:
    print(B*100)
else :
    print(C*100)
                
#3개 같은 눈
#2개 같은 눈
#다 다른 눈