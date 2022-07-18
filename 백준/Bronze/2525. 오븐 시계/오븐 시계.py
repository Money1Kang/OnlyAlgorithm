A, B = map(int, input().split())
alam = int(input())

A += alam // 60
B += alam % 60

if B >= 60:
    A += 1
    B -= 60
    
if A >= 24:
    A -= 24

    
print(A, B)