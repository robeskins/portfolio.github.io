import math
import numpy as np
import matplotlib.pyplot as plt

G=6.67408E-11
#This function takes an input and returns false if the object cannot be converted to a float
def Float(x):                   
    try:                
        float(x)
    except:
        return False
#This function is used to catch errors made by the user if they are not numerical.
def checkvalue(x):              
    while ((Float(x)) == False):
        print('Please enter a value that is numerical')
        x=input('Enter a valid number:' )
    x = float(x)
    return x
#This function is used when the input needs to be positive and numerical. Using a while loop until this condition is met.
def checkpositive(x):              
    while ((Float(x)) == False) or float(x) <= 0:
        print('Please enter a value that is numerical and positive')
        x=input('Enter a valid number:' )
    x = float(x)
    return x
#This function is used to get parameters for the options
def parameters():
    x = checkvalue(input('Enter an initial x coordinate:'))
    y = checkvalue(input('Enter an initial y cooridante:'))
    #Option d does not require a time step as it varies with each graph created.
    if Option == 'd':
        vx = checkvalue(input('Enter an initial x velocity:'))
        vy = checkvalue(input('Enter an initial y velocity:'))
        t = checkpositive(input('Enter a time duration:'))
        return vx,vy,x,y,t
    #Option e is used to investigate how initial velocty varies the orbit so does not return vx,vy,t
    elif Option == 'e':
        h = checkpositive(input('Enter a time step:'))
        return x,y,h
        
    else:
        vx = checkvalue(input('Enter an initial x velocity:'))
        vy = checkvalue(input('Enter an initial y velocity:'))
        h = checkpositive(input('Enter a time step:'))
        t = checkpositive(input('Enter a time duration:'))
        return vx,vy,x,y,t,h
#This function creates a circular plot for different offsets and radius's
def circle(R,Sx,Sy):
    theta = np.linspace(0, 2*math.pi)
    x= []
    y=[]
    
    for i in range(0,(len(theta))):
        X = R*math.sin(theta[i])
        Y = R*math.cos(theta[i])
        X = X+Sx
        Y = Y+Sy
        x.append(X)
        y.append(Y)
    return x,y 
#accel function uses newtons law of gravitation to find the acceleration
def accel(x,y,M,M2):
    if M2 == 0:
        ax = -(G*M*x)/(((x**2)+(y**2))**(3/2))
        ay = -(G*M*y)/(((x**2)+(y**2))**(3/2))
        
    else:
        xr = 384400e3
        yr=0
        ax1 = -(G*M*x)/(((x**2)+(y**2))**(3/2))
        ay1 = -(G*M*y)/(((x**2)+(y**2))**(3/2))
        ax2 = -(G*M2*(x-xr))/((((x-xr)**2)+((y-yr)**2))**(3/2))
        ay2 = -(G*M2*(y-yr))/((((x-xr)**2)+((y-yr)**2))**(3/2))
        ax = ax1 + ax2
        ay = ay1 + ay2
    
    return [ax,ay]
