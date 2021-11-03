for i in range(0,100):
    grade=float(input('Enter grade: '))
    if grade >= 70:
        print('A') 
    elif grade > 60 <= 69:
        print('B')
    elif grade > 50 <= 59:
        print('C')
    elif grade >= 40 <= 49:
        print('D')
    elif grade < 40:
        print('F')
    else:
        print('Null')


