N = int(input())
count = 0
while(True):
    S = input()
    count = count + 1
    print(S[0]+S[-1])
    if count == N:
        break