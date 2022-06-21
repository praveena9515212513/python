print('enter numbers')
a= int(input())
b= int(input())
c= int(input())
if(c==7):
    print(-1)
elif(b==7):
    print(c)
elif(a==7):
    print(b*c)
else:
    print(a*b*c)

------------------------------------------------------------
------------------------------------------------------------
                    (or)
if a==7:
    if(b==7):
        if(c==7):
            print(-1)
        else:
            print(c)
    else:
        if(c==7):
            print(-1)
        else:
            print(b*c)
else:
    if(b==7):
        if(c==7):
            print(-1)
        else:
            print(c)
    else:
        if(c==7):
            print(-1)
        else:print(a*b*c)

                    
    
