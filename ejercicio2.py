from tkinter import*

root= Tk()
root.geometry("1000x500+0+0")
root.title("dojo phyton3")


text_input = StringVar()
operador = ""

Tops= Frame(root, width = 1600, height = 80, bg= "powder blue",relief=SUNKEN)
Tops.pack(side = TOP)
frame= Frame(root, width = 300, height = 700, bg= "powder blue",relief=SUNKEN)
frame.pack(side = TOP)

lbinfo= Label(Tops, font=("SHOWCARD GOTHIC",50,'bold'), text = "dojo python3")
lbinfo.grid(row=0,column=0)
def btnClick(numero):
    global operador
    operador=operador + str(numero)
    text_input.set(operador)
def btneEval(numero):
    global operador
    result = str(eval(operador))
    text_input.set(result)
    operador=""

txtDisplay = Entry(frame,font=("SHOWCARD GOTHIC",20,'bold'), textvariable = text_input, bg="black")
txtDisplay.grid(columnspan=4)

btn1 = Button(frame,font=("SHOWCARD GOTHIC",20,'bold'),command= lambda:btnClick(1)).grid(row=2,column=0)
btn2 = Button(frame,font=("SHOWCARD GOTHIC",20,'bold'),command= lambda:btnClick(2)).grid(row=2,column=1)
Addition = Button(frame,font=("SHOWCARD GOTHIC",20,'bold'),command= lambda:btnClick("+")).grid(row=2,column=2)
Equials = Button(frame,font=("SHOWCARD GOTHIC",20,'bold'),command= btneEval).grid(row=2,column=3)
root.mainloop()
