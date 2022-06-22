rate_ad = 37550 + (7*37550.0)/100 - (10*37550.0)/100
rate_ch = 37550.0/3 + (7*(37550.0/3))/100 - (10*(37550.0/3))/100
print('no of adults and children')
a=int(input())
c=int(input())
print(a*rate_ad+c*rate_ch)
