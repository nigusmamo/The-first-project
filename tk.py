import tkinter as tk
from tkinter import *

win = tk.Tk()
win.configure(bg = "#17161b")

win.title("Nigus's calculator ")

equation = ""

lable_result = Label(win,width =22, height =2, text ="",font=("arial",30),bg = "white",fg = "black").pack()

def show(value):
     global equation
     equation += value
     lable_result.config(text = equation)

def clear():
    global equation
    equation = ""
    lable_result.config(text = equation)

def calculate():
     global equation
     result = ""
     if equation != "":
          try:
               result = eval(equation)
          except:
               result = "error"
               equation = ""
     lable_result.config(text = result)

Button(win,text = "C", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="red",bg = "#2a2d36",command = lambda:clear()).place(x=10,y=100)
Button(win,text = "/", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="blue",bg ="#2a2d36",command = lambda:show("/")).place(x=110,y=100)
Button(win,text = "*", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="blue",bg ="#2a2d36",command = lambda:show("*")).place(x=210,y=100)
Button(win,text = "%", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="blue",bg ="#2a2d36",command = lambda:show("%")).place(x=310,y=100)

Button(win,text = "7", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="black",bg ="#3697f5",command = lambda:show("7")).place(x=10,y=160)
Button(win,text = "8", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="black",bg ="#2a2d36",command = lambda:show("8")).place(x=110,y=160)
Button(win,text = "9", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="black",bg ="#2a2d36",command = lambda:show("9")).place(x=210,y=160)
Button(win,text = "-", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="blue",bg ="#2a2d36",command = lambda:show("-")).place(x=310,y=160)

Button(win,text = "4", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="black",bg ="#3697f5",command = lambda:show("4")).place(x=10,y=220)
Button(win,text = "5", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="black",bg ="#2a2d36",command = lambda:show("5")).place(x=110,y=220)
Button(win,text = "6", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="black",bg ="#2a2d36",command = lambda:show("6")).place(x=210,y=220)
Button(win,text = "+", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="blue",bg ="#2a2d36",command = lambda:show("+")).place(x=310,y=220)

Button(win,text = "1", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="black",bg ="#3697f5",command = lambda:show("1")).place(x=10,y=280)
Button(win,text = "2", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="black",bg ="#2a2d36",command = lambda:show("2")).place(x=110,y=280)
Button(win,text = "3", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="black",bg ="#2a2d36",command = lambda:show("3")).place(x=210,y=280)
Button(win,text = "0", width = 9, height = 1,font = ("arial",30,"bold"),bd =1,fg="black",bg ="#2a2d36",command = lambda:show("0")).place(x=10,y=340)

Button(win,text = ".", width = 3, height = 1,font = ("arial",30,"bold"),bd =1,fg="black",bg ="#2a2d36",command = lambda:show(".")).place(x=210,y=340)
Button(win,text = "=", width = 3, height = 3,font = ("arial",30,"bold"),bd =1,fg="green",bg ="red",command = lambda: calculate()).place(x=310,y=275)

win.mainloop()
