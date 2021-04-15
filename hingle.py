from zencad import *
from math import sqrt,pi

def part2(size=20,r=6,R=8,r_b = 2,h=5,l=10):
    line = sew([polysegment([ (size + r+0.25*l, 0) , 
                              (size + r+0.25*l, 1.5*l), 
                              (size + r+0.25*l, size)   ]),
                circle_arc((size + r+0.25*l, size),
                           (size + 0.5*sqrt(2)*r +0.25*l, size+0.5*sqrt(2)*r),
                           (size +0.25*l, size + r)),
                segment((size +0.25*l, size + r),(size - 0.25*l, size + r)),
                circle_arc((size - 0.25*l, size + r),
                           (size - 0.5*sqrt(2)*r -0.25*l, size+0.5*sqrt(2)*r),
                           (size - r -0.25*l, size)),
                circle_arc((size - r -0.25*l, size),
                           (0, 0.75*l),
                           (-size + r , size)),
                circle_arc((-size+r,size),
                           (-size,size+r),
                           (-size-r,size)),
                polysegment([(-size-r,size),
                             (-size -r -0.25*l,1.5*l),
                             (-size -r -0.25*l,0) ])
        ])

    base = sew([ line,line.rotateX(pi) ]).fill().extrude(h,center=False)

    base -= cylinder(r_b,h,False).moveX(size+0.25*l).moveY(size)
    base -= box([0.5*l,2*r_b,2*h],center=True).move(size,size,h)
    base -= cylinder(r_b,h,False).moveX(size-0.25*l).moveY(size)

    base -= cylinder(r_b,h,False).moveX(size+0.25*l).moveY(-size)
    base -= box([0.5*l,2*r_b,2*h],center=True).move(size,-size,h)
    base -= cylinder(r_b,h,False).moveX(size-0.25*l).moveY(-size)

    base -= cylinder(r_b,h,False).moveX(-size).moveY(size)
    base -= cylinder(r_b,h,False).moveX(-size).moveY(-size)

    line2 = sew([segment((size+r+0.25*l,0,0),(size+r+0.25*l,0,h+R)),
                circle_arc((size+r+0.25*l,0,h+R),
                           (size+r+0.25*l-R,0,h+2*R),
                           (size+r+0.25*l-2*R,0,h+R)),
                circle_arc((size+r+0.25*l-2*R,0,h+R),
                            (0,0,h),
                            (-size -r-0.25*l+2*R,0,h+R)),
                circle_arc((-size-r-0.25*l+2*R,0,h+R),
                           (-size-r-0.25*l+R,0,h+2*R),
                           (-size-r-0.25*l,0,h+R)),
                segment((-size-r-0.25*l,0,h+R),(-size-r-0.25*l,0,0)),
                segment((-size-r-0.25*l,0,0),(size+r+0.25*l,0,0))
                ]).fill()
    base += line2.extrude((0,-0.5*l,0)).moveY(0.75*l)
    base += line2.extrude((0,0.5*l,0)).moveY(-0.75*l)

    base -= cylinder(r_b,5*l,True).rotateX(0.5*pi).moveX(-size).moveZ(h+R)
    base -= cylinder(r_b,5*l,True).rotateX(0.5*pi).moveX(size).moveZ(h+R)
    return unify(base)

