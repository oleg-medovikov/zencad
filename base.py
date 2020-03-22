from zencad import *
from concurrent import futures
import zencad.assemble
import time

nema = 17
#======================Ардуино==========================
x05=0.5*53.4
y05=0.5*68.6
def plate(f):
    pnts=[[ x05, y05],
                [-x05, y05],
                [-x05,-y05+2.53 ],
                [-x05+2.5, -y05+2.53],
                [-x05+5, -y05],
                [ x05-15.5, -y05 ],
                [ x05-15.5+2.54, -y05+2.54],
                [ x05-1.52, -y05+2.54],
                [ x05, -y05+2.54+1.52]]
    if (f == 1):
        m=polygon(pnts=pnts, wire=False) \
                - circle(r=1.6).translate( x05-3.8, y05-15.23, 0)\
                - circle(r=1.5).translate(-x05+3.8, y05-15.23, 0)\
                - circle(r=1.5).translate(-x05+7.63, -y05+2.53 , 0)\
                - circle(r=1.5).translate(-x05+35.56, -y05+2.53, 0)
    else:
        m=polygon(pnts=pnts, wire=False) \
                - circle(r=1.6).translate( x05-3.8, y05-13.4, 0)\
                - circle(r=1.5).translate(-x05+3.8, y05-13.4, 0)
    return linear_extrude(proto=m, vec=(0,0,2),center=False)
def usb():
    pnts=[[ 5,0,-4],
                [ 5,0, 2],
                [ 2.5,0, 4],
                [-2.5,0, 4],
                [-5,0, 2],
                [-5,0,-4]]
    o=polygon(pnts=pnts,wire=False) \
                - rectangle(6,3,center=True).rotateX(deg(90))
    m=box([12,16,10],center=True) \
                - linear_extrude(proto=o,vec=(0,8,0),center=True).moveY(4)
    return m.translate(x05-16,y05,7)
def pit():
    m= box([9,3.3,11],center=True) \
                + cylinder(r=4.5, h=10,center=True).rotateX(deg(90)).translate(0,-5,1)\
                + box([9,10,5],center=True).translate(0,-5,-3)\
                - cylinder(r=3, h=10,center=True).rotateX(deg(90)).translate(0,-3,1)
    return m.translate(-x05+9,y05,7.5)
def pit2():
    m= cylinder(r=0.5, h=9,center=True).rotateX(deg(90))
    return m.translate(-x05+9,y05-4,8.5)
def knopka():
    m= box([6.4,6.4,2],center=True)
    return m.translate(x05-5,y05-4.5,3)
def knopka2():
    m= cylinder(r=1.5,h=1)
    return m.translate(x05-5,y05-4.5,4)
def micro():
    m= box([7,35,4],center=True)
    return m.translate(-x05+16.8,-y05+22,5)
def micro2():
    m= box(1)
    for i in range(14):
        m= m + box([10,1,1],center=True).moveY(i*2.4)
    return m.translate(-x05+16.8,-y05+7,3)
def raz1():
    m=box([2.5,2.5,8],center=True).up(4)\
                - box([1.5,1.5,8],center=True).up(4)
    m1=box(0.1)
    m2=box(0.1)
    for i in range(15):
        m1 = m1 + m.translate(-x05+3,y05-27.5 - i*2.5,2)\
                    - m.translate(-x05+3,y05-27.5 - 8*2.5,2)
    for i in range(19):
        m2 = m2 + m.translate(x05-3,-y05+5 + i*2.5,2)\
                    - m.translate(x05-3,-y05+5 + 8*2.5,2)
    return m1 + m2
def shtik():
    m=box([1,1,8],center=True).up(4)
    m1 = box(0.1)
    m2 = box(0.1)
    m3 = box(0.1)
    m4 = box(0.1)
    m5 = box(0.1)
    m6 = box(0.1)
    for i in range(13):
        m1 = m1 + m.translate(-x05+3,-y05+6+i*2.5,-7)\
                    - m.translate(-x05+3,-y05+6+6*2.5,-7)
    for i in range(17):
        m2 = m2 + m.translate(x05-3,-y05+5+i*2.5,-7)\
                    - m.translate(x05-3,-y05+5+8*2.5,-7)
    for i in range(13):
        m3 = m3 + m.translate(-x05+6 +i*2.5,-y05+3,2)\
                    + m.translate(-x05+6 +i*2.5,-y05+5.5,2)
    for i in range(4):
        m4 = m4 + m.translate(x05-7 -i*2.5,-y05+6,2)\
                    + m.translate(x05-7 -i*2.5,-y05+8.5,2)
    for i in range(4):
        m5 = m5 + m.translate(x05-24 -i*2.5,y05-2,2)\
                    + m.translate(x05-24 -i*2.5,y05-4.5,2)\
                    + m.translate(x05-24 -i*2.5,y05-7,2)\
                    + m.translate(x05-24 -i*2.5,y05-9.5,2)
    for i in range(6):
        m6 = m6 + m.translate(x05-21.5 +i*2.5,y05-9.5,2)\
                    + m.translate(x05-21.5 +i*2.5,y05-12,2)
    return m1 + m2 + m3 + m4 + m5 + m6
