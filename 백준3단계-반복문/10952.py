import sys

while True: # 1(True)면 무한 반복
    A,B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    else:
        print(A+B)
    