import math


def MyArcTan(x,N):
    y = 0

    if abs(x) <= 1:
        for n in range(0,N):
            y += (((-1)**n)/(2*n+1))*(x**(2*n+1))
            
    elif x>0:
        for n in range(0,N):
            y += (((-1)**n)/(2*n+1))*((1/x)**(2*n+1))
        y=(math.pi/2) - y
    else:
        for n in range(0,N):
            y += (((-1)**n)/(2*n+1))*((1/x)**(2*n+1))
        y= -(math.pi/2)- y
    
    return y


MyInput = '0'
while MyInput != 'q':
    print('-----------')
    print('Choice a will calculate arctan(x) using a Taylor expansion series.')
    print('Choice b will calculate the difference between the inbuilt function and MyArcTan and will form a table of values between x=2 and x=-2.')
    MyInput = input('Enter a choice, "a", "b" or "q" to quit: ')
    print('You entered the choice: ',MyInput)



    if MyInput == 'a':
        
        print('You have chosen part (a)')
        Input_x = input('Enter a value for x (floating point number): ')
        
        while (Input_x.isalpha()== True):
            print('x has to be numerical')
            Input_x = input('Enter a value for x (floating point number): ')
        
        x = float(Input_x)
        Input_N = input('Enter a value for N (positive integer): ')
        
        while (Input_N.isdigit() == False) or (int(Input_N) < 0):
            print('N has to be an integer and positive')
            Input_N = input('Enter an integer value for N (positive integer): ')
        
        N=int(Input_N)
        print('The answer is: ',MyArcTan(x,N))

    

    elif MyInput == 'b':
        print('You have chosen part (b)')
        Input_N = input('Enter a value for N (positive integer): ')
        
        while (Input_N.isdigit() == False) or (int(Input_N) < 0):
            print('N has to be a integer and positive')
            Input_N = input('Enter an integer value for N (positive integer): ')
       
        N = int(Input_N)
        print('| x  |   MyArcTan(x)     |     In Built Function Arctan(x)    |    Difference    |')
        print('--------------------------------------------------------------------')
        for x in range(-20,20):
             a= MyArcTan(x/10,N)
             b=math.atan(x/10)
             c= a-b
             print('|',str(x/10),'|' ,str(a),'|' ,str(b), '|' ,str(abs(c)), '|')


        
     
    
    elif MyInput != 'q':
        print('This is not a valid choice')

print('You have chosen to finish - goodbye.')        