def kleim():
    pnts=[[ 4,0, 0],
                [ 4,0, 5.6],
                [ 2.6,0, 10],
                [-2.6,0, 10],
                [-4,0, 5.6],
                [-4,0, 0]]
    o=polygon(pnts=pnts,wire=False)
    m=linear_extrude(proto=o,vec=(0,10,0),center=True)\
        - cylinder(r=1.7,h=10).moveY(2.5)\
        - cylinder(r=1.7,h=10).moveY(-2.6)\
        - box(4).translate(-4,0.5,1)\
        - box(4).translate(-4,-4.5,1)

    return m.translate(-x05+14,y05-5,2)
def raz2():
    m=box([2.5,2.5,8],center=True).up(4)\
                - box([1.5,1.5,8],center=True).up(4)
    m1=box(0.1)
    for i in range(8):
        m1 = m1 + m.translate(-x05+5.4+i*2.5,y05-16,2)\
                    + m.translate(-x05+5.4+i*2.5,y05-29,2)\
                    + m.translate( x05-5.4-i*2.5,y05-16,2)\
                    + m.translate( x05-5.4-i*2.5,y05-29,2)\
                    + m.translate( x05-5.4-i*2.5,-y05+19,2)\
                    + m.translate( x05-5.4-i*2.5,-y05+31,2)\
                    + m.translate(-x05+5.4+i*2.5,-y05+19,2)\
                    + m.translate(-x05+5.4+i*2.5,-y05+31,2)
    return m1
def kond():
    m= cylinder(r=4,h=12,center=True).rotateY(deg(90))\
                .translate(x05-12,y05-22.5,6)\
                + cylinder(r=4,h=12,center=True).rotateY(deg(90))\
                .translate(x05-12,-y05+25,6)\
                + cylinder(r=4,h=12,center=True).rotateY(deg(90))\
                .translate(-x05+17,y05-22.5,6)\
                + cylinder(r=4,h=12,center=True).rotateY(deg(90))\
                .translate(-x05+17,-y05+25,6)
    return m
def drivers():
    m= box([20,15,3.6],center=True).translate(x05-14,y05-22.5,11.8)\
                + box([20,15,3.6],center=True).translate(-x05+14,y05-22.5,11.8)\
                + box([20,15,3.6],center=True).translate(x05-14,-y05+25,11.8)\
                + box([20,15,3.6],center=True).translate(-x05+14,-y05+25,11.8)
    return m
def radiators():
    m = box([9,8,2],center=True)
    for i in range(5):
        m = m + box([1,8,2.6],center=True).translate(i*2 - 4,0,2.3)
    m = m.translate(x05-14,y05-22.5,13.8)\
                + m.translate(-x05+14,y05-22.5,13.8)\
                + m.translate(x05-14,-y05+25,13.8)\
                + m.translate(-x05+14,-y05+25,13.8)
    return m


arduino = zencad.assemble.unit()
arduino.add_shape(plate(1), color(0,0.31,0.5))
arduino.add_shape(usb(), color(0.8,0.8,0.8))
arduino.add_shape(pit(), color(0.1,0.1,0.1))
arduino.add_shape(pit2(), color(0.8,0.8,.8))
arduino.add_shape(knopka(), color(0.8,0.8,.8))
arduino.add_shape(knopka2(), color(0.8,0.2,0.2))
arduino.add_shape(micro(), color(0.1,0.1,0.1))
arduino.add_shape(micro2(), color(0.8,0.8,0.8))
arduino.add_shape(raz1(), color(0.1,0.1,0.1))

shild = zencad.assemble.unit()
shild.add_shape(plate(0),color(0.8,0.1,0.1))
shild.add_shape(shtik(),color.yellow)
shild.add_shape(knopka(), color(0.8,0.8,.8))
shild.add_shape(knopka2(), color(0.2,0.2,0.2))
shild.add_shape(kleim(), color.blue)
shild.add_shape(raz2(),color.white)
shild.add_shape(kond(), color(0.2,0.2,0.2))
shild.add_shape(drivers(),color(0.8,0.1,0.1))
shild.add_shape(radiators(), color(0.8,0.8,.8))


#==============================================================
#=================Концевик==============================
def kontsevic():
    def telo():
        m=box((20,6.3,10),center=True)\
                    - cylinder(1.3,6.3,True).rotateX(deg(90)).translate( 10-3.86-1.3,0,-5+2.8)\
                    - cylinder(1.3,6.3,True).rotateX(deg(90)).translate(-10+3.86+1.3,0,-5+2.8)
        return m
    def richag(a):
        m = cylinder(1.5,6.4,True).rotateX(deg(90))\
                    + box((3,6.4,2.5),center=True).moveZ(1.5)\
                    + box((28,6.4,0.5),center=True).translate(-12.5,0,3)\
                    - cylinder(0.5,6.4,True).rotateX(deg(90))
        return m.rotateY(deg(a)).translate(7,0,4)
    def kontakti():
        m = box((0.5,3,3.9),center=True).translate(10-1.5,0,-6.5)\
                    + box((0.5,3,3.9),center=True).translate(10-11,0,-6.5)\
                    + box((0.5,3,3.9),center=True).translate(10-18,0,-6.5)
        return m

    kontsevic = zencad.assemble.unit()
    kontsevic.add_shape(telo(), color(0.25,0.25,0.25))
    kontsevic.add_shape(richag(0), color(0.75,0.75,0.75))
    kontsevic.add_shape(kontakti(), color(0.75,0.75,0.75))
    return kontsevic
