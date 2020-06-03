#!/usr/bin/env python

from graphics import *
global __master
#Embedded from drawer.py
#default configuration
__fill=color_rgb(255,255,255)
__width=1
__outline=color_rgb(0, 0, 0)
__font='helvetica'
__font_size=12
__font_style="normal"
__font_color=color_rgb(0, 0, 0)
__init_point_poiner=(100,100)
#variable controlling unit

#tScript format
#declaring a variable
#	var __name_of_the_variable__ __value_of_the_variable__
#updating its value
#	update __name_of_the_variable__ __new_value_for_the_variable__
#using a variable
#	just type it anywhere with a @
#i.e
#	text #center @__name_of_the_variable__
variable_dictionary={}
def var_name_validation(string):
	string=str(string)
	for i in [0,1,2,3,4,5,6,7,8,9,'+','-','*','/','\\','!','@','#','$','%','^','&','(',')','{','}','{','}','=',',','.','?',':',';']:
		if string.startswith(str(i)):
			return False
	if string in ["vHeight","vWidth","vCenter","vTitle"]:
		return False

	return True
def set_variable(name,value,dictionary=variable_dictionary):
	if type(value)==type(""):
		if value.startswith("$"):
			value=value[1:]
			value=str(value)
		else:
			try:
				value=str(eval(str(value)))
			except SyntaxError:
				value=str(value)
			except NameError:
				value=str(value)
			except TypeError:
				value=str(value)
	elif type(value)==type(0):
		value=str(value)
	elif type(value)==type(10.5):
		value=str(value)
	if var_name_validation(str(name)):
		dictionary[str(name)]=value
	else:
		print('Name \'{}\' is not valid. '.format(name))

def get_variable(name,dictionary=variable_dictionary):
	try:
		return dictionary[str(name)]
	except KeyError:
		print("Variable \'{}\' is not defined.".format(name))
		return None
def update_variable(name,new_val,dictionary=variable_dictionary):
	if name in dictionary.keys():
		dictionary[name]=new_val
	else:
		print("Name '{}' is not defined.".format(name))

def check_variable(name,dictionary=variable_dictionary):
	if name in dictionary.keys():
		return True
	else:
		False

def flush_var(command,dictionary=variable_dictionary):
	command=str(command)
	for i in dictionary.keys():
		if "@"+str(i) in command:
			command=command.replace("@{}".format(i),dictionary[i])
	for i in command.split():
		if str(i).startswith("@"):
			name=str(i).replace("@", "")
			if check_variable(name):
				pass
			else:
				print("Variable name '{}' is not defined but used.".format(name))
	return command

#drawable objects unit
def __p():
	pass

def canvas(title,width,height):
	global __master
	__master=GraphWin(title,width,height)

def fill(color):
	global __fill
	global __font_color
	__fill=color
def outline(color):
	global __outline
	__outline=color
def width(px):
	global __width
	__width=px
def font_name(name):
	global __font
	__font=name
def font_size(px):
	global __font_size
	__font_size=px
def font_style(style):
	global __font_style
	__font_style=style
def font_color(color):
	global __font_color
	__font_color=color
def rectangle(sX,sY,width,height):
	rec=Rectangle(Point(sX,sY), Point(sX+width,sY+height))
	rec.setFill(__fill)
	rec.setOutline(__outline)
	rec.setWidth(__width)
	rec.draw(__master)
	return rec

def circle(sX,sY,radius):
	cir=Circle(Point(sX,sY), radius)
	cir.setFill(__fill)
	cir.setOutline(__outline)
	cir.setWidth(__width)
	cir.draw(__master)
	return cir

def triangle(aX,aY,bX,bY,cX,cY):
	tri=Polygon(Point(aX,aY),Point(bX,bY),Point(cX,cY))
	tri.setFill(__fill)
	tri.setOutline(__outline)
	tri.setWidth(__width)
	tri.draw(__master)
	return tri

