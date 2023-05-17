dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
input_str = input()
ret = 0
for j in range(len(input_str)):
    for i in dial:            
        if input_str[j] in i:
            ret += dial.index(i)+3
print(ret)