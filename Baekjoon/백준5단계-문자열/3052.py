n = []
for i in range(10):
    n.append(int(input())%42)
# print(len(n))
# print(n)

count = set(n) #SET 중복허용하지 않음
print(len(count))
# print(n)           