#====================Двигатели============================
if nema == 17 :
    xz_dvig = 42.5
    otverstia = 31
    d_vint= 3
    y_dvig= 40
    diam_rotor= 4.5
    osn_rotor = 32
    dlin_rotor= 24
    d_vint= 3

if nema == 23:
    xz_dvig = 56.5
    otverstia = 47.2
    d_vint= 5
    y_dvig= 76
    diam_rotor= 6
    osn_rotor = 38.2
    dlin_rotor= 20
    d_vint= 5

rich_x=0.5*(xz_dvig+10) #Сдвиг рычага по Х
#=====================Червячная передача====================
step= 8
teeth = 6
l_gear= 7
n_s= 2
n= 24
#==================Подшипник==========================
pod_d1= 8
pod_d2= 5
pod_h = 2.5
#=======================База======================
pi = math.pi
rad = 150
b_cyl_r = 50
d_trub= 15.2
d_trub_vn= 12
#====================Руки==================
Rf= 120 # Длина плеча рычага
Re= 250 # Длина предплечья рычага

r_trubki = 4
r_trubki_vn = 3.9
#===========================================
#===============Каретка====================
E = 70
l_karetki = 50
#==========================================
def dvig(): # Модель двигателя
    if nema==17 :
        u = cube((54,22,54), center=True).forw(0.5*y_dvig-1) \
                + cube((50,16,50), center=True) \
                + cube((54,22,54), center=True).back(0.5*y_dvig-1)
        u = u.rotateY(pi/4)
    if nema==23 :
        u = cube((xz_dvig+1,10,xz_dvig+1), center=True)\
                    .back(0.5*y_dvig-1)\
                + cube((xz_dvig,y_dvig,38), center=True).forw(5)\
                + cube((38,y_dvig,xz_dvig), center=True).forw(5)

    rotor = cylinder(r=0.5*diam_rotor,h=dlin_rotor)\
                .up(0.5*y_dvig).rotateX(pi/2)\
                + cylinder(r=0.5*osn_rotor,h=2)\
                .up(0.5*y_dvig).rotateX(pi/2)

    dvig = cube((xz_dvig,y_dvig,xz_dvig), center=True) ^ u
    dvig = dvig + rotor
    return dvig.rotateX(pi/2).translate(0,rich_x,27.5+0.5*y_dvig)
def tri_dvig(): # Функция располажения трех двигателей
    tri_dvig = nullshape()
    for i in range(-1,2,1):
        a = 2*pi*i/3
        tri_dvig = tri_dvig + dvig().moveY(-rad).rotateZ(a)
    return tri_dvig
def hvost(f): # Ласточкин хвост
    if f == 1 :
        dh = 0.3
    else:
        dh = 0
    pnts=[[ 20 + dh ,10 + dh],
                [ 10 + dh , -10 - dh],
                [-10 - dh , -10 - dh],
                [-20 - dh ,10 + dh]]
    o=polygon(pnts=pnts,wire=False)
    m=linear_extrude(proto=o,vec=(0,0,20),center=True).moveZ(25)
    return m
def pos_gaiki(): # функция выреза под гайку
    m = ngon(r=4.15,n=6,wire=False)
    n = linear_extrude(proto=m, vec=(0,0,5), center=True)
    return n
def basa(): # Центральная деталь
    basa = cylinder(r=b_cyl_r,h=30,center=True)\
                - cylinder(r=25,h=30,center=True)
    basa=basa.moveZ(20)
    for i in range(-1,2,1):
        a = 2*pi*i/3
        basa = basa-hvost(1).moveY(-b_cyl_r+10).rotateZ(a)\
                - cylinder(2,40,True).moveY(-b_cyl_r+10).rotateZ(a)\
                - cylinder(2,80,True).moveY( b_cyl_r-10).rotateZ(a)\
                - pos_gaiki().translate(0,b_cyl_r-10,32.5).rotateZ(a)\
                - box((d_trub+0.4,20,d_trub+0.4),center=True).translate(0,b_cyl_r-10,20)\
                .rotateZ(a)\
                - cylinder(3.45,5,True).translate(0,b_cyl_r-10,7.5).rotateZ(a)\
                - cylinder(3.45,5,True).translate(0,-b_cyl_r+10,7.5).rotateZ(a)\
                - cylinder(d_trub*0.4,40,True).rotateX(deg(90)).translate(0,b_cyl_r-20,20)\
                    .rotateZ(a)
#=================Крепление под камеру==================
    cam =  sphere(30).up(20)\
            ^ cylinder(r=30,h=15,yaw=deg(120),center=True)\
            .rotateZ(deg(30)).up(37.5)
    cam = cam + cylinder(8,10,True).translate(0,-5,35)\
            + box((16,11.5,10),center=True).translate(0,0,35)\
            - cylinder(1,10,True).translate(0,-5.5,35)\
            - box ((54,19,3.5),center=True)\
            .translate(14,0,41).rotateZ(deg(90))\
            - box((8.75,8.75,6.5),center=True).up(45)
    basa = basa + cam
    return basa.rotateX(deg(180)).rotateZ(deg(60)).up(50)
