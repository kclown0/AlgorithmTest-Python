input_num = int(input())
for i in range(input_num):
    s = list(map(int,input().split()))
    s_mean = sum(s[1:])/s[0]
    count = 0

    for i in range(1,len(s)):
        if s[i] > s_mean: 
            count += 1
    result = (count/s[0])*100
    print(f'{result:.3f}%')