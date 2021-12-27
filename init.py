print('assss')
from scientific_calculator import tower
from simple_calculator import first


while True:
    x = input("Scientific Calculator(c) or Simple Calculator(s)?")
    if(x.lower() == 's' or x.lower() == 'c'):
        if(x.lower() == 's'):
            first()
        else:
            tower()
    else:
        print('Wrong choice try again')