def skelet(): # Каркас из труб
    def truba(a,h):
        m = box((a,h,a),center=True) - box((a-2,h,a-2),center=True)
        return m
    m = nullshape()
    for i in range(-1,2,1):
        a = 2*pi*i/3
        m = m + truba(d_trub,2*rad-b_cyl_r-10).moveY(rad+0.5*b_cyl_r-25)\
                    .moveZ(30).rotateZ(a)
    return m
def ploshadka(): # Крепление платы ардуино
    m = sphere(20) ^ box((50,d_trub,50),center=True).moveZ(-10)\
                - box(d_trub+0.5,center=True)
    m = m + box((60,75,4),center=True).moveZ(0.5*d_trub+5)\
            + cylinder(2,4).translate(-x05+3.8,-y05+15.23, 0.5*d_trub+5)\
            + cylinder(2,4).translate( x05-3.8,-y05+15.23, 0.5*d_trub+5)\
            + cylinder(2,4).translate( x05-7.63,y05-2.53 , 0.5*d_trub+5)\
            + cylinder(2,4).translate( x05-35.56, y05-2.53 , 0.5*d_trub+5)\
            - cylinder(1,30).translate(-x05+3.8, -y05+15.23, 0)\
            - cylinder(1,30).translate( x05-3.8, -y05+15.23, 0)\
            - cylinder(1,30).translate( x05-7.63, y05-2.53 , 0)\
            - cylinder(1,30).translate( x05-35.56,y05-2.53 , 0)
    return m.translate(0,rad,20)
def krepej(): # Лепесток с двигателем и червячным редуктором
    if nema==17:
        v = box((xz_dvig,xz_dvig,10),center=True)\
                ^ box((54,54,10),center=True).rotateZ(pi/4)
    else:
        v = box((xz_dvig,xz_dvig,10),center=True)
    o=nullshape()
#=================Отверстия под винты и двигатель===============
    for i in range(4):
        o = o + cylinder(r=1.5,h=15,center=True)\
            .translate(0.5*otverstia,0.5*otverstia,0)\
            .rotateZ(i*pi/2)\
            + cylinder(r=2.7,h=4,center=True)\
            .translate(0.5*otverstia,0.5*otverstia,5.5)\
            .rotateZ(i*pi/2)
    pnts =     [[ 11 , 0 ,  0  ],
                [ 9  , 0 ,  9  ],
                [-9  , 0 ,  9  ],
                [-11 , 0 ,  0  ]]
    l = polygon(pnts=pnts,wire=False)
    n = linear_extrude(proto=l,vec=(0,40,0),center=True)

    krep = box((xz_dvig+20,xz_dvig+20,15),center=True)\
            ^ sphere(r=0.8*xz_dvig)\
            - cone(11,9,9,True).up(4.5)\
            - v.down(5)\
            - o - n.moveY(20)
#================Рама для удержания оси рычага ==================
    s = sphere(r=0.5*xz_dvig+24.5)\
            ^ box((150,28,50),center=True).translate(0.5*xz_dvig+12.5,0,17.5)\
            - sphere(r=0.5*xz_dvig+10).moveZ(5)\
            - sphere(52.5).translate(-25,55,15)\
            - sphere(52.5).translate(-25,-55,15)
    krep = krep + s

    krep = krep + cylinder(r=9, h=28, center=True)\
            .translate(rich_x,27.5,0).rotateX(pi/2)\
            - cylinder(r=2.5, h=28, center=True)\
            .translate(rich_x,27.5,0).rotateX(pi/2)\
            - cylinder(r=20, h=step-1.25, center=True)\
            .translate(rich_x,27.5,0).rotateX(pi/2)

#===============Крепление к базе=========
    hvostx = - rad+b_cyl_r + rich_x - 10
    box_h= - hvostx - rich_x

    krep = krep + box((box_h,40,15),center=True)\
            .translate(-0.5*(rad-rich_x)+10,0,0)\
            - cylinder(r=b_cyl_r+0.2,h=15,center=True)\
            .translate(-(rad-rich_x),0,0)\
            - cylinder(0.8*box_h,15,center=True)\
            .translate(-0.5*(rad-rich_x)+10,box_h,0)\
            - cylinder(0.8*box_h,15,center=True)\
            .translate(-0.5*(rad-rich_x)+10,-box_h,0)\
            + hvost(0).rotateZ(pi/2).translate(hvostx,0,-22.5)\
            - cylinder(2,40,True).moveX(hvostx)\
            - pos_gaiki().translate(hvostx,0,10)
#===============Крепление для концевика вверх=======
    krep = krep - hvost(1).rotateZ(deg(90)).scaleX(0.25).scaleY(0.25)\
                .translate(rich_x+9,0,-30)\
                - box((10,6,30),center=True).translate(rich_x+15,0,-10)\
                - box((4,28,6),center=True).translate(rich_x+12.5,0,0)\
                - cylinder(2,28,True).rotateX(deg(90)).translate(rich_x+12.5,0,-3)\
                - cylinder(2,28,True).rotateX(deg(90)).translate(rich_x+12.5,0, 3)
