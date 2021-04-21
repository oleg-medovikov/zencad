#!/usr/bin/env python3
#coding: utf-8

from zencad import *
import numpy as np
from numpy import pi,sin,cos,sqrt,arctan

def gear_profile(modul, number):
	list_=[]
	def add_point(x,y,z):
		if not len(list_):
			list_.append((x,y,z))
		else:
			if (x - list_[-1][0])**2 + (y - list_[-1][1])**2 > modul:
				list_.append((x,y,z))
	d   = number*modul		   # Диаметр делительный
	h   = 2.25*modul		# Высота зуба
	ha  = modul			 # Высота головки
	hf  = 1.25*modul		# Высота ножки
	da  = d + 2*ha	  # Диаметр вершин зубьев
	df  = d - 2*hf	  # Диаметр впадин зубчатого колеса  
	db  = d*cos(pi/9)   # Диаметр основной окружности
	b   = 8*modul		   # Ширина венца зубчатого колеса
	Pt  = pi*modul		  # Окружной шаг зубьев
	St  = 0.5*Pt		# Окружная толщина зуба
	Et  = 0.5*Pt		# Окружная ширина впадины зубчатого колеса
	Qf  = 0.25*modul		# Радиус кривизны переходной кривой зуба
	# Еще параметров
	teta = 2*pi/number  # Угол дуги окружности, которую занимает зуб

	for k in range(number):
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
		d_a = arctan(-y/x)	   # угол который занимает эвольвента
		d_b = 0.5*teta - d_a	 # угол который занимает впадина или зуб
		a_max = a				# максимальный угол эвольвенты
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
		for i in range(8,16,1):
			i = pi*i/12
			x = r1*cos(i) + 0.5*(df+db)
			y = r2*sin(i)
			turn = (k+1)*teta  - 0.5*(d_a + d_b) 
			X =  x*cos(turn) + y*sin(turn)
			Y = -x*sin(turn) + y*cos(turn)
			add_point(X,Y,0)
		while True:
			# Считаем точки эвольвенты второй грани(низ зуба)
			x =  db*(cos(a) - a*sin(a))
			y = -db*(sin(a) - a*cos(a))
			# Меняем точки первой эвольвенты относительно повернутой системы координат
			turn = (k+1)*teta 
			X =  x*cos(turn) + y*sin(turn)
			Y = -x*sin(turn) + y*cos(turn)
			a -= pi/180
			if X**2 + Y**2 <= db**2 and a >= 0:
				add_point(X,Y,0)
			else:
				break
	print( "Number of points: " + str(len(list_) ) +  "\nDiametr: " + str(d))
	return polysegment(list_, closed=True)


m = gear_profile(8,42).fill().extrude(30)

disp(m)

show()
