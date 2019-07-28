#import modules
from tkinter import messagebox 
from tkinter.messagebox import showinfo
from tkinter import *
import sqlite3
from PIL import Image, ImageTk
#networking and Screen casting modules
import base64
import cv2
import zmq
import mss
import numpy 
import sys
import time
import psutil
import threading
import multiprocessing
import subprocess as ps
import socket
#demooo
import requests
import json
from flask import jsonify
#url for request


import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
h_ip = (s.getsockname()[0])
s.close()
url="http://"+h_ip+":5111"

sct = mss.mss()
monitor=(0,0,1366,756)

i=2

global user
global log_screen
user=''
# Designing window for registration
def register():
    global register_screen
    global main_screen
    global username
    global password
    global username_entry
    global password_entry
    global login_screen
    login_screen.destroy()
    register_screen = Frame(bg="white",width="1200",height="575")
    register_screen.place(x=0,y=0)
    
    username = StringVar()
    password = StringVar()
    
    #Add Cdac logo
    iconPath = 'Images/Cdac_logo.png'
    logo = ImageTk.PhotoImage(Image.open(iconPath))
    label = Label(register_screen, image = logo, width='180',height='95',bg='white')
    label.image = logo
    label.configure(image = logo)
    label.place(x=230,y=80)
    #Register Logo
    Path='Images/register.png'
    bg_img = ImageTk.PhotoImage(Image.open(Path))
    label = Label(register_screen, image = bg_img, bg='white', width='680',height='575')
    label.image = bg_img
    label.configure(image = bg_img)
    label.place(x=550,y=0)
 
    Label(register_screen, text="Register", bg="white", width="30", font=("Arial",25,"bold")).place(x=55,y=190)
    Label(register_screen, text="Username : ",font=("Arial",15),bg='white').place(x=90,y=290)
    username_entry = Entry(register_screen, textvariable=username,width="30", bd=3,font=("Times",15))
    username_entry.place(x=200,y=290)
    Label(register_screen, text="Password : ", font=("Arial",15),bg='white').place(x=90,y=350)
    password_entry = Entry(register_screen, textvariable=password, show= '*', bd=3, width="30",font=("Times",15))
    password_entry.place(x=200,y=350)
    
    Button(register_screen, text="Register", command = register_user, font=("Arial",13),width='12', height='1', borderwidth=2, relief= RAISED, activebackground = 'slate blue', activeforeground = 'white',fg='white',bg='royalblue1',cursor='hand2').place(x=185,y=450)
    Button(register_screen, text="Sign in", command=go_back_to_login, font=("Arial",13),width='12', height='1', borderwidth=2, relief= RAISED, activebackground = 'slate blue', activeforeground = 'white',fg='white',bg='royalblue1',cursor='hand2').place(x=365,y=450)

#DATABASE REGISTRATION
def register_user():
    global conn, cursor
    global lbl1
    global url
    
    username_info = username.get()
    password_info = password.get()
    if username_info == "" or password_info == "":
        lbl1.destroy()
        lbl1 = Label(text="Please complete the required field!", bg='white', fg="red", font=("ms serif", 15, "bold"))
        lbl1.place(x=150,y=240)
    elif len(password_info) < 6:
        lbl1.destroy()
        lbl1 = Label(text="Atleast 6 character in the password!!", bg='white', fg="red", font=("ms serif", 15, "bold"))
        lbl1.place(x=165,y=240)
    else:
        try:
            #post request
            payload = {'username': username_info, 'password': password_info}
            rqst = requests.post(url+"/post", data=payload)
            if rqst.status_code == 200:
                lbl1.destroy()
                lbl1 = Label(register_screen, text="Registration Successful", bg='white', fg="green", font=("ms serif", 15, "bold"))
                lbl1.place(x=200,y=400)
            elif rqst.status_code == 500:
                lbl1.destroy()
                lbl1 = Label(register_screen, text="User Already Exist!!", bg='white', fg="red", font=("ms serif", 15, "bold"))
                lbl1.place(x=200,y=400)
            else:
                lbl1.destroy()
                lbl1 = Label(register_screen, text="Registration Failed", bg='white', fg="red", font=("ms serif", 15, "bold"))
                lbl1.place(x=200,y=400)
        except:
            lbl1.destroy()
            lbl1 = Label(register_screen, text="Server is off.. Try again later!!", fg="red", bg='white', font=("ms serif", 15, "bold"))
            lbl1.place(x=165,y=240)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