#===============Крепление для концевика низ=======
    niz = cylinder(11,20,True).rotateY(deg(90)).translate(0,0,40)\
            ^ box((20,20,10),center=True).translate(0,0,45)

    krep = krep + niz\
            + box((20,14,10),center=True).translate(0,0,52)\
            - hvost(1).scaleX(0.25).scaleY(0.25)\
            .rotateX(deg(90)).rotateY(deg(180)).rotateZ(deg(90))\
            .translate(-25,0,45)\
            - box((20,6.2,11),center=True).translate(0,0,52)\
            - box((6,14,4),center=True).translate(0,0,52)\
            - cylinder(2,14,True).rotateX(deg(90)).translate(3,0,52)\
            - cylinder(2,14,True).rotateX(deg(90)).translate(-3,0,52)
#===============Ограничитель для рычага===========
    krep = krep - cylinder(r=6.25, h=4, center=True)\
            .translate(rich_x,27.5,-12).rotateX(pi/2)\
            - cube((12.5,20,4),center=True).moveY(-10).rotateZ(deg(90-15))\
            .translate(rich_x,27.5,-12).rotateX(pi/2)\
            - cube((12.5,20,4),center=True).moveY(10)\
            .translate(rich_x,27.5,-12).rotateX(pi/2)\
            - cube((12.5,20,4),center=True).moveY(10).rotateZ(deg(-45))\
            .translate(rich_x,27.5,-12).rotateX(pi/2)\
            - cylinder(r=6.25, h=4, center=True)\
            .translate(rich_x,27.5,12).rotateX(pi/2)\
            - cube((12.5,20,4),center=True).moveY(-10).rotateZ(deg(90-15))\
            .translate(rich_x,27.5,12).rotateX(pi/2)\
            - cube((12.5,20,4),center=True).moveY(10)\
            .translate(rich_x,27.5,12).rotateX(pi/2)\
            - cube((12.5,20,4),center=True).moveY(10).rotateZ(deg(-45))\
            .translate(rich_x,27.5,12).rotateX(pi/2)


#===============Отверстия для проводов =====================
    krep = krep - cylinder(4,30,True).rotateY(deg(-45)).translate(-40,0,0)

    return krep.rotateZ (-pi/2).rotateY(pi).translate(0,rich_x,27.5)
def krep_konch(): # крепеж для концевика
    m = box((5.9,6,8),center=True)\
            + hvost(1).scaleX(0.25).scaleY(0.25).scaleZ(8/20)\
            .translate(0,5.5,-10)\
            - cylinder(2,6,True).rotateY(deg(90)).moveY(1.25)\
            + box((5.9,15,8),center=True).moveY(-10)
    o = box((14,25,10),center=True).moveY(-28)\
            ^ cylinder(7.5,25,True).rotateX(deg(90)).moveY(-28)\
            - box((7,23,10),center=True).moveY(-31)
    m = m + o
    d = cylinder(1.3,30,True).rotateY(deg(90)).translate(0,10-3.86-1.3,-5+2.8)\
        + cylinder(1.3,30,True).rotateY(deg(90)).translate(0,-10+3.86+1.3,-5+2.8)
    m = m - d.rotateX(deg(165)).translate(0,-31.3,-2.5)
    return m.translate(0,-rich_x+12.5,27)
def krep_konch_niz(): # крепеж для нижнего концевика
    m = cylinder(7.5,27,True).translate(0,-2,-8)\
            ^ box((12,12,27),center=True).translate(0,-2,-8)\
            - box((6.25,20,21),center=True).down(7.25)\
            - cylinder(1.3,12,True).rotateY(deg(90)).translate(0,-5.3,-2.65)\
            - cylinder(1.3,12,True).rotateY(deg(90)).translate(0,-5.3,-2.65-9.7)
    m = m + box((6,8,12),center=True).translate(0,0,11)\
            - cylinder(2,6,True).rotateY(deg(90)).translate(0,0,10.5)\
            + hvost(1).scaleX(0.24).scaleY(0.24).scaleZ(8/20)\
            .rotateX(deg(90)).translate(0,10,17.5)
    return m
def gear(teeth,step): # 2д шестерня
    g=nullshape()
    angle = pi/teeth
    rad_opis = (step/2) / math.sin(angle/2)
    rad_vpis = (step/2) / math.tan(angle/2)

    c1 = circle(step/2,angle=(1.5*pi-deg(0),pi/2-deg(0)), wire=True)\
                .translate(rad_opis,0,0)
    c2 = circle(step/2,angle=(pi/2+deg(10),1.5*pi-deg(10)), wire=True)\
                .translate(rad_vpis,0,0).rotateZ(angle)

    c12 = sew([c1, segment(c1.endpoints()[1], c2.endpoints()[1]), c2])

    c = []
    for i in range(teeth):
        ang = pi*2/teeth*i
        c.append(c12.rotateZ(ang))

    d = []
    for i in range(teeth-1):
        d.append(segment(c[i].endpoints()[1], c[i+1].endpoints()[0]))
    d.append(segment(c[0].endpoints()[0], c[-1].endpoints()[1]))

    e = []
    for i in range(teeth):
        e.append(c[i])
        e.append(d[i])
    return sew(e).rotateX(0.5*pi)
