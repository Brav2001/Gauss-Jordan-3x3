#------Metodo de eliminación de Gauss-Jordan 3x3--------------
#------Autor: Brayan Acosta Vivas-----------------------------
from tkinter import *
from tkinter import scrolledtext

raiz=Tk();
raiz.resizable(False,False)
raiz.geometry("650x700")
raiz.title("GAUSS-JORDAN 3X3")
miframe=Frame(raiz)
miframe.pack()
mires=Frame(raiz)
mires.pack()
#--------------------------label para el título del programa------------------------
titulo=Label(miframe,text="MÉTODO DE ELIMINACIÓN DE GAUSS-JORDAN PARA SISTEMA 3X3")
titulo.grid(row=1,column=1,columnspan=9,padx=10,pady=10)
#-------------------------declaración de las variables, entry y label de la primera ecuación-------- 

vx1=StringVar()
vy1=StringVar()
vz1=StringVar()
vw1=StringVar()
Ec1=Label(miframe,text="Ec1: ")
Ec1.grid(row=3,column=1,pady=5)
x1=Entry(miframe,textvariable=vx1)
x1.grid(row=3,column=2,pady=5)
xt1=Label(miframe,text="x")
xt1.grid(row=3,column=3,pady=5)
y1=Entry(miframe,textvariable=vy1)
y1.grid(row=3,column=4,pady=5)
yt1=Label(miframe,text="y")
yt1.grid(row=3,column=5,pady=5)
z1=Entry(miframe,textvariable=vz1)
z1.grid(row=3,column=6,pady=5)
zt1=Label(miframe,text="z")
zt1.grid(row=3,column=7,pady=5)
wt1=Label(miframe,text="=")
wt1.grid(row=3,column=8,pady=5)
w1=Entry(miframe,textvariable=vw1)
w1.grid(row=3,column=9,pady=5)

#-------------------------declaración de las variables, entry y label de la segunda ecuación-------- 
vx2=StringVar()
vy2=StringVar()
vz2=StringVar()
vw2=StringVar()
Ec2=Label(miframe,text="Ec2: ")
Ec2.grid(row=4,column=1,pady=5)
x2=Entry(miframe,textvariable=vx2)
x2.grid(row=4,column=2,pady=5)
xt2=Label(miframe,text="x")
xt2.grid(row=4,column=3,pady=5)
y2=Entry(miframe,textvariable=vy2)
y2.grid(row=4,column=4,pady=5)
yt2=Label(miframe,text="y")
yt2.grid(row=4,column=5,pady=5)
z2=Entry(miframe,textvariable=vz2)
z2.grid(row=4,column=6,pady=5)
zt2=Label(miframe,text="z")
zt2.grid(row=4,column=7,pady=5)
wt2=Label(miframe,text="=")
wt2.grid(row=4,column=8,pady=5)
w2=Entry(miframe,textvariable=vw2)
w2.grid(row=4,column=9,pady=5)

#-------------------------declaración de las variables, entry y label de la tercera ecuación-------- 
vx3=StringVar()
vy3=StringVar()
vz3=StringVar()
vw3=StringVar()
Ec3=Label(miframe,text="Ec3: ")
Ec3.grid(row=5,column=1,pady=5)
x3=Entry(miframe,textvariable=vx3)
x3.grid(row=5,column=2,pady=5)
xt3=Label(miframe,text="x")
xt3.grid(row=5,column=3,pady=5)
y3=Entry(miframe,textvariable=vy3)
y3.grid(row=5,column=4,pady=5)
yt3=Label(miframe,text="y")
yt3.grid(row=5,column=5,pady=5)
z3=Entry(miframe,textvariable=vz3)
z3.grid(row=5,column=6,pady=5)
zt3=Label(miframe,text="z")
zt3.grid(row=5,column=7,pady=5)
wt3=Label(miframe,text="=")
wt3.grid(row=5,column=8,pady=5)
w3=Entry(miframe,textvariable=vw3)
w3.grid(row=5,column=9,pady=5)

textres=scrolledtext.ScrolledText(mires,width=69, height=30)
textres.grid(row=1,column=1)
textres.config(font=("cambria",11))
#--------método que valida el tipo de dato introducido-------
error=False
def validar(dato):
	global error
	try:
		return round(float(dato),4)
	except:
		error=True
		return None
#--------método que valida el determinate de la matriz-------
def determinante(x1,x2,x3,y1,y2,y3,z1,z2,z3):
	det=((x1*y2*z3)+(x2*y3*z1)+(x3*y1*z2))-((x2*y1*z3)+(x1*y3*z2)+(x3*y2*z1))
	return det  			

