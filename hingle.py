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

#def stick_1():
    

#disp(stic_1())
part1 = disp(part1()).set_color(color(0.6, 0.6, 0.8))
#part2 = disp(part2()).set_color(color(0.6, 0.6, 0.8))
show()