def gear3d(): # Шестерня
    angle = pi/teeth
    rad_opis = (step/2) / math.sin(angle/2)
    rad_vpis = (step/2) / math.tan(angle/2)
    g = cylinder(0.7*rad_vpis,step-1.5,True).rotateX(deg(90))
    for i in range (teeth):
        g = g + sphere(step/2-0.2).moveX(rad_opis-0.5).rotateY(2*i*angle + pi/4)\
              + cylinder(step/2-0.2,15,True).rotateY(deg(90)).moveX(0.5*rad_opis)\
              .rotateY(2*i*angle + pi/4)
    for i in range (teeth):
        g = g - cylinder(0.55*step,step,True).rotateX(deg(90))\
              .moveX(rad_opis-1.5).rotateY((2*i+1)*angle + pi/4)
    g = g.rotateY(deg(15)) + box((d_trub_vn-0.25,d_trub_vn-0.25,30),center=True)\
            .up(20).rotateY(deg(90))
    g= g ^ box((100,step-1.5,100),center=True)

    g = g - cylinder(0.5*pod_d1,step-1.5,True).rotateX(deg(90))
    return g.rotateZ(deg(-90))
def worm (): # Червь
    angle = pi/teeth
    rad_opis =(step/2) / math.tan(angle/2)
    a = (n_s*angle*0.5)/n
    b = 0.5*pi/n
    def chast(x):
        if x==0:
                da = 0
                db = 0
        if x==1:
                da = a*n
                db = pi/2
        if x==2:
                da = 2*a*n
                db = pi
        if x==3:
                da = 3*a*n
                db = 1.5*pi
        g=[]
        r=0.5*(xz_dvig+10)
        for i in range(n+1):
                g.append(gear(teeth,step).rotateY(i*a + da)\
                            .translate(r,0,20).rotateZ(i*b + db))
        w = loft(g)
        #w.unlazy()
        return w
    x = [i for i in range(0,4,1)]
    with futures.ThreadPoolExecutor() as executor:
        worm = executor.map(chast, x)
    o = cylinder(r=3,h=30,center=True).up(15)\
        ^cube([6,6,20],center=True).translate(1,0,10)
    w = sphere(r=0.5*(xz_dvig+10),pitch=(0,pi/2))\
        - union(list(worm))\
        - cylinder(2,50,True).translate(0.5*otverstia,0.5*otverstia,0)
    w = w + cone(r1=10.4, r2=9.2, h=6,center=True).down(3)\
          - cylinder(11.2/2,11,True).down(0.5)\
          - cylinder(1.5,12,True).rotateY(deg(90)).translate(-5,0,-5.5+2.7)\
          - o
    w = w.rotateZ(deg( 90))
    return w.rotateY(pi)#.translate(0,rich_x,19.5)
def plecho(): # Плечо
#    m = cylinder(r=4,h=Rf - 40).up(20).rotateX(deg(90+teta))

    m = box((d_trub,d_trub,Rf-30),center=True)\
            - box((d_trub_vn,d_trub_vn,Rf),center=True)
    m = m.moveZ((Rf-30)/2+20).rotateX(deg(90))
    return m
def plecho_krep():
    m =  cylinder(0.5*d_trub+6,d_trub,center=True)\
            .up(32.5).rotateX(deg(90))\
            ^ box (d_trub+6,center=True).up(32.5).rotateX(deg(90))
    m =  m  + cylinder(6,28,True).rotateY(deg(90))\
            + box((28,12,40),center=True).up(20).rotateX(deg(90))\
            - cylinder(2.5,28,True).rotateY(deg(90))\
            - cylinder(21,20.5,True).rotateY(deg(90))\
            - box((d_trub+0.2,d_trub+0.2,d_trub+10),center=True)\
            .up(30).rotateX(deg(90))\
            - cylinder(2.5,28,True).rotateY(deg(90)).moveY(-30)
    return m
def camera():
    m = box ((54,18.6,1.1),center=True).moveX(14)\
            - cylinder(2.5,1.1,True).moveX(-5.5)\
            + box((8.5,8.5,6.5),center=True).down(3.75)
    return m 
def lokot_verh():
    m = box((d_trub_vn,30,d_trub_vn),center=True).moveY(20)\
            + cylinder(d_trub_vn,d_trub_vn,True).rotateY(deg(90))\
            + cylinder(d_trub_vn/2,l_karetki,True).rotateY(deg(90))\
            + sphere(d_trub_vn).translate(0.5*l_karetki,0,0)\
            + sphere(d_trub_vn).translate(-0.5*l_karetki,0,0)
    return m.moveY(-Rf)
def lokot_niz():
    m = sphere(d_trub)-sphere(d_trub_vn+0.2)
    m = m ^ cube((0.75*d_trub,2*d_trub,2*d_trub),center=True)
    m = m + cylinder(r_trubki_vn,30,True).moveZ(-15-d_trub)
    #m = m.moveX(0.5*l_karetki) + m.moveX(-0.5*l_karetki)
    return m#.moveY(-Rf)
def arm():
    m = cylinder(r_trubki,Re-2*d_trub,True).moveZ(-0.5*Re)\
            + lokot_niz()\
            + lokot_niz().rotateX(deg(180)).moveZ(-Re)
    #m = m.moveX(0.5*l_karetki) + m.moveX(-0.5*l_karetki)
    return m
