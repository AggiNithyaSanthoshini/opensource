X,Y,Z=map(int,input().split())
time = X*Y
available_time = Z * 1440
if time <= available_time:
    print("YES")
else:
    print("NO")