#--------método que imprime el paso a paso-------
def imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3):
	imp="\n│ "+str(x1)+"\t"+str(y1)+"\t"+str(z1)+"\t¦ "+str(w1)+"\t│ "+if1+"\n│ "+str(x2)+"\t"+str(y2)+"\t"+str(z2)+"\t¦ "+str(w2)+"\t│ "+if2+"\n│ "+str(x3)+"\t"+str(y3)+"\t"+str(z3)+"\t¦ "+str(w3)+"\t│ "+if3+"\n"
	textres.config(state="normal")
	textres.insert(INSERT,imp)
	textres.config(state="disable")
#--------método que imprime el valor de x,y,z-------
def respuesta(w1,w2,w3):
	imp="\nX = "+str(w1)+"\nY = "+str(w2)+"\nZ = "+str(w3)
	textres.config(state="normal")
	textres.insert(INSERT,imp)
	textres.config(state="disable")
#--------solución usando los 9 pasos-------
def solucion(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3):
	if1=""
	if2=""
	if3=""
	i=1
	while(i<=9):
		if i==1:
			if(x1==1):
				i=i+1
				continue
			else:
				if(x2==1):
					if1="f1«»f2"
					imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
					temp=x2
					x2=x1
					x1=temp
					temp=y2
					y2=y1
					y1=temp
					temp=z2
					z2=z1
					z1=temp
					temp=w2
					w2=w1
					w1=temp
					i=i+1
					continue
				elif(x3==1):
					if1="f1«»f3"
					imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
					temp=x3
					x3=x1
					x1=temp
					temp=y3
					y3=y1
					y1=temp
					temp=z3
					z3=z1
					z1=temp
					temp=w3
					w3=w1
					w1=temp
					i=i+1
					continue
				elif(x1!=0):
					a=round(1/x1,4)
					if1=str(a)+"f1"
					imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
					x1=round(x1*a,4)
					y1=round(y1*a,4)
					z1=round(z1*a,4)
					w1=round(w1*a,4)
					i=i+1
					continue
				elif(x1==0):
					if(x2!=0):
						if1="f1«»f2"
						imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
						temp=x2
						x2=x1
						x1=temp
						temp=y2
						y2=y1
						y1=temp
						temp=z2
						z2=z1
						z1=temp
						temp=w2
						w2=w1
						w1=temp
						a=round(1/x1,4)
						if1=str(a)+"f1"
						imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
						x1=round(x1*a,4)
						y1=round(y1*a,4)
						z1=round(z1*a,4)
						w1=round(w1*a,4)
						i=i+1
						continue
					elif(x3!=0):
						if1="f1«»f3"
						imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
						temp=x3
						x3=x1
						x1=temp
						temp=y3
						y3=y1
						y1=temp
						temp=z3
						z3=z1
						z1=temp
						temp=w3
						w3=w1
						w1=temp
						a=round(1/x1,4)
						if1=str(a)+"f1"
						imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
						x1=round(x1*a,4)
						y1=round(y1*a,4)
						z1=round(z1*a,4)
						w1=round(w1*a,4)
						i=i+1
						continue
		elif i==2:
			if x2==0:
				i=1+i
				continue
			else:
				a=x2
				if1=""
				if2="f2 -("+str(a)+")f1"
				imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
				x2=round(x2-(a*x1),4)
				y2=round(y2-(a*y1),4)
				z2=round(z2-(a*z1),4)
				w2=round(w2-(a*w1),4)
				i=1+i
				continue
		elif i==3:
			if x3==0:
				i=1+i
				continue
			else:
				a=x3
				if1=""
				if2=""
				if3="f3 -("+str(a)+")f1"
				imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
				x3=round(x3-(a*x1),4)
				y3=round(y3-(a*y1),4)
				z3=round(z3-(a*z1),4)
				w3=round(w3-(a*w1),4)
				i=1+i
				continue
		elif i==4:
			if(y2==1):
				i=i+1
				continue
			elif y2!=1:
				if(y3==1):
					if1=""
					if3=""
					if2="f2«»f3"
					imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
					temp=x2
					x2=x3
					x3=temp
					temp=y2
					y2=y3
					y3=temp
					temp=z2
					z2=z3
					z3=temp
					temp=w2
					w2=w3
					w3=temp
					i=i+1
					continue
				
				elif(y2!=0):
					a=round(1/y2,4)
					if1=""
					if3=""
					if2=str(a)+"f2"
					imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
					x2=round(x2*a,4)
					y2=round(y2*a,4)
					z2=round(z2*a,4)
					w2=round(w2*a,4)
					i=i+1
					continue
				elif(y2==0):
					if(y3!=0):
						if1=""
						if3=""
						if2="f2«»f3"
						imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
						temp=x3
						x3=x2
						x2=temp
						temp=y3
						y3=y2
						y2=temp
						temp=z3
						z3=z2
						z2=temp
						temp=w3
						w3=w2
						w2=temp
						a=round(1/y2,4)
						if2=str(a)+"f2"
						imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
						x2=round(x2*a,4)
						y2=round(y2*a,4)
						z2=round(z2*a,4)
						w2=round(w2*a,4)
						i=i+1
						continue
		elif i==5:
			if y1==0:
				i=i+1
				continue
			else:
				a=y1
				if3=""
				if2=""
				if1="f1 -("+str(a)+")f2"
				imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
				x1=round(x1-(a*x2),4)
				y1=round(y1-(a*y2),4)
				z1=round(z1-(a*z2),4)
				w1=round(w1-(a*w2),4)
				i=i+1
				continue
		elif i==6:
			if y3==0:
				i=i+1
				continue
			else:
				a=y3
				if3="f3 -("+str(a)+")f2"
				if2=""
				if1=""
				imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
				x3=round(x3-(a*x2),4)
				y3=round(y3-(a*y2),4)
				z3=round(z3-(a*z2),4)
				w3=round(w3-(a*w2),4)
				i=i+1
				continue
		elif i==7:
			if z3==1:
				i=i+1
				continue
			else:
				a=round(1/z3,4)
				if1=""
				if2=""
				if3=str(a)+"f3"
				imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
				x3=round(x3*a,4)
				y3=round(y3*a,4)
				z3=round(z3*a,4)
				w3=round(w3*a,4)
				i=i+1
				continue
		elif i==8:
			if z2==0:
				i=i+1
				continue
			else:
				a=z2
				if2="f2 -("+str(a)+")f3"
				if3=""
				if1=""
				imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
				x2=round(x2-(a*x3),4)
				y2=round(y2-(a*y3),4)
				z2=round(z2-(a*z3),4)
				w2=round(w2-(a*w3),4)
				i=i+1
				continue
		elif i==9:
			if z1==0:
				if2=""
				if3=""
				if1=""
				imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
				i=i+1
				break
			else:
				a=z1
				if2=""
				if3=""
				if1="f1 -("+str(a)+")f3"
				imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
				x1=round(x1-(a*x3),4)
				y1=round(y1-(a*y3),4)
				z1=round(z1-(a*z3),4)
				w1=round(w1-(a*w3),4)
				if2=""
				if3=""
				if1=""
				imprimir(x1,x2,x3,y1,y2,y3,z1,z2,z3,w1,w2,w3,if1,if2,if3)
				i=i+1
				break
	respuesta(w1,w2,w3)
