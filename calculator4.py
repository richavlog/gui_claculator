

from tkinter import*
x=Tk()
x.geometry("285x430")
x.resizable(0,0)
x.title("calculator")
Y=""
def cal(val):
    global Y
    Y=Y+str(val)
    myText.set(Y)
Y=""
def eq():
    global Y
    result=str(eval(Y))
    myText.set(result)
Y=""
def clea():
    global Y
    Y=""
    myText.set("") 
Y=""
def backspace(val):
        """Remove the last character from the display."""
        Y=Y+str(val)
        a= Y[:-1]
        a.update()

myText=StringVar()
e=Entry(x,font="30",width=15,bd=14,textvariable=myText)
e.pack(fill="both")
#make buttons
b1=Button(x,text="1",font="25",bg="light blue",height=2,width=4,command=lambda:cal("1"))
b1.place(x=10,y=60)
b2=Button(x,text="2",font="25",bg="light blue",height=2,width=4,command=lambda:cal("2"))
b2.place(x=80,y=60)
b3=Button(x,text="3",font="25",bg="light blue",height=2,width=4,command=lambda:cal("3"))
b3.place(x=150,y=60)
b4=Button(x,text="4",font="25",bg="light blue",height=2,width=4,command=lambda:cal("4"))
b4.place(x=10,y=140)
b5=Button(x,text="5",font="25",bg="light blue",height=2,width=4,command=lambda:cal("5"))
b5.place(x=80,y=140)
b6=Button(x,text="6",font="25",bg="light blue",height=2,width=4,command=lambda:cal("6"))
b6.place(x=150,y=140)
b7=Button(x,text="7",font="25",bg="light blue",height=2,width=4,command=lambda:cal("7"))
b7.place(x=10,y=220)
b8=Button(x,text="8",font="25",bg="light blue",height=2,width=4,command=lambda:cal("8"))
b8.place(x=80,y=220)
b9=Button(x,text="9",font="25",bg="light blue",height=2,width=4,command=lambda:cal("9"))
b9.place(x=150,y=220)
deci=Button(x,text=".",font="25",bg="light blue",height=2,width=4,command=lambda:cal("."))
deci.place(x=10,y=290)
zero=Button(x,text="0",font="25",bg="light blue",height=2,width=4,command=lambda:cal("0"))
zero.place(x=80,y=290)


devide=Button(x,text="/",font="25",bg="light blue",height=2,width=4,command=lambda:cal("/"))
devide.place(x=220,y=290)
mul=Button(x,text="*",font="25",bg="light blue",height=2,width=4,command=lambda:cal("*"))
mul.place(x=220,y=60)
sub=Button(x,text="-",font="25",bg="light blue",height=2,width=4,command=lambda:cal("-"))
sub.place(x=220,y=140)
add=Button(x,text="+",font="25",bg="light blue",height=2,width=4,command=lambda:cal("+"))
add.place(x=220,y=220)
c=Button(x,text="C",font="25",bg="light blue",height=2,width=17,command=lambda:clea())
c.place(x=10,y=360)
delete=Button(x,text="x",font="25",bg="red",fg="white",height=2,width=4,command=lambda:backspace("self"))
delete.place(x=220,y=360)
equal=Button(x,text="=",font="25",bg="light blue",height=2,width=4,command=lambda:eq())
equal.place(x=150,y=290)


x.mainloop()