def go_back_to_login():
    global register_screen
    register_screen.destroy()    
    login()
    
# Designing window for login 
 
def login():
    global login_screen
    global main_label
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    
    login_screen = Frame(bg="white",width="1200",height="575")
    login_screen.place(x=0,y=0)
    
    #Add Cdac logo
    iconPath = 'Images/Cdac_logo.png'
    logo = ImageTk.PhotoImage(Image.open(iconPath))
    label = Label(login_screen, image = logo, width='180',height='95',bg='white')
    label.image = logo
    label.configure(image = logo)
    label.place(x=230,y=150)
    #Login Logo
    Path='Images/login.png'
    bg_img = ImageTk.PhotoImage(Image.open(Path))
    label = Label(login_screen, image = bg_img, bg='white', width='680',height='575')
    label.image = bg_img
    label.configure(image = bg_img)
    label.place(x=570,y=0)
    
    username_verify = StringVar()
    password_verify = StringVar()
    
    def on_click(event):
        """function that gets called whenever entry is clicked"""
        if username_login_entry.get() == 'Username':
           username_login_entry.delete(0, "end") # delete all the text in the entry
           username_login_entry.insert(0, '') #Insert blank for user input
           username_login_entry.config(fg = 'black')
    def on_out(event):
        if username_login_entry.get() == '':
            username_login_entry.insert(0, 'Username')
            username_login_entry.config(fg = 'grey')
    username_login_entry = Entry(login_screen, textvariable=username_verify,width="35", bd=3,font=("Times",15))
    username_login_entry.insert(0, 'Username')
    username_login_entry.bind('<FocusIn>', on_click)
    username_login_entry.bind('<FocusOut>', on_out)
    username_login_entry.place(x=150,y=290)
    
    def on_pswd_click(event):
        """function that gets called whenever entry is clicked"""
        if password_login_entry.get() == 'Password':
           password_login_entry.delete(0, "end") # delete all the text in the entry
           password_login_entry.insert(0, '') #Insert blank for user input
           password_login_entry.config(fg = 'gray')
    def on_pswd_out(event):
        if password_login_entry.get() == '':
            password_login_entry.insert(0, 'Password')
            password_login_entry.config(fg = 'grey')
    #Label(login_screen, text="Password * ", font=("Times",15,'bold'),bg='white').place(x=90,y=350)
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*', bd=3, width="35",font=("Times",15))
    password_login_entry.insert(0, 'Password')
    password_login_entry.bind('<FocusIn>', on_pswd_click)
    password_login_entry.bind('<FocusOut>', on_pswd_out)
    password_login_entry.place(x=150,y=350)
    
    #forget password link
    Txt = Label(login_screen,text="Forget Password ?", height=2, width=30,bg='white',fg='blue', font=("Times",13,'bold italic'), cursor='hand2')
    Txt.place(x=190,y=490)
    Txt.bind("<Button-1>", forget_pass)
    
    Button(login_screen, text="Login",font=("Arial",13),width='15', height='1',fg='white', borderwidth=2, relief= RAISED, command = login_verify, activebackground = 'Darkorchid1', activeforeground = 'white', bg='purple',cursor='hand2').place(x=155,y=430)
    Button(login_screen, text="Register",font=("Arial",13),width='15', height='1', fg='white', borderwidth=2, relief= RAISED, command = register, activebackground = 'Darkorchid1', activeforeground = 'white', bg='purple',cursor='hand2').place(x=340,y=430)
    #port_assign()
        
        