def karetka():
    m = cylinder(d_trub_vn/2,l_karetki,True)\
            .rotateY(deg(90)).moveY(-0.5*E)\
            + sphere(d_trub_vn).translate(0.5*l_karetki,-0.5*E,0)\
            + sphere(d_trub_vn).translate(-0.5*l_karetki,-0.5*E,0)\
            + torus(r1=math.sqrt(3)*E/2, r2=d_trub_vn/2, yaw=deg(60))\
            .rotateZ(deg(120)).translate(math.sqrt(3)*E/2,-0.5*E,0)
    m= m + m.rotateZ(deg(120)) + m.rotateZ(deg(-120))
    return m


disp(square(200,center=True,wire=True),color.red)
disp(ngon(2*rad,n=3,wire=True).rotateZ(pi/2),color.cian)
disp(basa(),color.blue)
disp(krep_konch().moveZ(2.5).moveY(-rad),color.cian)
disp(krep_konch_niz().translate(0,-rad+25,-35),color.cian)
disp(skelet(),color.mech)
disp(ploshadka().up(10),color.green)
disp(camera().moveZ(10).rotateZ(deg(-30)),color.green)
disp(tri_dvig(),color(0.3,0.3,0.3))

disp(krepej().moveY(-rad),color(1,0.4,0))

disp(krepej().moveY(-rad).rotateZ(deg(120)),color(1,0.4,0))
#disp(worm(0).moveY(-rad).rotateZ(deg(120)),color.red)

disp(krepej().moveY(-rad).rotateZ(deg(-120)),color(1,0.4,0))
#disp(worm(0).moveY(-rad).rotateZ(deg(-120)),color.red)

arduino.relocate(translate(0,rad,47.5) * rotateZ(pi))
shild.relocate(translate(0,rad,60) * rotateZ(pi))


kon1 = kontsevic()
kon2 = kontsevic()
#kon3 = kontsevic()
kon1.relocate( translate(0,-rad-45,27) * rotateZ(deg(-90)) * rotateY(deg(165)))
kon2.relocate( translate(0,-rad+17.5,-42.5) * rotateY(deg(-90)) * rotateX(deg(90)))
#kon3.relocate( translate(0,0,100) * rotateY(deg(0)) * rotateX(deg(0)))
disp(kon1)
disp(kon2)
#disp(kon3)

#disp(worm(1).up(50),color.red)

disp(arduino)
disp(shild)

m1=krepej()
m2=basa()
m3=plecho_krep()
to_stl(m1,'/home/oleg/krepej.stl',0.01)
to_stl(m2,'/home/oleg/basa.stl',0.01)
to_stl(m3,'/home/oleg/plecho_krep.stl',0.01)
#to_stl(m,'C:/stl/worm.stl',0.01)

teta1 = 0
worm1   = disp(worm(),color.red)
worm2   = disp(worm(),color.red)
worm3   = disp(worm(),color.red)
gear3d1 = disp(gear3d())
gear3d2 = disp(gear3d())
gear3d3 = disp(gear3d())
plecho1 = disp(plecho(),color(0.8,0.8,0.8))
plecho2 = disp(plecho(),color(0.8,0.8,0.8))
plecho3 = disp(plecho(),color(0.8,0.8,0.8))
plecho_krep1 = disp(plecho_krep(),color(0,0,0.8))
plecho_krep2 = disp(plecho_krep(),color(0,0,0.8))
plecho_krep3 = disp(plecho_krep(),color(0,0,0.8))
lokot_verh1 = disp(lokot_verh(),color.red)
lokot_verh2 = disp(lokot_verh(),color.red)
lokot_verh3 = disp(lokot_verh(),color.red)

karetka = disp(karetka(),color.red)
arm1p = disp(arm(),color.blue)
arm1l = disp(arm(),color.blue)
arm2p = disp(arm(),color.blue)
arm2l = disp(arm(),color.blue)
arm3p = disp(arm(),color.blue)
arm3l = disp(arm(),color.blue)
ngon = disp(ngon(E,n=3,wire=True).rotateZ(pi/2),color.cian)
nulltime  = time.time()


def animate(widget):
    t = (20*(time.time() - nulltime))%210
