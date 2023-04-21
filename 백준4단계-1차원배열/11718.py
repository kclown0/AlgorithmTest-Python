num1 = int(input())
num_list = list(map(int,input().split()))
num2 = int(input())
count = 0
for i in range(num1):
    if num_list[i] == num2:
        count = count + 1
print(count)
