def reverse_integer(n):
    sign=-1 if n<0 else 1
    n*=sign
    reversed_n = int(str(n)[::-1])
    if reversed_n>2**31-1:
        return 0
    return sign*reversed_n
n= int(input())
print(reverse_integer(n))
