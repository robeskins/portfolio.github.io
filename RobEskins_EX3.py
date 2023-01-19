import math
import matplotlib.pyplot as plt

def Float(x):                   
    try:                
        float(x)
    except:
        return False
def Int(x):
    try:                
        int(x)
    except:
        return False
#This function checks the input is numerical and postive
def checkvalue(x):              
    while ((Float(x)) == False) or float(x) <= 0:
        print('Please enter a value that is numerical and positive')
        x=input('Enter a valid number:' )
    x = float(x)
    return x
#Function checks if the input is an integer,postive and it is even
def checkN(x):
    while ((Int(x)) == False) or (int(x)) <= 0 or (int(x) % 2 != 0):
        print('Please enter a value that is an even positive integer:')
        x=input('Enter a valid number:')
    x=int(x)
    return x
#This function checks that the input is numerical
def checkfloat(x):
    while ((Float(x)) == False):
        print('Please enter a value that is numerical and positive')
        x=input('Enter a valid number:' )
    x = float(x)
    return x
#This function checks if the input is a integer and is postive
def checkn(x):
    while ((Int(x)) == False) or (int(x)) <= 0:
        print('Please enter a value that is an positive integer:')
        x=input('Enter a valid number:')
    x=int(x)
    return x

def Fresnel(x,j,z,k):
    E = complex(math.cos((k/(2*z))*((j-(x))**2)),(math.sin((k/(2*z))*((j-(x))**2))))
    return E

def parameters():
    L = checkvalue(input('Enter a value for the wavelength:'))
    k=(2*math.pi)/L
    n = checkn(input('Enter a value for how many points divide up the screen:'))
    x1 = checkfloat(input('Enter a value for the lower limit in the x direction:'))
    x2 = checkfloat(input('Enter a value for the upper limit in the x direction:'))
    x = checkvalue(input('Enter a value for the range on the screen in the x plane:'))
   
    if Option == 'a':
        z = checkvalue(input('Enter a value for the distance to the screen:'))
        N = checkN((input('Enter a value for the interval of intergration:')))
        hx = (x2-x1)/N
        return k,z,x1,x,N,hx,n,x2,L
    
    elif Option == 'b':
        N = checkN((input('Enter a value for the interval of intergration:')))
        hx = (x2-x1)/N
        return k,x1,x,N,hx,n
    
    elif Option == 'c':
        z = checkvalue(input('Enter a value for the distance to the screen:'))
        return k,x1,x,n,x2,z
    
    elif Option == 'd':
        y1 = checkfloat(input('Enter a value for the lower limit in the y direction:'))
        y2 = checkfloat(input('Enter a value for the upper limit in the y direction:'))
        y = checkvalue(input('Enter a value for the range on the screen in the y plane:'))
        z = checkvalue(input('Enter a value for the distance to the screen:'))
        N = checkN((input('Enter a value for the interval of intergration:')))
        hy = (y2-y1)/N
        hx = (x2-x1)/N
        return k,z,x1,x,y1,y,N,hx,hy,n
    
def simpson(x,j,z,k,N,h):
    E=0
    for i in range(0,N+1):
            if (i == 0) or (i == N):
                E += Fresnel(x+i*h,j,z,k)
            
            elif (i % 2 == 0):
                E += 2*Fresnel(x+i*h,j,z,k)
                
            elif (i % 2 != 0):
                E += 4*Fresnel(x+i*h,j,z,k)
    return E
#This function runs the screen coordinates x through the simpsons function and appends to a list for intensity and x 
def onedfresnel(x1,z,k,N,hx,n):
    I = []
    X = []
    j = - x
    while j<=x:
        E = simpson(x1,j,z,k,N,hx)
        E = (hx/3)*(k/(2*math.pi*z))*E
        X.append(j)      
        j += x/n    
        E = (abs(E))**2
        I.append(E)
    return I,X
#This functions runs both x and y coordinates through the simpsons function and returns the intensity 
def twodfresnel(k,z,x1,x,y1,y,N,hx,hy,n,d):
    X=[]
    Y=[]
    a = -y
    I=[]
    while a<=y:
        j=-x
        Et=[]
        
        while j<=x:
            Ex = simpson(x1,j,z,k,N,hx)
            Ey = simpson(y1,a,z,k,N,hy)
            E = (hy/3)*Ey*(hx/3)*Ex
            E = (abs((k/(2*math.pi*z))*E))**2
            if d=='y':
                E = math.log(E)
            Et.append(E)
            j += x/n
        I.append(Et)
        a += y/n
    
    p = -x
    a = -y
   
    while p<=x:
        a += y/n
        p += x/n
        X.append(p)
        Y.append(a)
        
    return X,Y,I
        
Option = ''
print('\n')
while Option!= 'q':
    print('MENU:\n')
    print('---------------------------------------------------------------------- ')
    print('a)1D Fresnel Diffraction')
    print('b)1D Fresnel Diffraction with varying distance')
    print('c)1D Fresnel Diffraction with varying N')
    print('d)2D Fresnel Diffraction')
    print('q)Quit the program')
    
    print('---------------------------------------------------------------------- ')
    Option=input('Enter an option:' )
#Option a performs 1D diffraction
    if Option == 'a':
        k,z,x1,x,N,hx,n,x2,L= parameters()
        I,X = onedfresnel(x1,z,k,N,hx,n)
        plt.plot(X,I)
        plt.xlabel('Screen Distance, x')
        plt.ylabel('Relative Intensity')
        plt.xticks(rotation='vertical')
        plt.show()
#Option b performs 1D diffraction for mulitple distances        
    elif Option == 'b':
        k,x1,x,N,hx,n= parameters()
        Z = int(input('How many graphs would you like:'))
        for i in range(0+1,Z+1):
            print('Screen Distance',i)
            print('---------------------------------------------------------------------- ')
            z=checkvalue(input('Enter a value for the distance to the screen:'))
            Ii,Xi = onedfresnel(x1,z,k,N,hx,n)
            plt.plot(Xi,Ii,label = z)
        plt.legend(title='Screen Distance (m)')
        plt.xlabel('Screen Distance, x')
        plt.ylabel('Relative Intensity')
        plt.show()
#Option c performs 1D diffraction for mulitple N values       
    elif Option == 'c':
        k,x1,x,n,x2,z = parameters()
        Z = int(input('How many graphs would you like:'))
        for i in range(0+1,Z+1):
            print('N Value',i)
            print('---------------------------------------------------------------------- ')
            N=int(input('Enter a value for the interval:'))
            hx = (x2-x1)/N
            Ii,Xi = onedfresnel(x1,z,k,N,hx,n)
            plt.plot(Xi,Ii,label = N)
        plt.legend(title='N Value')
        plt.xlabel('Screen Distance, x')
        plt.ylabel('Relative Intensity')
        plt.show()
#Option d performs 2D diffraction    
    elif Option == 'd':  
        Decsion = ''
        Decsion = input('Would you like a logarithmic scale?(y/n):')
        k,z,x1,x,y1,y,N,hx,hy,n = parameters()
        print('Please Wait...')
        X,Y,I = twodfresnel(k,z,x1,x,y1,y,N,hx,hy,n,Decsion)
        plt.pcolormesh(X,Y,I)
        plt.xlabel('X Screen Distance')
        plt.ylabel('Y Screen Distance')
        plt.xticks(rotation='vertical')
        plt.colorbar()
        plt.show()
        
    elif Option != 'q' :
        print('This is not a valid choice, please try again:')
print('You have chosen to quit')
