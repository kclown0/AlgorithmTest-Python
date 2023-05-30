A = input()
if int(A) % 4 == 0 :
    if int(A) % 100 != 0 or int(A) % 400 == 0 : 
        print(1)
    else :
        print(0)
else :
    print(0)        