import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By

window = tkinter.Tk()
window.title("Login Form")
window.geometry('500x500+500+0')
window.configure(bg='#333333')
photo = PhotoImage(file="logo.png")
window.iconphoto(True, photo)


def login():
    username= "nan"
    password = "1"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success",message="You Successfully logged in.")
        window.destroy()
        root = Tk()
        root.title("Market")
        root.geometry("500x200+500+100") #("กว้างxยาว+แกนx+แกนy")
        root.configure(bg='#333333')
        photo = PhotoImage(file="logo.png")
        root.iconphoto(True, photo)
        
        myMenu = Menu(bg='#333333',fg="#fff")
        root.config(menu=myMenu)

        def exitProgram():
            confirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการปิดโปรแกรมหรือไม่?")
            if confirm == "yes":
                root.destroy()

        #ย่อย
        menuitem = Menu(bg='#333333',fg="#fff")
        menuitem.add_command(label="Exit",command=exitProgram)
        
        #หลัก
        myMenu.add_cascade(label="File",menu=menuitem)



        

        frame = tkinter.Frame(bg='#333333')

        headLabel = Label(frame, text="Crypto",bg='#333333',fg="#fff",font=("Arial",30)).grid(row=0,column=0,columnspan=4,sticky="news",pady=40)

        driver_asx = webdriver.Chrome()
        driver_asx.get('https://www.bitkub.com/th/market/axs')
        def pricefunc():
            name = driver_asx.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[3]/div/div[3]/div/div[2]/div[1]/div/div/button[1]/h1').text
            price = driver_asx.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[3]/div/div[3]/div/div[2]/div[2]/ul/li[1]/div/div[2]/span').text
            Hight = driver_asx.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[3]/div/div[3]/div/div[2]/div[2]/ul/li[2]/div/div[2]').text
            Low = driver_asx.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[3]/div/div[3]/div/div[2]/div[2]/ul/li[4]/div/div[2]').text

            driver_asx.refresh()
            return name,price,Hight,Low

        def update_gui():
            asx = pricefunc()
            # อัปเดต text บนหน้าจอ
            name_label.config(text="เหรียญ " + asx[0],bg="#FBFF6F")
            price_label.config(text="ราคาล่าสุด " + asx[1],bg="#BFFF7E")
            Hight_label.config(text="สุงสุด24H " + asx[2],bg="#FF9494")
            Low_label.config(text="ต่ำสุด24H " + asx[3],bg="#FFC694")
            # เรียกตัวเองซ้ำหลังจาก 3 วินาที
            frame.after(3000, update_gui)

        # สร้าง Label 
        name_label = Label(frame, text="เหรียญ")
        name_label.grid(row=1,column=0)

        price_label = Label(frame, text="ราคาล่าสุด")
        price_label.grid(row=1,column=1)

        Hight_label = Label(frame, text="สุงสุด24H")
        Hight_label.grid(row=1,column=2)

        Low_label = Label(frame, text="ต่ำสุด24H")
        Low_label.grid(row=1,column=3)

        driver_zeta = webdriver.Chrome()
        driver_zeta.get('https://www.bitkub.com/th/market/zeta')
        def pricefunc1():
            name = driver_zeta.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[3]/div/div[3]/div/div[2]/div[1]/div/div/button[1]/h1').text
            price = driver_zeta.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[3]/div/div[3]/div/div[2]/div[2]/ul/li[1]/div/div[2]/span').text
            Hight = driver_zeta.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[3]/div/div[3]/div/div[2]/div[2]/ul/li[2]/div/div[2]').text
            Low = driver_zeta.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[3]/div/div[3]/div/div[2]/div[2]/ul/li[4]/div/div[2]').text

            driver_zeta.refresh()
            return name,price,Hight,Low

        def update_gui1():
            zeta = pricefunc1()
            # อัปเดต text บนหน้าจอ
            name_label1.config(text="เหรียญ " + zeta[0],bg="#FBFF6F")
            price_label1.config(text="ราคาล่าสุด " + zeta[1],bg="#BFFF7E")
            Hight_label1.config(text="สุงสุด24H " + zeta[2],bg="#FF9494")
            Low_label1.config(text="ต่ำสุด24H " + zeta[3],bg="#FFC694")
            # เรียกตัวเองซ้ำหลังจาก 3 วินาที
            frame.after(3000, update_gui1)

        # สร้าง Label 
        name_label1 = Label(frame, text="เหรียญ")
        name_label1.grid(row=2,column=0)

        price_label1 = Label(frame, text="ราคาล่าสุด")
        price_label1.grid(row=2,column=1)

        Hight_label1 = Label(frame, text="สุงสุด24H")
        Hight_label1.grid(row=2,column=2)

        Low_label1 = Label(frame, text="ต่ำสุด24H")
        Low_label1.grid(row=2,column=3)

        # เริ่มต้นการอัปเดต GUI
        update_gui()
        update_gui1()

        frame.pack()
        root.mainloop()

    else:
        messagebox.showerror(title="Error",message="Invalid login")

frame = tkinter.Frame(bg='#333333')

login_label = tkinter.Label(frame, text="LOGIN",bg='#333333',fg="#fff",font=("Arial",30))
username_label = tkinter.Label(frame, text="Username",bg='#333333',fg="#fff",font=("Arial",16))
username_entry = tkinter.Entry(frame,font=("Arial",16),width=10)
password_entry = tkinter.Entry(frame,show="*",font=("Arial",16),width=10)
password_label = tkinter.Label(frame, text="Password",bg='#333333',fg="#fff",font=("Arial",16))
login_button = tkinter.Button(frame, text="Login",bg='#FF3399',fg="#fff",font=("Arial",16),command=login)

login_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1,pady=(5,20))
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1,pady=(5,20))
login_button.grid(row=3,column=0,columnspan=2,pady=(5,30))


frame.pack()

window.mainloop()