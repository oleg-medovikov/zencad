import numpy as np
from numpy import pi,sin,cos,sqrt,arctan
from PIL import Image

x_max = 1000
y_max = 1000

array = np.zeros([x_max,y_max,3],dtype=np.uint8)
array.fill(255)
#array[int(0.5*x_max),:] = 0
#array[:,int(0.5*y_max)] = 0



def add_point(x,y,color):
    array[int(3*y + 0.5*y_max) , int(3*x + 0.5*x_max) ] = color
    
def circle(d, color):
    for a in range(360):
        x = d*cos(a)
        y = d*sin(a)
        add_point(x,y,color) 


    

def gear_profile(m, z):
    d   = z*m           # Диаметр делительный
    h   = 2.25*m        # Высота зуба
    ha  = m             # Высота головки
    hf  = 1.25*m        # Высота ножки
    da  = d + 2*ha      # Диаметр вершин зубьев           
    df  = d - 2*hf      # Диаметр впадин зубчатого колеса  
    db  = d*cos(pi/9)   # Диаметр основной окружности
    b   = 8*m           # Ширина венца зубчатого колеса
    Pt  = pi*m          # Окружной шаг зубьев
    St  = 0.5*Pt        # Окружная толщина зуба
    Et  = 0.5*Pt        # Окружная ширина впадины зубчатого колеса
    Qf  = 0.25*m        # Радиус кривизны переходной кривой зуба
  
    circle(d,(255,100,0))
    #circle(da,(155,0,0))
    circle(df,(0,155,0))
    circle(db,(0,0,155))
    # Еще параметров
    teta = 2*pi/z  # Угол дуги окружности, которую занимает зуб

    for k in range(z):
        a = 0
        while True:
            # Считаем точки эвольвенты первой грани
            x =  db*(cos(a) + a*sin(a))
            y = -db*(sin(a) - a*cos(a))
            # Меняем точки первой эвольвенты относительно повернутой системы координат
            turn = k*teta
            X =  x*cos(turn) + y*sin(turn)
            Y = -x*sin(turn) + y*cos(turn)
            a += pi/180
            if X**2 + Y**2 <= da**2:
                add_point(X,Y,0)
            else:
                break
                        
        d_a = arctan(-y/x)       # угол который занимает эвольвента
        d_b = 0.5*teta - d_a     # угол который занимает впадина или зуб
        a_max = a                # максимальный угол эвольвенты
        a = 0 
        while True:
            # Считаем точки вершины зуба
            x = da*cos(a)
            y = da*sin(a)
            turn = k* teta + d_a
            X =  x*cos(turn) + y*sin(turn)
            Y = -x*sin(turn) + y*cos(turn)
            a -= pi/180
            if a > -0.5*d_b*(d/da):
                add_point(X,Y,0)
            else:
                break
       
        a = a_max
        while True:
            # Считаем точки эвольвенты второй грани
            x =  db*(cos(a) + a*sin(a)) 
            y =  db*(sin(a) - a*cos(a))
            # Меняем точки первой эвольвенты относительно повернутой системы координат
            turn = k*teta + d_a + d_b
            X =  x*cos(turn) + y*sin(turn)
            Y = -x*sin(turn) + y*cos(turn)
            a -= pi/180
            if (X**2 + Y**2) > db**2 and a > 0 :
                if (X**2 + Y**2) < da**2 :
                    add_point(X,Y,0)
            else:
                break
            
        a = 0        
        while True:
            # Считаем точки эвольвенты второй грани(низ зуба)
            x = db*(cos(a) - a*sin(a))
            y = db*(sin(a) - a*cos(a))
            # Меняем точки первой эвольвенты относительно повернутой системы координат
            turn = k*teta + d_a + d_b
            X =  x*cos(turn) + y*sin(turn)
            Y = -x*sin(turn) + y*cos(turn)
            a += pi/180
            if X**2 + Y**2 >= (0.5*(df+db))**2:
                add_point(X,Y,0)
            else:
                break   
         
        # Считаем эллипс между зубами    
        d_d = arctan(y/x) # Угол, который занимает маленькая эвольвента
        r1 = 0.5*(db-df)
        r2 = 0.5*(df+db) * sin((d_b - d_d)) 
        for i in range(16,7,-1):
            i = pi*i/12
            x = r1*cos(i) + 0.5*(df+db)
            y = r2*sin(i)
            turn = (k+1)*teta  - 0.5*(d_a + d_b) 
            X =  x*cos(turn) + y*sin(turn)
            Y = -x*sin(turn) + y*cos(turn)
            add_point(X,Y,0)
       
                
        a = 0        
        while True:
            # Считаем точки эвольвенты второй грани(низ зуба)
            x =  db*(cos(a) - a*sin(a))
            y = -db*(sin(a) - a*cos(a))
            # Меняем точки первой эвольвенты относительно повернутой системы координат
            turn = (k+1)*teta 
            X =  x*cos(turn) + y*sin(turn)
            Y = -x*sin(turn) + y*cos(turn)
            a += pi/180
            if X**2 + Y**2 >= (0.5*(df+db))**2:
                add_point(X,Y,0)
            else:
                break  
    
gear_profile(16,6)

img = Image.fromarray(array)
img.save('test.png')
img  