#Orbit creates a list for x,y displacement,x,y veloxcity, time and energies and uses RK4 method in a for loop to append values 
def orbit(M,VX,VY,X,Y,t,h,M2):
     xr = 384400e3
     N = int(t/h)
     
     x = np.zeros(N)
     y = np.zeros(N)
     vx = np.zeros(N)
     vy = np.zeros(N)
     T = np.linspace(0,t,N)
     K = np.zeros(N)
     P = np.zeros(N)
     TE = np.zeros(N)
     
     x[0] = X
     y[0] = Y
     vx[0] = VX
     vy[0] = VY
     K[0] = (1/2)*((((VX**2)+(VY**2))**0.5)**2)
     P[0] = -(G*M)/((((X**2)+(Y**2))**0.5))
     TE[0] = K[0] + P[0]
     for i in range(0,N-1):
        k1x = vx[i]
        k1y = vy[i]
        k1vx = accel(x[i],y[i],M,M2)[0]
        k1vy = accel(x[i],y[i],M,M2)[1]
            
        k2x = vx[i]+((h*k1vx)/2)
        k2y = vy[i]+((h*k1vy)/2)
        k2vx = accel(((x[i])+((h*k1x)/2)),((y[i])+((h*k1y)/2)),M,M2)[0]
        k2vy = accel(((x[i])+((h*k1x)/2)),((y[i])+((h*k1y)/2)),M,M2)[1]
            
        k3x = vx[i]+((h*k2vx)/2)
        k3y = vy[i]+((h*k2vy)/2)
        k3vx = accel(((x[i])+((h*k2x)/2)),((y[i])+((h*k2y)/2)),M,M2)[0]
        k3vy = accel(((x[i])+((h*k2x)/2)),((y[i])+((h*k2y)/2)),M,M2)[1]
            
        k4x = vx[i]+((h*k3vx))
        k4y = vy[i]+((h*k3vy))
        k4vx = accel(((x[i])+(h*k3x)),((y[i])+(h*k3y)),M,M2)[0]
        k4vy = accel(((x[i])+(h*k3x)),((y[i])+(h*k3y)),M,M2)[1]
        
        x[i+1] = (x[i]+(h/6)*(k1x+2*k2x+2*k3x+k4x))
        y[i+1] = (y[i]+(h/6)*(k1y+2*k2y+2*k3y+k4y))
        vx[i+1] = (vx[i]+(h/6)*(k1vx+2*k2vx+2*k3vx+k4vx))
        vy[i+1] = (vy[i]+(h/6)*(k1vy+2*k2vy+2*k3vy+k4vy))
        K[i+1] = (1/2)*(((vx[i+1])**2)+((vy[i+1])**2))
        
        if Option == 'c':
            P[i+1] = (-(G*M)/((((x[i+1])**2)+((y[i+1])**2))**(0.5)))-((G*M2)/((((xr-x[i+1])**2)+((y[i+1])**2))**(0.5)))
        else:
            P[i+1] = -(G*M)/((((x[i+1])**2)+((y[i+1])**2))**(0.5))
        
        TE[i+1] = K[i+1] + P[i+1]
        
     return T,x,y,vx,vy,K,P,TE
#plt.fill is used to fill the cirle plot to represent a planet 
def plotdisplacement(x1,y1,x2,y2,*args):
    if Option == 'c':
        xM = args[0]
        yM = args [1]
        plt.fill(xM,yM)
    
    plt.fill(x1,y1)
    plt.plot(x2,y2)
    plt.axis('equal')
    plt.xlabel('x Displacement(m)')
    plt.ylabel('y Displacement(m)')
    plt.show()

def plotspeed(vx,vy):
    plt.plot(vx,vy)
    plt.xlabel('x Velocity(m/^2)')
    plt.ylabel('y Velocity(m/s^2)')
    plt.axis('equal')
    plt.show()

def plotenergy(t,P,TE,K):
    plt.plot(t,P,label = 'Potential Energy')
    plt.plot(t,TE, label = 'Total Energy')
    plt.plot(t,K, label = 'Kinetic Energy')
    plt.ylabel('Energy Per Kg (J/Kg)')
    plt.xlabel('Time (s)')
    plt.legend(loc='best')
    plt.show()

def average(x,y,vx,vy,h):
    option = input('Did the object complete a full orbit?(y/n):')
    if option == 'y': 
        Nd=nearest(x,y)
        Nv=nearest(vx,vy)
        to = (((Nd+Nv)/2)*h)/60
        print('Time for one orbit:',to,'minutes')
    else:
        print('Calcualtion can not be made')
#Nearest function finds the element in a list which is closest to the inital coordinate
def nearest(x,y):
    xN = np.zeros(len(x))
    yN = np.zeros(len(x))
    v = []
    #for loop that takes the inital value off of the remaining elements and takes the absoulte value and appends it to a list for both x and y coordiantes
    for j in range(1,len(x)):
        xN[j] = (abs(x[j]-x[0]))
        yN[j] = (abs(y[j]-y[0]))
    #the lists are then subtracted to find which coordinate is closest to the intial coordinate
    for j in range(0,(len(x))-1):
        v.append(abs(xN[j+1]-yN[j+1]))
    #Finally it returns the index of this, in order to calcualte a time.
    closest = v.index(min(v))
    return closest

