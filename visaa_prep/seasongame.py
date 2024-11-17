n=int(input())
if 1<= n <=12:
    if n in [3,4,5]:
        print('Spring')
    elif n in [6,7,8]:
        print('Summer')
    elif n in [9,10,11]:
        print('Autum')
    else:
        print('Winter')
else:
    print('Invalid')