def part1(size_x=15,size_y=20,r=6,R=8,r_b = 2,h=5,l=10):
    line = sew([polysegment([ (size_x + r+0.25*l, 0) , 
                              (size_x + r+0.25*l, 1.5*l), 
                              (size_x + r+0.25*l, size_y)   ]),
                circle_arc((size_x + r+0.25*l, size_y),
                           (size_x + 0.5*sqrt(2)*r +0.25*l, size_y+0.5*sqrt(2)*r),
                           (size_x +0.25*l, size_y + r)),
                segment((size_x +0.25*l, size_y + r),(size_x - 0.25*l, size_y + r)),
                circle_arc((size_x - 0.25*l, size_y + r),
                           (size_x - 0.5*sqrt(2)*r -0.25*l, size_y+0.5*sqrt(2)*r),
                           (size_x - r -0.25*l, size_y)),
                circle_arc((size_x - r -0.25*l, size_y),
                           (0, 1.25*l),
                           (-size_x + r , size_y)),
                circle_arc((-size_x+r,size_y),
                           (-size_x,size_y+r),
                           (-size_x-r,size_y)),
                polysegment([(-size_x-r,size_y),
                             (-size_x -r -0.25*l,1.5*l),
                             (-size_x -r -0.25*l,0) ])
        ])

    base = sew([ line,line.rotateX(pi) ]).fill().extrude(h,center=False)

    base -= cylinder(r_b,h,False).moveX(size_x+0.25*l).moveY(size_y)
    base -= box([0.5*l,2*r_b,2*h],center=True).move(size_x,size_y,h)
    base -= cylinder(r_b,h,False).moveX(size_x-0.25*l).moveY(size_y)

    base -= cylinder(r_b,h,False).moveX(size_x+0.25*l).moveY(-size_y)
    base -= box([0.5*l,2*r_b,2*h],center=True).move(size_x,-size_y,h)
    base -= cylinder(r_b,h,False).moveX(size_x-0.25*l).moveY(-size_y)

    base -= cylinder(r_b,h,False).moveX(-size_x).moveY(size_y)
    base -= cylinder(r_b,h,False).moveX(-size_x).moveY(-size_y)

    line2 = sew([segment((size_x+r+0.25*l,0,0),(size_x+r+0.25*l,0,h+R)),
                circle_arc((size_x+r+0.25*l,0,h+R),
                           (size_x+r+0.25*l-R,0,h+2*R),
                           (size_x+r+0.25*l-2*R,0,h+R)),
                circle_arc((size_x+r+0.25*l-2*R,0,h+R),
                            (0,0,h),
                            (-size_x -r-0.25*l+2*R,0,h+R)),
                circle_arc((-size_x-r-0.25*l+2*R,0,h+R),
                           (-size_x-r-0.25*l+R,0,h+2*R),
                           (-size_x-r-0.25*l,0,h+R)),
                segment((-size_x-r-0.25*l,0,h+R),(-size_x-r-0.25*l,0,0)),
                segment((-size_x-r-0.25*l,0,0),(size_x+r+0.25*l,0,0))
                ]).fill()

    base += line2.extrude((0,-0.5*l,0)).moveY(0.25*l)
    base += line2.extrude((0,-0.5*l,0)).moveY(1.25*l)
    base += line2.extrude((0,0.5*l,0)).moveY(-1.25*l)

    base -= cylinder(r_b,5*l,True).rotateX(0.5*pi).moveX(-size_x).moveZ(h+R)
    base -= cylinder(r_b,5*l,True).rotateX(0.5*pi).moveX(size_x).moveZ(h+R)
    return unify(base)

def stick_blue(R=6,r_b=2,l=5, L=30):
	a = R/sqrt(2)
	line1 = sew([ circle_arc( ( a , 0 ,  a ), ( 0 , 0 , -R ),( -a ,0 , a ) ),
					  circle_arc( (-a,  0,  a ), (-R/3 , 0 , a+0.5*L  ) ,( -a, 0 , a + L) ),
 					  circle_arc( (-a,  0,  a + L),(0,0,2*a+R+L),(a,0,a +L) ),
					  circle_arc( ( a,  0,  a +L), (R/3, 0,a+0.5*L ) ,(a,0,a) )
  ]).fill()
	m = line1.extrude((0,l,0),True)
	m -= cylinder(r_b,l,True).rotX(0.5*pi)
	m -= cylinder(r_b,l,True).rotX(0.5*pi).up(2*a+L)
	
	L=38
	line1 = sew([ circle_arc( ( a , 0 ,  a ), ( 0 , 0 , -R ),( -a ,0 , a ) ),
					  circle_arc( (-a,  0,  a ), (-R/3 , 0 , a+0.5*L  ) ,( -a, 0 , a + L) ),
 					  circle_arc( (-a,  0,  a + L),(0,0,2*a+R+L),(a,0,a +L) ),
					  circle_arc( ( a,  0,  a +L), (R/3, 0,a+0.5*L ) ,(a,0,a) )
  ]).fill()
	n = line1.extrude((0,l,0),True)
	n -= cylinder(r_b,l,True).rotX(0.5*pi)
	n -= cylinder(r_b,l,True).rotX(0.5*pi).up(2*a+L)

	L =30
	m +=n.rotY(deg(13)).up(2*a+L)
	return m
    
def stick_green(R=6,r_b=2,l=5, L=40.5):
	a = R/sqrt(2)
	line = sew([ circle_arc( ( a , 0 ,  a ), ( 0 , 0 , -R ),( -a ,0 , a ) ),
					  circle_arc( (-a,  0,  a ), (-R/3 , 0 , a+0.5*L  ) ,( -a, 0 , a + L) ),
 					  circle_arc( (-a,  0,  a + L),(0,0,2*a+R+L),(a,0,a +L) ),
					  circle_arc( ( a,  0,  a +L), (R/3, 0,a+0.5*L ) ,(a,0,a) )
  ]).fill()
	m = line.extrude((0,l,0),True)
	m -= cylinder(r_b,l,True).rotX(0.5*pi)
	m -= cylinder(r_b,l,True).rotX(0.5*pi).up(2*a+L)
	return m

