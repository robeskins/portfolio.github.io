import math
import numpy as np


g=9.81
#Multiple options require the same formulas so have defined them in a definition 
def Float(x):                   #Function that returns false if it can't float the input 
    try:                
        float(x)
    except:
        return False

def checkvalue(x):              #Checks input values are numerical and postive
    while ((Float(x)) == False) or float(x) <= 0:
        print('Please enter a value that is numerical and positive')
        x=input('Enter a valid number:' )
    x = float(x)
    return x

def inputs():
    y0=checkvalue((input('Enter an inital height:' )))
    m=checkvalue(input('Enter the mass of the human:'))
    return y0,m

def kinputs():
    C=checkvalue(input('Enter the drag coeffienct(1.0-1.30):'))
    p=1.2
    A=checkvalue(input('Enter the area of the sky diver:'))
    k = (C*p*A)/2
    k=float(k)
    return k

def plotheight(t,y):
    plt.plot(t,y)
    plt.xlabel('Time (s)')
    plt.ylabel('Height (m)')
    plt.show() 

def plotvelocity(t,v):
    plt.plot(t,v)
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.show() 
#This method appends values to a numpy array and returns the velcoty and the height using the analytical approach
def analytical(*args):
    if Option == 'd':           #Option d requires optional arguments to pass through the function 
        y0=args[0]
        m=args[1]
        K=args[2]
        t=args[3]
    else:
        y0,m = inputs()
        K = kinputs()
        t=checkvalue(input('Enter a time period:'))
    NumPoints = 200
    tmin = 0.0
    tmax = t
    t = np.linspace(tmin,tmax,NumPoints)
    y = np.zeros(NumPoints)
    v = np.zeros(NumPoints)
    for i in range(NumPoints):
        y[i] = y0-((m/K)*math.log(math.cosh((((K*g)/m)**0.5)*t[i])))

    for i in range(NumPoints):
        v[i] = -(((m*g)/K)**0.5)*math.tanh((((K*g)/m)**0.5)*t[i])
    return t,y,v
#Eulers method uses the previous element in a list in order to calculate the next element and appends the value to the list 
def euler(*args):
    if Option == 'e':
        r = args[0]
        y0 = args[1]
    else:
        y0,m = inputs()
        K = kinputs()
        r = K/m
    T=checkvalue((input('Enter a timestep for eulers intergration:')))
    y = [y0]
    v = [0]
    t = [0]
    i=1
    while y[-1]>=0:
            v.append(v[i-1] - T*(g + (r) * (abs(v[i-1]))*(v[i-1])))
            y.append(y[i-1] + T*v[i-1]) 
            i = i +1
#The last element was deleted because the while loop will still append the last value which is less than 0    
    del(v[-1])
    del(y[-1])
    for i in range(1,len(y)):
        t.append(t[i-1]+T)
    
    if Option == 'd':
        return t,y,v,y0,m,K
    else:
        return t,y,v
#The eulers method was used with a small timestep for accuracy. The height 'y' was used to create a list for the varying k values.
def density():
    y0,m =inputs()
    K = kinputs()
    h=7.64*10**3
    k = [(K*(math.exp(-y0/h)))]
    y = [y0]
    v = [0]
    t=[0]
    T=0.01
    i=1
    while y[-1]>=0:
        v.append(v[i-1] - T*(g + (k[i-1]/m) * (abs(v[i-1]))*(v[i-1])))
            
        y.append(y[i-1] + T*v[i-1]) 
            
        k.append((K*(math.exp(-y[i]/h))))
            
        i= i +1
        
    for i in range(1,len(y)):
            t.append(t[i-1]+T)
    return y,k,v,t

Option=''
print('\n')
while Option!= 'q':
    print('MENU:\n')
    print('---------------------------------------------------------------------- ')
    print('a)Tracking free fall using analytical predictions')
    print('b)Tracking free fall using Eulers method of intergration')
    print('c)Tracking free fall with a varying density that is dependent of height')
    print('d)Comparsion of Eulers method and the analytical approach')
    print('e)Eulers method for k/m values')
    print('q)Quit the program')
    print('-----------------------------------------------------------------------')
    print('All choices will print graphs of Velocity (m/s) and Height (m) against Time (s)')
    Option=input('Enter an option:' )
#This option will print a graph of Velcity against time and Height against time using the analytical method for a given time period decided by the user  
    if Option == 'a':
        print('You have chosen a')
        t,y,v = analytical()
        plotheight(t,y)
        plotvelocity(t,v)
        print('Final velocity',abs(v[-1]),'m/s')
        print('\n')
#This option will also print graphs using the Eulers method,where it ask the user to use a timestep for the equations      
    elif Option == 'b':
        print('You have chosen b')
        t,y,v = euler()
        plotheight(t,y)
        plotvelocity(t,v)
        print('Duration of free fall:',t[-1],'s')
        print('Final velocity:',abs(v[-1]),'m/s')
        print('\n')
#Option c will use the eulers method but with a varying density which is more realstic for real life scenario  
    elif Option == 'c':
        print('You have chosen c')
        y,ky,v,t=density()
        plotheight(t,y)
        plotvelocity(t,v)
        
        print('Time duration of fall:',t[-1],'s')
        print('Max speed reached:',abs(min(v)),'m/s')
        if abs(min(v)) >= 343:
            print('Speed of Sound was reached')
        print('')
#This option will compare Eulers and  the analytical approach with the same given conditions
    elif Option == 'd':
        tE,yE,vE,y0,m,K = euler()
        t=tE[-1]
        tA,yA,vA = analytical(y0,m,K,t)
        
        plt.plot(tE,yE,color = 'blue',label='Euler')
        plt.plot(tA,yA,color = 'red',label='Analytical')
        plt.xlabel('Time (s)')
        plt.ylabel('Height (m)')
        plt.legend(loc="upper right")
        plt.show()
        plt.plot(tE,vE,color = 'green',label='Euler')
        plt.plot(tA,vA,color= 'red',label='Analytical')
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (m/s)')
        plt.legend(loc="upper right")
        plt.show()
#This option allows the user to input a value for k/m       
    elif Option == 'e':
        y0=checkvalue(input('Enter an initial height:'))
        r=checkvalue(input('Enter a value for the ratio of k/m:'))
        t,y,v=euler(r,y0)
        plotheight(t,y)
        plotvelocity(t,v)
    
    elif Option != 'q' :
        print('This is not a valid choice, please try again:')
print('You have chosen to quit')
        
