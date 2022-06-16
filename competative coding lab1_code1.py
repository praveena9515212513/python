for i in range(500):
    print('''Enter the following details:
    Branch of study,
    Score,
    Course fee.''')
    branch = input()
    score = int(input())
    fee = int(input())
    if(branch == 'arts'):
        if(score>=90 and score%2!=0):
            scholarship = 50
        elif(score>=90):
            scholarship = 50
        elif(score%2!=0):
            scholarship = 5
        else:
            scholarship = 0
    elif(branch == 'engineering'):
        if(score>85 and score%7==0):
            scholarship = 50
        elif(score>85):
            scholarship = 50
        elif(score%7==0):
            scholarship = 5
        else:
            scholarship = 0
    else:
        scholarship = 0
        
    scholarship_amount=(fee*scholarship)/100
    final_fee = fee - scholarship_amount

    print(final_fee)

        