#    t = 50
    if (t<105):
        teta1 = t-15
        teta2 = t-15
        teta3 = t-15
    else:
        teta1 = 210-t-15
        teta2 = 210-t-15
        teta3 = 210-t-15
       #========1 рука
    worm1.relocate(translate(0,-rad+rich_x,19.5) * rotateZ(deg(-3*teta1 )))
    gear3d1.relocate(moveY(-rad) * rotateX(deg(teta1)))
    plecho1.relocate(moveY(-rad) * rotateX(deg(teta1)))
    plecho_krep1.relocate(moveY(-rad) * rotateX(deg(teta1)))
    lokot_verh1.relocate(moveY(-rad) * rotateX(deg(teta1)))
        #========2 рука
    worm2.relocate(translate(1.732*0.5*(rad-rich_x),0.5*(rad-rich_x),19.5)\
            * rotateZ(deg(-3*teta2 + 120)))
    gear3d2.relocate(translate(1.732*0.5*rad,0.5*rad,0)\
            * rotateZ(deg(120)) * rotateX(deg(teta2)))
    plecho2.relocate(translate(1.732*0.5*rad,0.5*rad,0)\
            * rotateZ(deg(120)) * rotateX(deg(teta2)))
    plecho_krep2.relocate(translate(1.732*0.5*rad,0.5*rad,0)\
            * rotateZ(deg(120)) * rotateX(deg(teta2)))
    lokot_verh2.relocate(translate(1.732*0.5*rad,0.5*rad,0)\
            * rotateZ(deg(120)) * rotateX(deg(teta2)))
        #========3 рука
    worm3.relocate(translate(-1.732*0.5*(rad-rich_x),0.5*(rad-rich_x),19.5)\
            * rotateZ(deg(-3*teta3 - 120)))
    gear3d3.relocate(translate(-1.732*0.5*rad,0.5*rad,0)\
            * rotateZ(deg(-120)) * rotateX(deg(teta3)))
    plecho3.relocate(translate(-1.732*0.5*rad,0.5*rad,0)\
            * rotateZ(deg(-120)) * rotateX(deg(teta3)))
    plecho_krep3.relocate(translate(-1.732*0.5*rad,0.5*rad,0)\
            * rotateZ(deg(-120)) * rotateX(deg(teta3)))
    lokot_verh3.relocate(translate(-1.732*0.5*rad,0.5*rad,0)\
            * rotateZ(deg(-120)) * rotateX(deg(teta3)))
    # радиусы описаной окружности базы и каретки
    t = rad - 0.5*E  # радиус вписанной окружности

    x1 = 0
    y1 = -(t + Rf*math.cos( deg(teta1) ))
    z1 = -Rf*math.sin( deg(teta1) )

    y2 = (t + Rf*math.cos( deg(teta2) ))*math.sin(pi/6)
    x2 = y2*math.tan(pi/3)
    z2 = -Rf*math.sin( deg(teta2) )


    y3 = (t + Rf*math.cos( deg(teta3) ))*math.sin(pi/6)
    x3 = -y3*math.tan(pi/3)
    z3 = -Rf*math.sin( deg(teta3) )

    dnm = (y2-y1)*x3-(y3-y1)*x2

    w1 = y1**2 + z1**2
    w2 = x2**2 + y2**2 + z2**2
    w3 = x3**2 + y3**2 + z3**2

    a1 = (z2-z1)*(y3-y1)-(z3-z1)*(y2-y1)
    b1 = -((w2-w1)*(y3-y1)-(w3-w1)*(y2-y1))/2

    a2 = -(z2-z1)*x3+(z3-z1)*x2
    b2 = ((w2-w1)*x3 - (w3-w1)*x2)/2

    a = a1**2 + a2*a2 + dnm**2
    b = 2*(a1*b1 + a2*(b2-y1*dnm) - z1*dnm**2)
    c = (b2-y1*dnm)*(b2-y1*dnm) + b1**2 + dnm**2*(z1**2 - Re**2)

    d = b**2 - 4*a*c
    print(d)
    Z = -0.5*(b + math.sqrt(d))/a
    Y = (a1*Z + b1)/dnm
    X = (a2*Z + b2)/dnm



    karetka.relocate(translate(X,Y,Z))
    ngon.relocate(translate(X,Y,Z))

    arm1p.relocate(translate(x1+0.5*l_karetki,y1-0.5*E,z1)\
            * rotateY(-math.asin( (X-x1)/Re ) )\
            * rotateX(math.asin( (Y-y1)/Re ) ))
    arm1l.relocate(translate(x1-0.5*l_karetki,y1-0.5*E,z1)\
            * rotateY(-math.asin( (X-x1)/Re ) )\
            * rotateX(math.asin( (Y-y1)/Re ) ))

    arm2p.relocate(translate(x2+0.433*E+0.25*l_karetki\
            ,y2+0.25*E-0.433*l_karetki,z2) \
            * rotateZ(deg(120))\
            * rotateX(math.asin( (Y+0.866*x2+0.5*y2)/Re ) )\
            * rotateY(math.asin( (X+0.5*x2-0.866*y2)/Re ) ))
    arm2l.relocate(translate(x2+0.433*E-0.25*l_karetki\
            ,y2+0.25*E+0.433*l_karetki,z2) \
            * rotateZ(deg(120))\
            * rotateX(math.asin( (Y+0.866*x2+0.5*y2)/Re ) )\
            * rotateY(math.asin( (X+0.5*x2-0.866*y2)/Re ) ))

    arm3p.relocate(translate(x3-0.433*E+0.25*l_karetki\
            ,y3+0.25*E+0.433*l_karetki,z3) \
            * rotateZ(deg(-120))\
            * rotateX(math.asin( (Y-0.866*x3+0.5*y3)/Re ) )\
            * rotateY(math.asin( (X+0.5*x3+0.866*y3)/Re ) ))
    arm3l.relocate(translate(x3-0.433*E-0.25*l_karetki\
            ,y3+0.25*E-0.433*l_karetki,z3) \
            * rotateZ(deg(-120))\
            * rotateX(math.asin( (Y-0.866*x3+0.5*y3)/Re ) )\
            * rotateY(math.asin( (X+0.5*x3+0.866*y3)/Re ) ))

show(animate=animate)






#show()

