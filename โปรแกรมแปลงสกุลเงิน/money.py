from tkinter import *
from tkinter import ttk
root = Tk()
root.title("โปรแกรมแปลงสกุลเงิน")
#กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("800x500+0+0") #("กว้างxยาว+แกนx+แกนy")

#INPUT
money = IntVar()
Label(text="จำนวนเงิน (THB)",padx=10,font=30).grid(row=0,sticky=W)
et1=Entry(width=30,font=30,textvariable=money)
et1.grid(row=0,column=1)

choice = StringVar(value="โปรดเลือกสกุลเงิน")
Label(text="เลือกสกุลเงิน",padx=10,font=30).grid(row=1,sticky=W)
combo=ttk.Combobox(width=30,font=30,textvariable=choice)
combo["values"]=("EUR","JPY","USD","GBP")
combo.grid(row=1,column=1)

#OUTPUT
Label(text="ผลการคำนวณ",padx=10,font=30).grid(row=2,sticky=W)
et2=Entry(width=30,font=30)
et2.grid(row=2,column=1)


def calculate():
    amount=money.get()
    currentcy=choice.get()

    if currentcy == "EUR":
        et2.delete(0,END)
        result = ((amount*0.026),"EUR(ยูโร)")
        et2.insert(0,result)
    elif currentcy == "JPY":
        et2.delete(0,END)
        result = ((amount*3.486),"JPY(เยน)")
        et2.insert(0,result)
    elif currentcy == "USD":
        et2.delete(0,END)
        result = ((amount*0.031),"USD(ดอลล่า)")
        et2.insert(0,result)
    elif currentcy == "GBP":
        et2.delete(0,END)
        result = ((amount*0.023),"GBP(ปอนด์)")
        et2.insert(0,result)
    else :
        et2.delete(0,END)
        result = "ไม่พบข้อมูล"
        et2.insert(0,result)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)

Button(text="คำนวณ",font=30,width=15,command=calculate).grid(row=3,column=1,sticky=W)
Button(text="ล้างค่า",font=30,width=15,command=deleteText).grid(row=3,column=1,sticky=E)
root.mainloop()