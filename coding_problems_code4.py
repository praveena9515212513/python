print("enter a number:")
n = int(input())
if(n%3==0 and n%5==0):
    print('Zoom')
elif(n%3==0):
    print('Zip')
elif(n%5==0):
    print('Zap')
else:
    print('Invaild')