#forget password
def forget_pass(event):
    global login_screen
    global main_screen
    global forget_screen
    global username_test
    global labelu
    global username_test
    global btn
    global new_password
    global password_enter
    
    login_screen.destroy()
    #forget screen 
    forget_screen = Frame(bg="white",width="1200",height="575")
    forget_screen.place(x=0,y=0)
    
    #Add Cdac logo
    iconPath = 'Images/Cdac_logo.png'
    logo = ImageTk.PhotoImage(Image.open(iconPath))
    label = Label(forget_screen, image = logo, width='180',height='95',bg='white')
    label.image = logo
    label.configure(image = logo)
    label.place(x=230,y=80)
    #Forget password Logo
    Path='Images/fpswd.png'
    bg_img = ImageTk.PhotoImage(Image.open(Path))
    label = Label(forget_screen, image = bg_img, bg='white', width='680',height='575')
    label.image = bg_img
    label.configure(image = bg_img)
    label.place(x=560,y=0)
    
    username_forget = StringVar()
    password_forget1 = StringVar()
    password_forget2 = StringVar()
    Label(forget_screen, text="Forget Password", width="25", font=("Arial",25,'bold'),bg='white').place(x=110,y=190) 
    labelu = Label(forget_screen, text="Username : ",font=("Arial",15),bg='white')
    labelu.place(x=90,y=290)
    username_test = Entry(forget_screen, textvariable=username_forget,width="30", bd=3,font=("Times",15))
    username_test.place(x=220,y=285)
    Label(forget_screen, text="Password : ", font=("Arial",15),bg='white').place(x=90,y=350)
    password_enter = Entry(forget_screen, textvariable=password_forget1, show= '*', bd=3, width="30",font=("Times",15))
    password_enter.place(x=220,y=345)
    Label(forget_screen, text="Confirm Password : ", font=("Arial",15),bg='white').place(x=15,y=410)
    new_password = Entry(forget_screen, textvariable=password_forget2, show= '*', bd=3, width="30",font=("Times",15))
    new_password.place(x=220,y=405)
            
    btn = Button(forget_screen, text="Submit",font=("Times",13,'bold'),width='15', height='1', borderwidth=2, relief= RAISED, command = submit_action, activebackground = 'Darkorchid1',cursor='hand2', bg='purple', fg='white')
    btn.place(x=195,y=470)
    btn = Button(forget_screen, text="Sign In",font=("Times",13,'bold'),width='15', height='1', borderwidth=2, relief= RAISED, command = login, activebackground = 'Darkorchid1', fg = 'white', bg='purple',cursor='hand2')
    btn.place(x=400,y=470)

# submit uername and further procedure
def submit_action(event=None):    
    global forget_screen
    global labelu
    global username_test
    global new_password
    global password_enter
    global btn
    global conn, cursor
    global lbl1
    
    usertest = username_test.get()
    passtest1 = password_enter.get()
    passtest2 = new_password.get()
    

    if  usertest == "" or passtest1 == "" or passtest2 == "":
        lbl1.destroy()
        lbl1 = Label(text="Please complete the required field!!", bg='white', fg="red", font=("ms serif", 15, "bold"))
        lbl1.place(x=170,y=240)
        
    else:
        try:
            if passtest1 == passtest2:            
                payload = {'username': usertest, 'password': passtest2}
                rqst = requests.put(url+"/forget", data = payload)
                if rqst.status_code == 200:
                    lbl1.destroy()
                    lbl1 = Label(forget_screen, text="Password changed!!", bg='white', fg="green", font=("ms serif", 15, "bold"))
                    lbl1.place(x=200,y=240)
                else:
                    lbl1.destroy()
                    lbl1 = Label(forget_screen, text="Please enter your valid username!", bg='white', fg="red", font=("ms serif", 15, "bold"))
                    lbl1.place(x=170,y=240)
            else:
                lbl1.destroy()
                lbl1 = Label(forget_screen, text="Password not matched!", bg='white', fg="red", font=("ms serif", 15, "bold"))
                lbl1.place(x=200,y=240)
        except:
            lbl1.destroy()
            lbl1 = Label(forget_screen, text="Server is off.. Try again later!!", fg="red", bg='white', font=("fixedsys", 15, "bold"))
            lbl1.place(x=150,y=240)
    username_test.delete(0, END)
    new_password.delete(0, END)
    password_enter.delete(0, END)
    
# Database login  
def login_verify(event=None):
    global conn, cursor
    global lbl1
    global url
    
    username1 = username_verify.get()
    password1 = password_verify.get()
    try:
        payload = {'username': username1, 'password': password1}
        response = requests.get(url+"/get", data = payload)
        if response.status_code == 200:
            login_window()
        else:
            lbl1.destroy()
            lbl1 = Label(login_screen, text="Invalid Username or Password ", fg="red", bg='white', font=("ms serif", 15, "bold"))
            lbl1.place(x=180,y=245)
    except:
        lbl1.destroy()
        lbl1 = Label(login_screen, text="Server is off.. try again later!!", fg="red", bg='white', font=("ms serif", 15, "bold"))
        lbl1.place(x=180,y=245)
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
                    