#--------método principal------
def matriz():
	textres.config(state="normal")
	textres.delete("1.0","end")
	textres.config(state="disable")
	global error
	#---Invocación del método validar---
	x_1=validar(vx1.get())
	x_2=validar(vx2.get())
	x_3=validar(vx3.get())
	y_1=validar(vy1.get())
	y_2=validar(vy2.get())
	y_3=validar(vy3.get())
	z_1=validar(vz1.get())
	z_2=validar(vz2.get())
	z_3=validar(vz3.get())
	w_1=validar(vw1.get())
	w_2=validar(vw2.get())
	w_3=validar(vw3.get())
	#-----------------------------------
	if error:
		textres.config(state="normal")
		textres.insert(INSERT,"Existen variables no numericas, recuerde que para escribir decimales debe usar el punto '.' y no la coma ','")
		textres.config(state="disable")
		error=False
		return None
	det=determinante(x_1,x_2,x_3,y_1,y_2,y_3,z_1,z_2,z_3)#invocación del determinante
	if det==0.0:
		textres.config(state="normal")
		textres.insert(INSERT,"El determinante de la matriz es cero")
		textres.config(state="disable")
		return None
	solucion(x_1,x_2,x_3,y_1,y_2,y_3,z_1,z_2,z_3,w_1,w_2,w_3)#invocación del metodo determinante
#declaración del boton para el cálculo 
calc=Button(miframe,text="Calcular", command=matriz)
calc.grid(row=6,column=4,columnspan=3,padx=10,pady=10)
#----------------------------------------
textres.config(state="disable")

raiz.mainloop()