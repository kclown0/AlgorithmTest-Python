#최대값
count = 0
count2 = 0
n = []
while(True):
    N = int(input())
    n.append(N)
    count = count + 1
    if count == 9:
        break
    
while(True):
    if n[count2] == max(n):
        break
    else :
        count2 = count2 + 1

print(max(n))
print(count2 + 1)