def square(sX,sY,a):
	squ=Rectangle(Point(sX,sY), Point(sX+a,sY+a))
	squ.setFill(__fill)
	squ.setOutline(__outline)
	squ.setWidth(__width)
	return squ

def straight_line(sX,sY,length):
	lin=Line(Point(sX,sY), Point(sX+length,sY))
	lin.setFill(__fill)
	lin.setOutline(__outline)
	lin.setWidth(__width)
	lin.draw(__master)
	return lin

def line(sX,sY,eX,eY):
	lin=Line(Point(sX,sY), Point(eX,eY))
	lin.setFill(__fill)
	lin.setOutline(__outline)
	lin.setWidth(__width)
	lin.draw(__master)
	return lin

def text(sX,sY,text="Foo"):
	tex=Text(Point(sX,sY), text)
	tex.setFace('times roman')
	tex.setTextColor(__font_color)
	tex.setSize(__font_size)
	tex.setStyle(__font_style)
	tex.draw(__master)
	return tex

def pointer(sX,sY):
	global __init_point_poiner
	__init_point_poiner=(sX,sY)
def stroke(string):
	global __init_point_poiner
	string=str(string)
	if string.startswith("+") and string.endswith("vertical"):
		i=string.replace("+", "")
		i=i.replace("vertical", "")
		line(__init_point_poiner[0],__init_point_poiner[1],__init_point_poiner[0], __init_point_poiner[1]-int(i))
		
	elif string.startswith("-") and string.endswith("vertical"):
		i=string.replace("-", "")
		i=i.replace("vertical", "")
		line(__init_point_poiner[0],__init_point_poiner[1],__init_point_poiner[0], __init_point_poiner[1]+int(i))
		
	elif string.startswith("+") and string.endswith("horizontal"):
		i=string.replace("+", "")
		i=i.replace("horizontal", "")
		line(__init_point_poiner[0], __init_point_poiner[1], __init_point_poiner[0]+int(i), __init_point_poiner[1])
		
	elif string.startswith("-") and string.endswith("horizontal"):
		i=string.replace("-", "")
		i=i.replace("horizontal", "")
		line(__init_point_poiner[0], __init_point_poiner[1], __init_point_poiner[0]-int(i), __init_point_poiner[1])
		
	else:
		print("stroke $length $direction")		
def waitForMouse():
	try:
		__master.getMouse()
	except GraphicsError:
		pass
def readKey():
	key=__master.getKey()
	return key
def close():
	__master.close()

def evalAll(lst):
	for i in range(len(lst)):
		lst[i]=str(eval(lst[i]))
	return lst
def trigByKey(key,func=__p):
	try:
		while readKey()!=str(key):
			pass
		func()
	except GraphicsError:
		pass
def trigByClick(func):
	waitForMouse()
	func()

from sys import argv
from time import sleep
arguments=argv[1:]
version="tScript 1.0.0"
global file_path
try:
	if arguments[0]=="-h" or arguments[0]=="--help":
		print("visit github.com/NurTasin/tScript for help.")
		print("We don't recommend you to use this compiler as it is still under development and it has no stable release.")
		quit()
	elif arguments[0]=="--copyright":
		print("Copyright 2020 Nur Mahmud Ul Alam Tasin.")
		quit()
	elif arguments[0]=="--version" or arguments[0]=="-v":
		print(version)
		quit()
except:
	pass

try:
	file_path=arguments[0]
except IndexError:
	print("No script given!")
	quit()
#for argument in arguments:
#	if argument.startswith("path="):
#		file_path=argument.replace("path=", "")
#		file_path=file_path.replace("\"", "")
if file_path=="":
	print("path argument can't be empty")
	exit(1)
global vCenter
global vHeight
global vWidth
global vTitle
ifCanvasDec=False
commentStarted=False
if file_path in ["-h","--help","-v","--version","--copyright"]:
	exit()
