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
#=====================Концевик==========================
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
#=====================Червячная передача====================
step= 8
teeth = 6
l_gear= 7
n_s= 2
n= 24
#====================Подшипник==========================
pod_d1= 8
pod_d2= 5
pod_h = 2.5

#===============================================

#=======================база======================
pi = math.pi
rad = 150
b_cyl_r = 50
d_trub= 15.2
d_trub_vn= 12
#============================================
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

rich_x=0.5*(xz_dvig+10) #сдвиг рычага по X
#===================================================
#====================� уки==================
Rf= 150 # длина плеча рычага
Re= 400 # длина предплечья рычага

r_trubki = 3.9
#===========================================

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
def tri_dvig(): # Функция расположения трех двигателей
    tri_dvig = null()
    for i in range(-1,2,1):
        a = 2*pi*i/3
        tri_dvig = tri_dvig + dvig().moveY(-rad).rotateZ(a)
    return tri_dvig
def null(): # Функция пустого объекта
    m= box(1) - box(1)
    return m

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
def basa(): # Центральная деталь базы
    basa = cylinder(r=b_cyl_r,h=30,center=True)\
                - cylinder(r=25,h=30,center=True)
    basa=basa.moveZ(20)
    def pos_gaiki():
        m = ngon(r=3.55,n=6,wire=False)
        n = linear_extrude(proto=m, vec=(0,0,5), center=True)
        return n
    for i in range(-1,2,1):
        a = 2*pi*i/3
        basa = basa-hvost(1).moveY(-b_cyl_r+10).rotateZ(a)\
                    - cylinder(2,40,True).moveY(-b_cyl_r+10).rotateZ(a)\
                    - cylinder(2,80,True).moveY( b_cyl_r-10).rotateZ(a)\
                    - cylinder(3.45,5,True).translate(0,b_cyl_r-10,32.5).rotateZ(a)\
                    - box((d_trub+0.4,20,d_trub+0.4),center=True).translate(0,b_cyl_r-10,20)\
                    .rotateZ(a)\
                    - pos_gaiki().translate(0,b_cyl_r-10,7.5).rotateZ(a)\
                    - pos_gaiki().translate(0,-b_cyl_r+10,7.5).rotateZ(a)\
                    - cylinder(d_trub*0.4,40,True).rotateX(deg(90)).translate(0,b_cyl_r-20,20)\
                    .rotateZ(a)
#=================Центральное крепление==================
    basa = basa + cube((5,50,5),center=True).translate(10,0,7.5)\
                +cube((5,50,5),center=True).translate(-10,0,7.5)
    return basa
def skelet(): # Трубы квадратного профиля
    def truba(a,h):
        m = box((a,h,a),center=True) - box((a-2,h,a-2),center=True)
        return m
    m = null()
    for i in range(-1,2,1):
        a = 2*pi*i/3
        m = m + truba(d_trub,2*rad-b_cyl_r-10).moveY(rad+0.5*b_cyl_r-25)\
                    .moveZ(20).rotateZ(a)
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

def krepej(): # Лепесток с двигателем и червячной передачей 
    if nema==17:
        v = box((xz_dvig,xz_dvig,10),center=True)\
                ^ box((54,54,10),center=True).rotateZ(pi/4)
    else:
        v = box((xz_dvig,xz_dvig,10),center=True)
    o=null()
#=================отверстия под винты и двигатель===============
    for i in range(4):
        o = o + cylinder(r=1.5,h=15,center=True)\
            .translate(0.5*otverstia,0.5*otverstia,0)\
            .rotateZ(i*pi/2)\
            + cylinder(r=2.7,h=4,center=True)\
            .translate(0.5*otverstia,0.5*otverstia,5.5)\
            .rotateZ(i*pi/2)
    pnts =     [[ 11  , 0 ,  0  ],
                [ 9  , 0 ,  9  ],
                [-9  , 0 ,  9  ],
                [-11  , 0 ,  0  ]]
    l = polygon(pnts=pnts,wire=False)
    n = linear_extrude(proto=l,vec=(0,40,0),center=True)

    krep = box((xz_dvig+20,xz_dvig+20,15),center=True)\
            ^ sphere(r=0.8*xz_dvig)\
            - cone(11,9,9,True).up(4.5)\
            - v.down(5)\
            - o - n.moveY(20)
#================� ама для удержания оси рычага ==================
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
            - cylinder(3.45,5,True).translate(hvostx,0,-5)
#===============Крепление для концевика верх=======
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


#===============Отверстия для проводов=====================
    krep = krep - cylinder(4,30,True).rotateY(deg(-45)).translate(-40,0,0)

    return krep.rotateZ (-pi/2).rotateY(pi).translate(0,rich_x,27.5)

def krep_konch(): # Крепеж для концевика
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
def krep_konch_niz():
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
def gear(teeth,step): # Функция шестерни
    g=null()
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

