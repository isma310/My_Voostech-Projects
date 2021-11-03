for i in range(0,100):
    grade=float(input('Enter grade: '))
    if grade >= 70:
        print('A:EXCELLENT') 
    elif grade > 60 <= 69:
        print('B:VERY GOOD')
    elif grade > 50 <= 59:
        print('C:GOOD')
    elif grade >= 40 <= 49:
        print('D:PASS')
    elif grade < 40:
        print('F:FAIL')
    else:
        print('Null')