# =============================================================================
    
#login screen main program

def login_window():
    global main_screen
    global login_screen
    global username_verify
    global password_verify
    global log_screen
    global btn
    global chk_btn
    global user
    global lbl1
    
    user = username_verify.get()
    pswd = password_verify.get()
    
    lbl1.destroy()
    log_screen = Frame(bg="white",width="1200",height="575")
    log_screen.place(x=0,y=0)
    #Add Cdac logo
    iconPath = 'Images/Cdac_logo.png'
    logo = ImageTk.PhotoImage(Image.open(iconPath))
    label = Label(log_screen, image = logo, width='180',height='95',bg='white')
    label.image = logo
    label.configure(image = logo)
    label.place(x=90,y=70)
    #Login windowLogo
    Path='Images/user.png'
    bg_img = ImageTk.PhotoImage(Image.open(Path))
    label = Label(log_screen, image = bg_img, bg='white', width='680',height='575')
    label.image = bg_img
    label.configure(image = bg_img)
    label.place(x=570,y=0)
    #display day and date
    def Draw():
        global text
        text= Label(log_screen,text='Date',font=('Arial', 17), bg='white')
        text.place(x=90,y=240)

    def Refresher():
        global text
        text.configure(text=time.asctime()[4:10]+", "+time.asctime()[0:3])

    # display time
    global time1
    time1 = ''
    clock = Label(log_screen, font=('Arial', 17), bg='white')
    clock.place(x=90,y=280)
         
    def tick():
        global time1
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        clock.after(200, tick)
    
    Label(log_screen, text=f"Welcome {user}", font=("Arial",30),bg='white').place(x=90,y=195) 
    Label(log_screen, text= "Now You can Access Internet..!!",font=("Arial",23,'bold'),bg='white').place(x=90,y=320)
    
    # button for seeing bandwidth consumption
    btn = Button(log_screen, text="Speed",font=("Arial",13,'bold'), bg='white',borderwidth=1, relief= RAISED, command = bandwidth_consumption, cursor='hand2')
    btn.place(x=350,y=380)

    btn = Button(log_screen, text="cast",font=("Arial",13,'bold'), bg='white',borderwidth=1, relief= RAISED, command = casting, cursor='hand2')
    btn.place(x=450,y=380)
    
    #logout button    
    Button(log_screen, text="Logout",font=("Arial",13),width='20', height='1',bg='white', borderwidth=1, relief= RAISED, command = logout, cursor='hand2').place(x=100,y=440)
    
    tick()
    Draw()
    Refresher()
    port_assign()
    
    
def logout():
    global log_screen
    global user
    
    login()
    
    user_login={'username':user}
    rqst = requests.post(url+"/user_deactivate", data=user_login)
    
    #port_free={'username':user}
    #rqst = requests.post(url+"/delete", data=port_free)
    
    log_screen.destroy()

def get_open_port():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("",0))
	s.listen(1)
	port = s.getsockname()[1]
	s.close()
	return port

def get_ip():
    
    #linux
    x = ps.check_output("ifconfig", shell=True)
    x=str(x).split('\\n')
    c=[]
    for i in x:
        if 'inet' in i:
            c.append(i)
            
    ip = c[2][10:37].split(" ")[1]
    
    '''
    #windows
    x = ps.check_output("ipconfig", shell=True)  
    x=str(x).split('\\n')
    c=[]
    [c.append(i) for i in x if 'IPv4' in i]
    d=[]
    for i in c:
        d.append(i.split(": "))
    ip=d[0][1].replace("\\r","")
    '''
    
    return ip
        

