
# 문자열을 하나씩 나눠서 리스트를 만든다.
str_input = input()
char_list= []
for i in range(len(str_input)):
    char_list.append(str_input[i])

# 알파벳 리스트를 만든다.(검색)
alphabet_list = [chr(i) for i in range(ord('a'),ord('z')+1)]

# 문자열 리스트의 인덱스 위치에 맞게 알파벳 리스트의 값을 변경해준다.
for i in range(len(char_list)):
    for j in range(len(alphabet_list)):
        if char_list[i] == alphabet_list[j]:
            alphabet_list[j] = char_list.index(char_list[i])

# 변경되지 않은 알파벳 리스트의 값은 -1로 변경해준다.
for i in range(len(alphabet_list)):
    if type(alphabet_list[i]) == str:
        alphabet_list[i] = -1

print(alphabet_list)