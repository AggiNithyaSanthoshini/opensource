def count_divisible(n):
    count=0
    for i in range(1,n+1):
        if i % 3 == 0 or i % 5 ==0:
            count+=1
    return count
n=int(input())
print(count_divisible(n))