Option = ''
print('\n')
while Option!= 'q':
    print('MENU:\n')
    print('---------------------------------------------------------------------- ')
    print('a)Rocket orbiting around the Earth')
    print('b)Rocket orbiting around any body of mass')
    print('c)Rocket orbitting with the earth and moon')
    print('d)One body simulating with different time steps')
    print('e)One body simulation with varying initial velocities')
    print('---------------------------------------------------------------------- ')
    
    Option=input('Enter an option:' )
    #Option a simulates a rocket around the earth
    if Option == 'a':
        M = 5.972e24
        vx,vy,x,y,t,h = parameters()
        t,x,y,vx,vy,K,P,TE = orbit(M,vx,vy,x,y,t,h,0)
        xE,yE = circle(6371000,0,0)
        
        plotdisplacement(xE,yE,x,y)
        plotspeed(vx,vy)
        plotenergy(t,P,TE,K)
        average(x,y,vx,vy,h)
    #Option b simulates a rocket around any body        
    elif Option == 'b':
        M = checkpositive(input('Enter a mass for the body:'))
        vx,vy,x,y,t,h = parameters()
        R = checkpositive(input('Enter a radius for the body'))
        t,x,y,vx,vy,K,P,TE = orbit(M,vx,vy,x,y,t,h,0)
        xE,yE = circle(R,0,0)
        
        plotdisplacement(xE,yE,x,y)
        plotspeed(vx,vy)
        plotenergy(t,P,TE,K)
        average(x,y,vx,vy,h)
    #Option c simulates a rocket with the earth and moon    
    elif Option == 'c':
         M1 = 5.972E24
         M2 = 7.34767309E22
         Re = 6371000
         Rm = 1737E3
         xr = 384400e3
         vx,vy,x,y,t,h = parameters()
         t,x,y,vx,vy,K,P,TE = orbit(M1,vx,vy,x,y,t,h,M2)
         xE,yE = circle(Re,0,0)
         xM,yM = circle(Rm,384400e3,0)
         
         option = ''
         option = input('Do you want closest approach?(y/n)')
         if option == 'y':
             xc = []
             for i in range(0,(len(x))):
                 xc.append(x[i]-xr)
             
             XC=max(xc)
             print('The closest distance to the moon is,',abs(XC),'m')
         
         plotdisplacement(xE,yE,x,y,xM,yM)
         plotspeed(vx,vy)
         plotenergy(t,P,TE,K)
         average(x,y,vx,vy,h)
    #Option d simulates mulitple time steps around the earth      
    elif Option == 'd':
        M = 5.972e24
        vx,vy,x,y,t = parameters()
        N = int(input('How many time stepped orbits would you like?:'))
        
        for i in range(0,N):
            
            hi = checkpositive(input('Enter a time step:'))
           
            ti,xi,yi,vxi,vyi,K,P,TE = orbit(M,vx,vy,x,y,t,hi,0)
            plt.plot(xi,yi,label = hi)
            plt.axis('equal')
        plt.legend(loc='upper right',title='Timestep (s)')
        plt.xlabel('x Displacement(m)')
        plt.ylabel('y Displacement(m)')
        plt.show
    #Option e simulates multiple velocity orbits
    elif Option == 'e':
        M = 5.972e24
        x,y,h = parameters()
        N = int(input('How many orbits would you like?:'))
        
        for i in range(1,N+1):
            print('Simulation',i)
            print('---------------')
            vx = checkvalue(input('Enter an intial x velocity:'))
            vy = checkvalue(input('Enter an intial y velocity:'))
            t = checkpositive(input('Enter a time duration:'))
            
            ti,xi,yi,vxi,vyi,K,P,TE = orbit(M,vx,vy,x,y,t,h,0)
            plt.plot(xi,yi,label = ('vx=',vx))
            plt.axis('equal')
        
        plt.legend(loc='best',title='Initial Velocity(m/s)')
        plt.xlabel('x Displacement(m)')
        plt.ylabel('y Displacement(m)')
        plt.show
        print('Quit the program to show graph')
    
    elif Option != 'q':
        print('This is not a valid choice, please try again:')
print('You have chosen to quit')   
