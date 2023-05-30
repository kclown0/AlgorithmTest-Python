
# 검색
list_word = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
for i in list_word:
    word = word.replace(i, '1')
print(len(word))