def stick_red(R=6,r_b=2,l=5, L=20):
	a = R/sqrt(2)
	line = sew([ circle_arc( ( a , 0 ,  a ), ( 0 , 0 , -R ),( -a ,0 , a ) ),
					  circle_arc( (-a,  0,  a ), (-R/3 , 0 , a+0.5*L  ) ,( -a, 0 , a + L) ),
 					  circle_arc( (-a,  0,  a + L),(0,0,2*a+R+L),(a,0,a +L) ),
					  circle_arc( ( a,  0,  a +L), (R/3, 0,a+0.5*L ) ,(a,0,a) )
  ]).fill()
	m = line.extrude((0,l,0),True)
	m -= cylinder(r_b,l,True).rotX(0.5*pi)
	m -= cylinder(r_b,l,True).rotX(0.5*pi).up(2*a+L)
	return m

def stick_yellow(R=6,r_b=2,l=5, L=34):
	a = R/sqrt(2)
	line1 = sew([ circle_arc( ( a , 0 ,  a ), ( 0 , 0 , -R ),( -a ,0 , a ) ),
					  circle_arc( (-a,  0,  a ), (-R/3 , 0 , a+0.5*L  ) ,( -a, 0 , a + L) ),
 					  circle_arc( (-a,  0,  a + L),(0,0,2*a+R+L),(a,0,a +L) ),
					  circle_arc( ( a,  0,  a +L), (R/3, 0,a+0.5*L ) ,(a,0,a) )
  ]).fill()
	m = line1.extrude((0,l,0),True)
	m -= cylinder(r_b,l,True).rotX(0.5*pi)
	m -= cylinder(r_b,l,True).rotX(0.5*pi).up(2*a+L)
	
	L=8.5
	line1 = sew([ circle_arc( ( a , 0 ,  a ), ( 0 , 0 , -R ),( -a ,0 , a ) ),
					  circle_arc( (-a,  0,  a ), (-R/3 , 0 , a+0.5*L  ) ,( -a, 0 , a + L) ),
 					  circle_arc( (-a,  0,  a + L),(0,0,2*a+R+L),(a,0,a +L) ),
					  circle_arc( ( a,  0,  a +L), (R/3, 0,a+0.5*L ) ,(a,0,a) )
  ]).fill()
	n = line1.extrude((0,l,0),True)
	n -= cylinder(r_b,l,True).rotX(0.5*pi)
	n -= cylinder(r_b,l,True).rotX(0.5*pi).up(2*a+L)

	L =34
	m +=n.rotY(deg(10)).up(2*a+L)
	return m


stick_blue1 = disp(stick_blue().rotY(deg(9)).move(-15,-5,13)).set_color(color(15/255, 76/255, 129/255))
stick_green1 = disp(stick_green().rotY(deg(-37.1)).move(38,-10,55)).set_color(color(75/255,139/255,59/255))
stick_red1 = disp(stick_red().rotY(deg(-25)).move(15,-5,13)).set_color(color(145/255,46/255,23/255))
stick_yellow1 = disp(stick_yellow().rotY(deg(-55.5)).move(38,-10,15)).set_color(color(1,229/255,124/255))

stick_blue2 = disp(stick_blue().rotY(deg(9)).move(-15,5,13)).set_color(color(15/255, 76/255, 129/255))
stick_green2 = disp(stick_green().rotY(deg(-37.1)).move(38,0,55)).set_color(color(75/255,139/255,59/255))
stick_red2 = disp(stick_red().rotY(deg(-25)).move(15,5,13)).set_color(color(145/255,46/255,23/255))
stick_yellow2 = disp(stick_yellow().rotY(deg(-55.5)).move(38,0,15)).set_color(color(1,229/255,124/255))


stick_green3 = disp(stick_green().rotY(deg(-37.1)).move(38,10,55)).set_color(color(75/255,139/255,59/255))
stick_yellow3 = disp(stick_yellow().rotY(deg(-55.5)).move(38,10,15)).set_color(color(1,229/255,124/255))

part1 = disp(part1()).set_color(color(83/255,86/255,84/255))
box1 = disp(box([100,100,15],center=False).move(-50,-50,-15)).set_color(color(101/255,67/255,33/255))
box2 = disp(box([100,100,15],center=False).rotateY(0.5*pi).move(51,-50,85)).set_color(color(101/255,67/255,33/255))
part2 = disp(part2().rotY(-0.5*pi).move(51,0,50-15) ).set_color(color(83/255,86/255,84/255))
show()
