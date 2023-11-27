from tkinter import*




r=Tk()
r.geometry("570x600+100+200")
r.configure(bg="black")
r.title("simple calculator")
r.resizable(0,0)
equation=""
def clear():
   global equation
   equation=""
   Label_result.config(text=equation)
   
   

def show(value):
    global equation
    equation+=value
    Label_result.config(text=equation)
def calculate():
    global equation
    result=eval(equation)
    Label_result.config(text=result)

Label_result=Label(r,width=25,height=2,text="",font=("arial",30))
Label_result.pack()

Button1=Button(r,width=5,height=1,text="C",bg="#3697F5",fg="#fff",font=("arial",30),command=clear)
Button1.place(x=5,y=100)
Button2=Button(r,width=5,height=1,text="/",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("/"))
Button2.place(x=145,y=100)
Button3=Button(r,width=5,height=1,text="%",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("%"))
Button3.place(x=285,y=100)
Button3=Button(r,width=5,height=1,text="*",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("*"))
Button3.place(x=430,y=100)
Button4=Button(r,width=5,height=1,text="7",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("7"))
Button4.place(x=5,y=195)
Button5=Button(r,width=5,height=1,text="8",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("8"))
Button5.place(x=145,y=195)
Button6=Button(r,width=5,height=1,text="9",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("9"))
Button6.place(x=285,y=195)
Button7=Button(r,width=5,height=1,text="-",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("-"))
Button7.place(x=430,y=195)
Button8=Button(r,width=5,height=1,text="4",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("4"))
Button8.place(x=5,y=290)
Button9=Button(r,width=5,height=1,text="5",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("5"))
Button9.place(x=145,y=290)
Button10=Button(r,width=5,height=1,text="6",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("6"))
Button10.place(x=285,y=290)
Button11=Button(r,width=5,height=1,text="+",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("+"))
Button11.place(x=430,y=290)
Button11=Button(r,width=5,height=1,text="1",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("1"))
Button11.place(x=5,y=385)
Button12=Button(r,width=5,height=1,text="2",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("2"))
Button12.place(x=145,y=385)
Button13=Button(r,width=5,height=1,text="3",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("3"))
Button13.place(x=285,y=385)
Button14=Button(r,width=11,height=1,text="0",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("0"))
Button14.place(x=5,y=480)
Button15=Button(r,width=5,height=1,text=".",bg="#3697F5",fg="#fff",font=("arial",30),command=lambda:show("."))
Button15.place(x=285,y=480)
Button16=Button(r,width=5,height=3,text="=",bg="orange",fg="#fff",font=("arial",30),command=lambda:calculate())
Button16.place(x=430,y=390)





















