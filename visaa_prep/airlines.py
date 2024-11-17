def calculate_additional_planes(X,N):
    required_planes=(N+99)//100
    return max(required_planes - X,0)
X,N=map(int,input().split())
print(calculate_additional_planes(X,N))