def gear3d(teta): # Основание рычаг а с шестерней 
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
    g = g + box((d_trub_vn-0.25,d_trub_vn-0.25,30),center=True)\
            .up(20).rotateY(deg(90+teta))
    g= g ^ box((100,step-1.5,100),center=True)

    g = g - cylinder(0.5*pod_d1,step-1.5,True).rotateX(deg(90))
#    g=[]
#    g.append(gear(teeth,step).translate(0,0.5*l_gear,0).rotateY(deg(3)).scale(0.82))
#    g.append(gear(teeth,step).translate(0,0.5,0).scale(0.98))
#    g.append(gear(teeth,step).translate(0,-0.5,0).scale(0.98))
#    g.append(gear(teeth,step).translate(0,-0.5*l_gear,0).rotateY(deg(-3)).scale(0.82))

#    g=loft(g).rotateY(deg(teta))
#    g=g - cylinder(r=0.5*pod_d1,h=l_gear,center=True).rotateX(pi/2)
#    k = cone(r1=3,r2=4,h=10).up(10).rotateY(deg(90 + teta))\
#        +cylinder(r=r_trubki,h=30).up(20).rotateY(deg(90 + teta))

    return g.rotateZ(deg(-90))

def worm (teta): # Червяк 
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
    w = w.rotateZ(deg(3*teta + 90))
    return w.rotateY(pi)#.translate(0,rich_x,19.5)

def plecho(teta): # Плечо
#    m = cylinder(r=4,h=Rf - 40).up(20).rotateX(deg(90+teta))

    m = box((d_trub,d_trub,Rf),center=True)\
            - box((d_trub_vn,d_trub_vn,Rf),center=True)
    m = m.moveZ(Rf/2+20).rotateX(deg(90+teta))
    return m

def plecho_krep(teta):
    m =  cylinder(0.5*d_trub+6,d_trub,center=True).up(32.5).rotateX(deg(90 + teta))\
            ^ box (d_trub+6,center=True).up(32.5).rotateX(deg(90 + teta))
    m =  m  + cylinder(6,28,True).rotateY(deg(90))\
            + box((28,12,40),center=True).up(20).rotateX(deg(90 + teta))\
            - cylinder(2.5,28,True).rotateY(deg(90))\
            - cylinder(25,20.5,True).rotateY(deg(90))\
            - box((d_trub+0.2,d_trub+0.2,d_trub+10),center=True)\
            .up(30).rotateX(deg(90 + teta))
    return m

disp(square(200,center=True,wire=True),color.red)
disp(ngon(2*rad,n=3,wire=True).rotateZ(pi/2),color.cian)
disp(basa(),color.blue)
disp(krep_konch().moveZ(2.5).moveY(-rad),color.cian)
disp(krep_konch_niz().translate(0,-rad+25,-35),color.cian)
disp(skelet(),color.mech)
disp(ploshadka(),color.green)
#disp(tri_dvig(),color(0.3,0.3,0.3))


disp(krepej().moveY(-rad),color.green)


disp(krepej().moveY(-rad).rotateZ(deg(120)),color.green)
#disp(worm(0).moveY(-rad).rotateZ(deg(120)),color.red)

disp(krepej().moveY(-rad).rotateZ(deg(-120)),color.green)
#disp(worm(0).moveY(-rad).rotateZ(deg(-120)),color.red)

arduino.relocate(translate(0,rad,37.5) * rotateZ(pi))
shild.relocate(translate(0,rad,50) * rotateZ(pi))


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

m=worm(1)
#to_stl(m,'/home/oleg/Zencad/stl/worm.stl',0.01)
to_stl(m,'C:/stl/worm.stl',0.01)

teta1 = -15
worm   = disp(worm(teta1),color.red)
gear3d = disp(gear3d(teta1))
plecho = disp(plecho(teta1),color(0.8,0.8,0.8))
plecho_krep = disp(plecho_krep(teta1),color(0,0,0.8))

nulltime  = time.time()

def animate(widget):
    t = (20*(time.time() - nulltime))%210
    if (t<105):
        worm.relocate(translate(0,-rad+rich_x,19.5) * rotateZ(deg(-3*t)))
        gear3d.relocate(moveY(-rad) * rotateX(deg(t)))
        plecho.relocate(moveY(-rad) * rotateX(deg(t)))
        plecho_krep.relocate(moveY(-rad) * rotateX(deg(t)))
    else:
        worm.relocate(translate(0,-rad+rich_x,19.5) * rotateZ(deg(-3*(210-t))))
        gear3d.relocate(moveY(-rad) * rotateX(deg(210-t)))
        plecho.relocate(moveY(-rad) * rotateX(deg(210-t)))
        plecho_krep.relocate(moveY(-rad) * rotateX(deg(210-t)))

show(animate=animate)






#show()

