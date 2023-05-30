A, B = input().split()

if int(B) -45 < 0 and int(A) -1 < 0:
    print(23, int(B) + 15)
elif int(B) -45 < 0 :
    print(int(A) -1, int(B) + 15)
else :
    print(int(A), int(B) -45)

# # map 쓰기
# H, M = map(int, input().split())
# if M > 44 :
#     print(H, M-45)
# elif M < 45 and H >0 :
#     print(H -1, M+15)
# else :
#     print(23, M+15)    