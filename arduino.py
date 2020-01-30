from zencad import *



x05=0.5*53.4
y05=0.5*68.6

def plate(f):
    pnts=[  [ x05, y05],
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
            - circle(r=1.6).translate( x05-3.8,   y05-15.23, 0)\
            - circle(r=1.5).translate(-x05+3.8,   y05-15.23, 0)\
            - circle(r=1.5).translate(-x05+7.63, -y05+2.53 , 0)\
            - circle(r=1.5).translate(-x05+35.56, -y05+2.53, 0)
    else:
        m=polygon(pnts=pnts, wire=False) \
            - circle(r=1.6).translate( x05-3.8,   y05-13.4, 0)\
            - circle(r=1.5).translate(-x05+3.8,   y05-13.4, 0)

    return linear_extrude(proto=m, vec=(0,0,2),center=False)


def usb():
    pnts=[  [ 5  ,0,-4],
            [ 5  ,0, 2],
            [ 2.5,0, 4],
            [-2.5,0, 4],
            [-5  ,0, 2],
            [-5  ,0,-4]]
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
    pnts=[  [ 4  ,0, 0],
            [ 4  ,0, 5.6],
            [ 2.6,0, 10],
            [-2.6,0, 10],
            [-4  ,0, 5.6],
            [-4  ,0, 0]]
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

arduino.relocate(moveZ(-12.5))
disp(shild)
disp(arduino)

show()
