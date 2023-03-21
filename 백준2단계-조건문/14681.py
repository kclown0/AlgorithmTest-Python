A = input()
B = input()

if int(A) > 0 and int(B) > 0 :
    print(int(1))
elif int(A) < 0 and int(B) > 0 :
    print(int(2))
elif int(A) < 0 and int(B) < 0 :
    print(int(3))
else :
    print(int(4)) 