inpFile=open(file_path,"r")
commands=inpFile.readlines()
lineNum=1
#main magic happens here
for command in commands:
	if command.startswith("canvas ") and not commentStarted: #brings the canvas
		i=command[len("canvas "):]
		i=flush_var(i)
		try:
			vWidth=int(eval(i.split()[0]))
			vHeight=int(eval(i.split()[1]))
			vTitle=str(" ".join(i.split()[2:]))
			vCenter=(vWidth//2,vHeight//2)
			__init_point_poiner=vCenter
		except:
			print("Error while declaring canvas properties at line {} of {}".format(lineNum,file_path))
			exit()
		ifCanvasDec=True
		canvas(vTitle,vWidth,vHeight)
	elif command.startswith("triangle ") and not commentStarted and ifCanvasDec: #draws a triangle on the canvas
		i=command[len("triangle "):]
		i=flush_var(i)
		i=i.replace("center ",str(vCenter))
		i=i.replace("top", "0")
		i=i.replace("bottom", str(vHeight))
		i=i.replace("left", "0")
		i=i.replace("right", str(vWidth))
		i=i.replace("title", str(vTitle))
		try:
			i=i.replace("(", "")
			i=i.replace(")", "")
			i=i.replace(",", " ")
			coords=i.split()
			coords=evalAll(coords)
			for i in range(len(coords)):
				coords[i]=int(coords[i])
			if ifCanvasDec:
				triangle(coords[0],coords[1],coords[2],coords[3],coords[4],coords[5])
		except:
			print("Error while drawing triangle at line {} of {}".format(lineNum,file_path))
	elif command.startswith("circle ")  and not commentStarted and ifCanvasDec: #drawing the circle on the canvas
		i=command[len("circle "):]
		i=flush_var(i)
		i=i.replace("center",str(vCenter))
		i=i.replace("top", "0")
		i=i.replace("bottom", str(vHeight))
		i=i.replace("left", "0")
		i=i.replace("right", str(vWidth))
		i=i.replace("title", str(vTitle))
		try:
			i=i.replace("(", "")
			i=i.replace(")", "")
			i=i.replace(",", " ")
			coords=i.split()
			coords=evalAll(coords)
			for i in range(len(coords)):
				coords[i]=int(coords[i])
			if ifCanvasDec:
				circle(coords[0],coords[1],coords[2])
		except:
			print("Error while drawing circle at line {} of {}".format(lineNum,file_path))
	elif command.startswith("rectangle ") and not commentStarted and ifCanvasDec:#drawing a rectangle on the canvas
		i=command[len("rectangle "):]
		i=flush_var(i)
		i=i.replace("center", str(vCenter))
		i=i.replace("top", "0")
		i=i.replace("bottom", str(vHeight))
		i=i.replace("left", "0")
		i=i.replace("right", str(vWidth))
		i=i.replace("title", str(vTitle))
		try:
			i=i.replace("(", "")
			i=i.replace(")", "")
			i=i.replace(",", " ")
			coords=i.split()
			coords=evalAll(coords)
			for i in range(len(coords)):
				coords[i]=int(coords[i])
			if ifCanvasDec:
				rectangle(coords[0],coords[1],coords[2],coords[3])
		except:
			print("Error while drawing rectangle at line {} of {}".format(lineNum,file_path))
	elif command.startswith("line ") and not commentStarted and ifCanvasDec: #drawing a line on the canvas
		i=command[len("line "):]
		i=flush_var(i)
		i=i.replace("center", str(vCenter))
		i=i.replace("top", "0")
		i=i.replace("bottom", str(vHeight))
		i=i.replace("left", "0")
		i=i.replace("right", str(vWidth))
		i=i.replace("title", str(vTitle))
		try:
			i=i.replace("(", "")
			i=i.replace(")", "")
			i=i.replace(",", " ")
			coords=i.split()
			coords=evalAll(coords)
			for i in range(len(coords)):
				coords[i]=int(coords[i])
			if ifCanvasDec:
				line(coords[0],coords[1],coords[2],coords[3])
		except:
			print("Error while drawing line at line {} of {}".format(lineNum,file_path))
	elif command.startswith("square ")  and not commentStarted and ifCanvasDec: #drawing a square on the canvas
		i=command[len("square "):]
		i=flush_var(i)
		i=i.replace("center", str(vCenter))
		i=i.replace("top", "0")
		i=i.replace("bottom", str(vHeight))
		i=i.replace("left", "0")
		i=i.replace("right", str(vWidth))
		i=i.replace("$title", str(vTitle))
		try:
			i=i.replace("(", "")
			i=i.replace(")", "")
			i=i.replace(",", " ")
			coords=i.split()
			coords=evalAll(coords)
			for i in range(len(coords)):
				coords[i]=int(coords[i])
			if ifCanvasDec:
				square(coords[0],coords[1],coords[2])
		except:
			print("Error while drawing square at line {} of {}".format(lineNum,file_path))
	elif command.startswith("text ")  and not commentStarted and ifCanvasDec: #drawing a text on the canvas
		i=command[len("text "):]
		i=flush_var(i)
		i=i.replace("center", str(vCenter))
		i=i.replace("top", "0")
		i=i.replace("bottom", str(vHeight))
		i=i.replace("left", "0")
		i=i.replace("right", str(vWidth))
		i=i.replace("$title", str(vTitle))
		try:
			i=i.replace("(", "")
			i=i.replace(")", "")
			i=i.replace(",", " ")
			coords=i.split()
			coords[0]=eval(coords[0])
			coords[1]=eval(coords[1])
			coords[0]=int(coords[0])
			coords[1]=int(coords[1])
			text_=" ".join(coords[2:])
			if ifCanvasDec:
				text(coords[0],coords[1],text_)
		except:
			print("Error while adding text label at line {} of {}".format(lineNum,file_path))
	elif command.startswith("//"): #line comment
		pass
	elif command.startswith("/*"): #block comment starting
		commentStarted=True
	elif command.endswith("*/"): #block comment ending
		commentStarted=False
	elif commentStarted:
		pass
	elif command.startswith("wait ") and not commentStarted and ifCanvasDec: #stops the execution until event
		i=command[len("wait "):]
		i=flush_var(i)
		com=i.split()
		if len(com)==1:
			try:
				com[0]=eval(com[0])
				sleep(int(com[0]))
			except:
				print(" wait $seconds excepted but not given.")
		elif len(com)==2:
			if com[0]=="mouse" and com[1]=="click":
				waitForMouse()
			elif com[0]=="key":
				key=str(com[1])
				trigByKey(key)
			else:
				print("'wait mouse click' or 'wait key $key' or 'wait $seconds' excepted but given `{}`\nError at line {}".format(command,lineNum))
		else:
			print("'wait mouse click' or 'wait key $key' or 'wait $seconds' excepted but given `{}`\nError at line {}".format(command,lineNum))
	elif command.startswith("font ") and not commentStarted and ifCanvasDec: #changes the font family
		i=command[len("font "):]
		i=i.replace("\n","")
		i=flush_var(i)
		if i.lower() in ['helvetica','arial','courier','times roman']:
			font_name(i.lower())
		else:
			print("The font face `{}` is not supported in tScript. Using Arial instead.\n[helvetica,arial,courier,times roman] are supported".format(i))
			font_name('arial')
	elif command.startswith("font_size ") and not commentStarted and ifCanvasDec: #declares the font size
		i=command[len("font_size "):]
		i=i.replace("\n","")
		i=flush_var(i)
		try:
			i=eval(i)
			if 5<=int(i)<=36:
				font_size(int(i))
			else:
				print("The font size is too small or too large for the canvas.")
		except:
			print("font size $size required but not got. @ line {}".format(lineNum))
	elif command.startswith("font_style ") and not commentStarted and ifCanvasDec: #declares the font style
		i=command[len("font_style "):]
		i=i.replace("\n", "")
		i=flush_var(i)
		try:
			if i.lower() in ['bold','normal','italic', 'bold italic']:
				font_style(i.lower())
			else:
				print("style `{}` is not supported by tScript.".format(i))
		except:
			print("font style $style is required but got an integer @line {}".format(lineNum))
	elif command.startswith("font_color ") and not commentStarted and ifCanvasDec: #declares the font color
		i=command[len("font_color "):]
		i=i.replace("\n", "")
		i=flush_var(i)
		if i.startswith("#") and len(i)==7:
			font_color(str(i))
		elif not i.startswith("#"):
			print("font color $HTML_Color_Code required but not got.@line {}".format(lineNum))
		elif len(i)!=7:
			print("font color $HTML_Color_Code here length must be 7 characters.@line {}".format(lineNum))
	elif command.startswith("fill ") and not commentStarted and ifCanvasDec: #declare the fill color
		i=command[len("fill "):]
		i=i.replace("\n", "")
		i=flush_var(i)
		if i.startswith("#") and len(i)==7:
			fill(str(i))
		elif not i.startswith("#"):
			print("fill $HTML_Color_Code required but not got.@line {}".format(lineNum))
		elif len(i)!=7:
			print("fill $HTML_Color_Code here length must be 7 characters.@line {}".format(lineNum))
	elif command.startswith("outline ") and not commentStarted and ifCanvasDec: #declares the outline color
		i=command[len("outline "):]
		i=i.replace("\n", "")
		i=flush_var(i)
		if i.startswith("#") and len(i)==7:
			outline(str(i))
		elif not i.startswith("#"):
			print("outline $HTML_Color_Code required but not got.@line {}".format(lineNum))
		elif len(i)!=7:
			print("outline $HTML_Color_Code here length must be 7 characters.@line {}".format(lineNum))		
	elif command.startswith("width ") and not commentStarted and ifCanvasDec: #declares the width of strokes or outlines
		i=command[len("width "):]
		i=i.replace("\n","")
		i=flush_var(i)
		try:
			i=eval(i)
			width(int(i))
		except:
			print("width $pixel is required got a string instead.@line {}".format(lineNum))
	elif command.startswith("stroke ") and not commentStarted and ifCanvasDec: #strokes on the canvas
		i=command[len("stroke "):]
		i=i.replace("\n", "")
		i=flush_var(i)
		try:
			stroke(i)
		except:
			print("Error while stroking on the canvas. @line:{}".format(lineNum))
	elif command.startswith("pointer ") and not commentStarted and ifCanvasDec: #points on a point to stroke from
		i=command[len("pointer "):]
		i=i.replace("\n", "")
		i=flush_var(i)
		i=i.replace("(", "")
		i=i.replace(")", "")
		i=i.replace(","," ")
		coords=i.split()
		coords[0]=eval(coords[0])
		coords[1]=eval(coords[1])
		coords[0]=int(coords[0])
		coords[1]=int(coords[1])
		try:
			pointer(coords[0],coords[1])
		except:
			print("Error while setting the pointer co-ordinates @ line: {}".format(lineNum))
	elif command.startswith("var ") and not commentStarted: #declares a variable
		i=command[len("var "):]
		coords=i.split()
		coords[0]=str(coords[0])
		i=i[len(coords[0])+1:]
		set_variable(coords[0], i)
	elif command.startswith("update ") and not commentStarted: #updates a variable
		i=command[len("update "):]
		coords=i.split()
		coords[0]=str(coords[0])
		i=i.replace(str(coords[0]), "")
		update_variable(coords[0], i)
	else:
		if not commentStarted and ifCanvasDec:
			print("\'{}\' not recognized as an internal command".format(command))
	lineNum+=1
if not ifCanvasDec:
	print("You have to declare the canvas properties first. try `tScript -h` for help")
