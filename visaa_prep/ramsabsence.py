def max_consecutive_absent(n,attendence):
    max_absent=0
    current_absent=0
    for day in attendence:
            if day==0:
                current_absent+=1
                max_absent=max(max_absent,current_absent)
            else:
                current_absent=0
    return max_absent
n=int(input())
attendence=list(map(int,input().split()))
print(max_consecutive_absent(n,attendence))