def port_assign():
    global url1
    global url2
    global user
    
    port1 = get_open_port()
    port2 = get_open_port()
    #for popup
    port3 = get_open_port()
    ip = get_ip()
    url1 = f"tcp://{h_ip}:{port1}"
    url2 = f"tcp://{h_ip}:{port2}"
    payload = {'username':user, 'ip': ip, 'port1': port1, 'port2': port2, 'port3': port3}
    rqst = requests.post(url+"/port", data=payload)
    user_login={'username':user}
    rqst = requests.post(url+"/user_activate", data=user_login)
    if rqst.status_code == 200:
        pass
    else:
        pass
    
    global msg
    def casting_popup():
        #For popup
        s=socket.socket()
        s.bind((ip,port3))
        s.listen(5)
        c,addr=s.accept()
        msg = c.recv(1024).decode("utf-8")
        def fun():
            global win
            win = Toplevel(width=120,height=100,bg='white')
            win.wm_title("Casting")
            l = Label(win, text="Server request for casting.\nPlease press cast button..!!",font=("Arial",20),bg='white')
            l.grid(row=0, column=0)
        
            b = Button(win, text="Okay", command=win.destroy,bg='white')
            b.grid(row=1, column=0)
            
        if msg == "cast":
            fun()
        else:
            pass
        c.close()
        
    threading.Thread(target=casting_popup).start()
    
def casting(event=None):
    global btn
    global url1
    global url2
    try:
        context = zmq.Context()
        footage_socket = context.socket(zmq.PUB)
        footage_socket.connect(url1)
        sket = context.socket(zmq.REP)
        sket.connect(url2)
        def bnd():
            while True:
                try:
                    frame = numpy.array(sct.grab(monitor))
                    encoded, buffer = cv2.imencode('.jpg', frame)
                    jpg_as_text = base64.b64encode(buffer)
                    footage_socket.send(jpg_as_text)
                    msg = sket.recv(copy=True)
                    msg = msg.decode('utf-8')
                    sket.send(b"hello")
                    if msg == "stop":
                        sket.close()   
                        footage_socket.close()
                        cv2.destroyAllWindows()
                        break            
                except KeyboardInterrupt:
                    sket.close()
                    footage_socket.close()
                    cv2.destroyAllWindows()
                    break
        t1 = threading.Thread(target=bnd)
        t1.start()
               
    except Exception as e:
        pass
    

def bandwidth_consumption():
    global log_screen
    global bnd_width
    global old_value
    global bnd_width
    global value
    global chk_btn
          
    bnd_width=0.000
    lb = Label(log_screen,font=("Arial",30,'italic'),bg='white')
    lb.place(x=100,y=375)
    
    def bnd():
        old_value = 0
        while i==2:
            new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
            if old_value:
                v = new_value - old_value
                k = f"{((v/1024)/1024)*8:.3f} Mbps"
                lb.configure(text = k)
                lb.after(1000, bnd)
                lb.mainloop()
            old_value = new_value
            time.sleep(0.5) 
    bnd()
# =============================================================================

# Designing Main(first) window 
def main_account_screen():
    global main_screen
    global main_label
    global lbl1
    global log_screen
    
    main_screen = Tk()
    main_screen.geometry("1200x625")
    main_screen.title("Account Login") 
    
    # Menu bar
    menu = Menu(main_screen)
    main_screen.config(menu=menu)
    main_screen.config(bg='white')
    subm1 = Menu(menu)
    menu.add_cascade(label="Tools",menu=subm1,activebackground='light blue',activeforeground='white')
    subm1.add_command(label="Networking tools",command=None)
    subm2 = Menu(menu)
    menu.add_cascade(label="About",menu=subm2,activebackground='light blue',activeforeground='white')
    subm2.add_command(label="Details",command=None)
    subm2.add_separator()
    subm2.add_command(label="Contributors",command=None)
    subm3 = Menu(menu)
    menu.add_cascade(label="Help",menu=subm3,activebackground='light blue',activeforeground='white')
    subm3.add_command(label="Contact Us",command=None)
    
    lbl1 = Label(text="",bg='white')
    lbl1.place(x=0,y=0)
    log_screen = Frame(main_screen,bg="white")
    log_screen.place(x=0,y=0)
        
    login()
    #t = threading.Thread(target=login)
    #t.start()
    
    main_screen.resizable(height = False, width = False)
    
    def on_closing():
        global log_screen
        global user
        
        log_screen.destroy()
        if len(user) == 0:
            user='123456'
        user_login={'username':user}
        rqst = requests.post(url+"/user_deactivate", data=user_login)
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            global i
            i=100
            main_screen.destroy()
            sys.exit()
        else:
            pass
        
            
    main_screen.protocol("WM_DELETE_WINDOW", on_closing)
    
    main_screen.mainloop()
    
main_account_screen()
