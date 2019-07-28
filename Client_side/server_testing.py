from tkinter import *
from tkinter import ttk
import tkinter
import sqlite3
from PIL import Image, ImageTk
import subprocess
import threading
#casting lib
import cv2
import zmq
import base64
import numpy as np
import time
import requests
import socket


import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = (s.getsockname()[0])
s.close()
url= "http://"+ip+":5111"

global ips

def login():
    global login_screen
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    global ip_ke_liye
    global for_ip
    
    login_screen = Frame(bg="white",width="1370",height="675")
    login_screen.place(x=0,y=0)
    
    
    
    
    
    
    #Add Cdac logo
    '''iconPath = 'Images/index.png'
    logo = ImageTk.PhotoImage(Image.open(iconPath))
    label = Label(login_screen, image = logo, width='180',height='95',bg='white')
    label.image = logo
    label.configure(image = logo)
    label.place(x=220,y=130)'''
    #Admin login Logo
    Path='Images/admin_login.png'
    bg_img = ImageTk.PhotoImage(Image.open(Path))
    label = Label(login_screen, image = bg_img, bg='white', width='680',height='575')
    label.image = bg_img
    label.configure(image = bg_img)
    label.place(x=460,y=0)
    username_verify = StringVar()
    password_verify = StringVar()
    for_ip = StringVar()
    
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
    
    username_login_entry = Entry(login_screen, textvariable=username_verify,width="30", bd=3,font=("Times",15))
    username_login_entry.insert(0, 'Username')
    username_login_entry.bind('<FocusIn>', on_click)
    username_login_entry.bind('<FocusOut>', on_out)
    username_login_entry.place(x=160,y=290)
    
    
    
    
    
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
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*', bd=3, width="30",font=("Times",15))
    password_login_entry.insert(0, 'Password')
    password_login_entry.bind('<FocusIn>', on_pswd_click)
    password_login_entry.bind('<FocusOut>', on_pswd_out)
    password_login_entry.place(x=160,y=350)
    
    Button(login_screen, text="Login",font=("Times",13,'bold'),width='10', height='1', borderwidth=2, relief= RAISED, command = login_verify, activebackground = 'light green', activeforeground = 'white',cursor='hand2').place(x=240,y=430)
    
    
def login_verify(event=None):
    global lbl1
    global ip
    username1 = username_verify.get()
    password1 = password_verify.get()
    
    
    if username1 == "" or password1 == "" or ip == "":
        lbl1.destroy()
        lbl1 = Label(login_screen, text="Please complete the required field!", bg='white', fg="red", font=("Arial",15,'bold'),height=2)
        lbl1.place(x=145,y=245)
    else:
        
        if username1 =='admin' and password1 == 'admin':
            lbl1.destroy()
            login_window()
        else:
            lbl1.destroy()
            lbl1 = Label(login_screen, text="Invalid Username or Password ", fg="red", bg='white', font=("Arial",15,'bold'),height=2)
            lbl1.place(x=155,y=255)
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
        
   
        
def login_window():
    global main_screen
    global login_screen
    global username_verify
    global password_verify
    global log_screen
    
    user = username_verify.get()
    pswd = password_verify.get()
    log_screen = Frame(bg="white",width="1200",height="625")
    log_screen.place(x=0,y=0)
    left_side = Canvas(log_screen, bg="gray30",width="350",height="625")
    left_side.place(x=0,y=0)
    
    #Admin logo
    iconPath = 'Images/admin.png'
    logo = ImageTk.PhotoImage(Image.open(iconPath))
    label = Label(log_screen, image = logo, width='80',height='80', bg = 'white')
    label.image = logo
    label.configure(image = logo)
    label.place(x=360,y=0)
    Label(log_screen, text="Admin", bg='white', font=("Arial", 17)).place(x= 450,y= 15)
    Label(log_screen, text="Control All Conected Nodes", bg='white', font=("Arial", 10)).place(x= 450,y= 45)
    #Admin login Logo
    Path='Images/admin_screen.png'
    bg_img = ImageTk.PhotoImage(Image.open(Path))
    label = Label(log_screen, image = bg_img, bg='white')
    label.image = bg_img
    label.configure(image = bg_img)
    label.place(x=420,y=80)
    
    #net consumption logo
    iconPath = 'Images/data.png'
    logo = ImageTk.PhotoImage(Image.open(iconPath))
    label = Label(log_screen, image = logo, width='80',height='80', bg = 'white')
    label.image = logo
    label.configure(image = logo)
    label.place(x=900,y=0)
    
    Txt = Label(log_screen,text="Total Net\nConsumption",bg='white',fg='black', font=("Times",13,'bold italic'), cursor='hand2')
    Txt.place(x=980,y=17)
    Txt.bind("<Button-1>", net_usage)
    
    Txt = Label(log_screen,text="Screen Casting",bg='gray30',fg='gray60', font=("Arial",20), cursor='hand2',activeforeground = 'gray15')
    Txt.place(x=75,y=90)
    Txt.bind("<Button-1>", casting)
    left_side.create_line(20, 135, 330, 135, fill='gray60')
    
    Txt = Label(log_screen,text="Connected Nodes",bg='gray30',fg='gray60', font=("Arial",20), cursor='hand2',activeforeground = 'gray15')
    Txt.place(x=55,y=150)
    Txt.bind("<Button-1>", connected_node)
    left_side.create_line(20, 195, 330, 195, fill='gray60')
    
    Txt = Label(log_screen,text="Block User",bg='gray30',fg='gray60', font=("Arial",20), cursor='hand2',activeforeground = 'gray15')
    Txt.place(x=100,y=210)
    Txt.bind("<Button-1>", Block_user)
    left_side.create_line(20, 255, 330, 255, fill='gray60')
    
    Txt = Label(log_screen,text="Unblock User",bg='gray30',fg='gray60', font=("Arial",20), cursor='hand2',activeforeground = 'gray15')
    Txt.place(x=90,y=270)
    Txt.bind("<Button-1>", Unblock_user)
    left_side.create_line(20, 315, 330, 315, fill='gray60')
    
    Txt = Label(log_screen,text="IP Table Status",bg='gray30',fg='gray60', font=("Arial",20), cursor='hand2',activeforeground = 'gray15')
    Txt.place(x=75,y=330)
    Txt.bind("<Button-1>", Ip_status)
    left_side.create_line(20, 375, 330, 375, fill='gray60')
    
    Txt = Label(log_screen,text="Blocked Nodes",bg='gray30',fg='gray60', font=("Arial",20), cursor='hand2',activeforeground = 'gray15')
    Txt.place(x=70,y=390)
    Txt.bind("<Button-1>", blocked_nodes)
    left_side.create_line(20, 435, 330, 435, fill='gray60')
    '''
    Txt = Label(log_screen,text="Block Using\nTuxcut",bg='gray30',fg='gray60', font=("Arial",10), cursor='hand2',activeforeground = 'gray15')
    Txt.place(x=60,y=450)
    Txt.bind("<Button-1>", Tuxcut_sw)
    left_side.create_line(160, 445, 160, 485, fill='gray60')
    '''
    #changessssssssssssssssssssssssssssssssssss
    #evillimiter x=185
    Txt = Label(log_screen,text="Block Using Command",bg='gray30',fg='gray60', font=("Arial",20), cursor='hand2',activeforeground = 'gray15')
    Txt.place(x=30,y=450)
    Txt.bind("<Button-1>", Evillimiter_terminal)
    left_side.create_line(20, 495, 330, 495, fill='gray60')
    
    Txt = Label(log_screen,text="User Details",bg='gray30',fg='gray60', font=("Arial",20), cursor='hand2',activeforeground = 'gray15')
    Txt.place(x=80,y=510)
    Txt.bind("<Button-1>", admin_update)
    left_side.create_line(20, 555, 330, 555, fill='gray60')
    
    Txt = Label(log_screen,text="Registered Users",bg='gray30',fg='gray60', font=("Arial",20), cursor='hand2',activeforeground = 'gray15')
    Txt.place(x=60,y=570)
    Txt.bind("<Button-1>", Regitered_users)
    left_side.create_line(20, 615, 330, 615, fill='gray60')
    
    Button(log_screen, text="Logout",font=("Times",13,'bold'), bg='white', height='1', relief= RAISED, command = logout, activebackground = 'snow2', activeforeground = 'gray30', cursor='hand2').place(x=1100,y=20)
    
    
def net_usage(event=None):
    win = Toplevel()
    win.wm_title("Net Consumed")
    win.configure(width=100,height=70)
    
    run_command = "timeout 1 nload wlan0"
    ret_val = subprocess.Popen( run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
    output, errors = ret_val.communicate()
    output = str(output).split("\\")
    for i in output[17:30]:
        incm = output[17:25]
        outgo = output[26:32]
    incomming = incm[5][10:]
    outgoing = outgo[3][10:]
    data = f"Incomming Data: {incomming[5:]}\nOutgoing Data: {outgoing[5:]}\n"
    l = Label(win, text=data, width=25, height=5)
    l.grid(row=0, column=0)

    b = Button(win, text="OK", command=win.destroy)
    b.grid(row=1, column=0)

def casting(event=None):
    global castingip
    global cast1
    global cast2
    global lbl1
    
    cast1 = Frame(bg="white",width="1020",height="603")
    cast1.place(x=350,y=72)
    cast2 = Frame(cast1, bg="white", width = "1020", height="603")    
    cast2.place(x=0, y=0)
    
    response = requests.get(url+"/get_login_ip")
    reg_users = response.text
    st = reg_users.split("]")
    j = []
    for i in st[0:len(st)]:
        j.append(i.split("\n")[2:5])
    ips1 = []
    for k in j[0:len(st)-2]:
        ips1.append(k[0].replace("    ","").replace('"',""))
    
    castingip = StringVar(cast2)
    castingip.set("Choose IP")
    popupMenu = OptionMenu(cast2, castingip, *ips1)
    popupMenu.place(x=650,y=220)
    Label(cast2, text ="IP Addresses", bg='white', font=("ms serif", 10, 'bold')).place(x=650,y=200)
    lb1 = Label(cast2, text ="Casting IP Address", bg='white', height='2', font=("ms serif", 25, 'bold'))
    lb1.place(x=300,y=70)
    blabel = Label(cast2, text="Enter IP address you want to screencast:",bg='white',font=("Times",15,'bold'), height='2')
    blabel.place(x=260, y=160)
    entry = Entry(cast2, textvariable=castingip,width="30", bd=3,font=("Times",15))
    entry.place(x=280,y=220)
    btn = Button(cast2, text="Submit",font=("Times",13,'bold'),width='10', height='1', borderwidth=2, relief= RAISED, command = View_casting, activebackground = 'red', activeforeground = 'white',cursor='hand2')
    btn.place(x=285,y=330)
    btn = Button(cast2, text="Cast",font=("Times",13,'bold'),width='10', height='1', borderwidth=2, relief= RAISED, command = screen_cast, activebackground = 'red', activeforeground = 'white',cursor='hand2')
    btn.place(x=450,y=330)
    entry.delete(0, END)
    
def View_casting():
    global casatingip
    global cast2
    global lbl1
    global port
    global ip
    
    ip = castingip.get()
    try:
        conn = sqlite3.connect('networkusers.db')
        cursor = conn.cursor()
        cursor = cursor.execute("SELECT port1, port2, port3 FROM port WHERE ip = ?;",(ip,))
        port = cursor.fetchone()
        if port is not None:
            lbl1.destroy()
            lbl1 = Label(cast2, text=f"Port Assigned for {ip} are {port[0]} and {port[1]}.", bg='white', fg="green", font=("ms serif", 15, "bold"))
            lbl1.place(x=200,y=280)
        else:
            lbl1.destroy()
            lbl1 = Label(cast2, text="Please Enter Registered IP.", bg='white', fg="red", font=("ms serif", 15, "bold"))
            lbl1.place(x=290,y=280)
    except:
        lbl1.destroy()
        lbl1 = Label(cast2, text="Server is off.. Try again later!!", fg="red", bg='white', font=("ms serif", 15, "bold"),height=2)
        lbl1.place(x=200,y=280)
    
def screen_cast():
    global ip
    global port
    
    s=socket.socket()
    s.connect((ip,port[2]))
    s.sendall("cast".encode("utf-8"))
    s.close()
    
    def cast():
        global port
        global ip
        global cast1
        global login_screen
        
        url1 = f"tcp://*:{port[0]}"
        url2= f"tcp://*:{port[1]}"
        try:
            context = zmq.Context()
            footage_socket = context.socket(zmq.SUB)
            footage_socket.bind(url1)
            sket = context.socket(zmq.REQ)
            sket.bind(url2)
            footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
            while True:
                try:
                    frame = footage_socket.recv_string()
                    img = base64.b64decode(frame)
                    npimg = np.fromstring(img, dtype=np.uint8)#encoding
                    source = cv2.imdecode(npimg, 1)#decode
                    source = cv2.resize(source,None,fx=0.50,fy=0.50)
                    cv2.imshow("Stream", source)
                    sket.send(b"start")
                    dm = sket.recv()
                    if cv2.waitKey(25) & 0xFF == ord("q"):
                        cv2.destroyAllWindows()
                        sket.send(b"stop",copy=True)
                        sket.close()
                        footage_socket.close()
                        cast1.destroy()
                        login_window()
                        break        
                except KeyboardInterrupt:
                    cv2.destroyAllWindows()
                    sket.send(b"stop",copy=True)
                    sket.close()
                    
                    footage_socket.close()
                    break
        except Exception as e:
            print(e)
    
    threading.Thread(target=cast).start()


#Connected nodes 
def connected_node(event=None):
    data_screen = Frame(bg='white', width=850, height = 540)
    data_screen.place(x=350, y=72)
    frame=Frame(data_screen,width=835,height=540)
    frame.grid(row=0,column=0)
    canvas = Canvas(frame,bg='white',width=835, height=540) # a canvas in the parent object
    f1 = Frame(canvas,bg='white') # a frame in the canvas
    
    # a scrollbar in the parent
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    hscrollbar = Scrollbar(frame, orient="horizontal", command=canvas.xview)
    # connect the canvas to the scrollbar
    canvas.configure(xscrollcommand=hscrollbar.set,yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y") # comment out this line to hide the scrollbar
    hscrollbar.pack(side="bottom",fill="x")
    canvas.pack(side="left", fill="both", expand=True) # pack the canvas
    # make the frame a window in the canvas
    canvas.create_window((4,4), window=f1, anchor="nw", tags="frame")
    # bind the frame to the scrollbar
    f1.bind("<Configure>", lambda x: canvas.configure(scrollregion=canvas.bbox("all")))
    frame.bind("<Down>", lambda x: canvas.yview_scroll(3, 'units')) # bind "Down" to scroll down
    frame.bind("<Up>", lambda x: canvas.yview_scroll(-3, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    frame.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(-1*(x.delta/40)), "units"))
    frame.bind("<Down>", lambda x: canvas.xview_scroll(3, 'units')) # bind "Down" to scroll down
    frame.bind("<Up>", lambda x: canvas.xview_scroll(-3, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    frame.bind("<MouseWheel>", lambda x: canvas.xview_scroll(int(-1*(x.delta/40)), "units"))
    canvas.update_idletasks()
    label1 = Label(f1, bg="white", width = "28", height="175")
    label1.grid(row=2,column=1)
    Label(label1, text = 'IP',bg='white', font=("ms serif",15,'bold')).place(x=70,y=10)
    label2 = Label(f1,bg="white", width = "35", height="175")
    label2.grid(row=2,column=3)    
    Label(label2, text = 'MAC',bg='white', font=("ms serif",15,'bold')).place(x=70,y=10)
    label3 = Label(f1,bg="white", width = "80", height="175")
    label3.grid(row=2,column=5)
    Label(label3, text = 'HOST NAME', bg = 'white',font=("ms serif",15,'bold')).place(x=120,y=10)
    
    cmd = subprocess.check_output("arp-scan -l", shell = True)
    cmd = str(cmd).split('\\n')
    cmd = cmd[2:len(cmd)-4]
    ips = []
    mac = []
    host_name = []
    for i in cmd:
        i=i.split('\\t')
        ips.append(i[0])
        mac.append(i[1])
        host_name.append(i[2])
    x=0
    for i in range(len(ips)):
        Label(label1, text=ips[i],bg='white',font=("Times",15,'bold')).place(x=30, y=60+x)
        Label(label2, text=mac[i],bg='white',font=("Times",15,'bold')).place(x=30, y=60+x)
        Label(label3, text=host_name[i],bg='white',font=("Times",15,'bold')).place(x=30, y=60+x)
        x +=30
    connected_nodes = f"Total Connected Nodes:: {len(ips)-1}\nHost IP:: {ips[0]}"
    Label(label3, text=connected_nodes,bg='white',fg='RED', font=("Times",20,'bold')).place(x=30, y=80+x)

def logout():
    global log_screen
    global block
    global unblock
    login()
    log_screen.destroy()
    
# block user
def Block_user(event=None):
    global blockip
    global block
    global entry
    global block2
    
    blockip = StringVar()
    block = Frame(bg="white",width="850",height="600")
    block.place(x=350,y=72)
    block2 = Frame(block, bg="white", width = "835", height="590")    
    block2.place(x=0, y=0)
    lb1 = Label(block2, text ="Block IP Address", bg='white', height='2', font=("ms serif", 25, 'bold'))
    lb1.place(x=300,y=70)
    blabel = Label(block2, text="Enter ip address you want to block:",bg='white',font=("Times",15,'bold'), height='2')
    blabel.place(x=260, y=160)
    entry = Entry(block2, textvariable=blockip,width="30", bd=3,font=("Times",15))
    entry.place(x=280,y=220)
    btn = Button(block2, text="Submit",font=("Times",13,'bold'),width='10', height='1', borderwidth=2, relief= RAISED, command = Block_ip, activebackground = 'red', activeforeground = 'white',cursor='hand2')
    btn.place(x=350,y=320)

def Block_ip():
    global blockip
    global block2
    global entry
    global ip_addr
    
    ip_addr = blockip.get()
    opts = {'ip':ip_addr}
    block_ip_table_list()
    #block specific ip 
    ipcmd = "iptables -I INPUT -s {ip} -j DROP".format(**opts) # DROP ---> REJECT
    c= subprocess.Popen(ipcmd, shell=True,stdin = subprocess.PIPE, stderr=subprocess.PIPE)
    
    entry.delete(0, END)
    
def block_ip_table_list():
    global ip_addr
    global block2
    
    try:
        conn = sqlite3.connect("networkusers.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS block_ip (ip TEXT);")
        query=cursor.execute("SELECT ip FROM block_ip WHERE ip= ?;",(ip_addr,))
        l = len(list(query))
        
        if l == 0:
            cursor.execute("INSERT INTO block_ip (ip) VALUES (?);", (ip_addr,))
            conn.commit()
            action = Label(block2, text="IP Blocked Successfully",bg='white', fg='green',font=("Times",15,'bold'))
            action.place(x=300,y=280)
        else:
            action = Label(block2, text="IP Already Blocked!!",bg='white', fg='red',font=("Times",15,'bold'))
            action.place(x=310,y=280)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    
# Unblock user
def Unblock_user(event=None):
    global unblockip
    global unblock
    global unblock2
    global entry2
    global tree
    
    unblockip = StringVar()
    unblock = Frame(bg="white",width="850",height="600")
    unblock.place(x=350,y=72)
    unblock2 = Frame(unblock, bg="white", width = "850", height="600")    
    unblock2.place(x=0, y=0)
    lb1 = Label(unblock2, text ="Unblock IP Address", bg='white', height='2', font=("ms serif", 25, 'bold'))
    lb1.place(x=300,y=70)
    unblabel = Label(unblock2, text="Enter ip address you want to unblock:",bg='white',font=("Times",15,'bold'))
    unblabel.place(x=260, y=160)
    entry2 = Entry(unblock2, textvariable=unblockip,width="30", bd=3,font=("Times",15))
    entry2.place(x=280,y=220)
    btn = Button(unblock2, text="Submit",font=("Times",13,'bold'),width='10', height='1', borderwidth=2, relief= RAISED, command = Unblock_ip, activebackground = 'red', activeforeground = 'white',cursor='hand2')
    btn.place(x=350,y=320)
    
    tree= ttk.Treeview(unblock2, column=("column1"), show='headings')
    tree.heading("#1", text="IP ADRESS")
    tree.place(x=40,y=280)
    
    global b2
    b2 = Button(unblock2,text="Blocked IP", command=View, bg="white")
    b2.place(x=95,y=250)
    
def Unblock_ip():
    global unblockip
    global entry2
    global unblock
    global unblock2
    global ip_addr2
    global b2
    
    b2.configure(state="normal")
    ip_addr2 = unblockip.get()
    opts = {'ip':ip_addr2}
    unblock_user_db()
    # Unblock specific ip 
    ipcmd = "iptables -D INPUT -s {ip} -j DROP".format(**opts)# DROP ---> REJECT
    c = subprocess.check_output(ipcmd, shell=True)
    entry2.delete(0, END)

def unblock_user_db():
    global ip_addr2
    global unblock2
    
    try:
        conn = sqlite3.connect("networkusers.db")
        cursor = conn.cursor()
        query=cursor.execute("SELECT ip FROM block_ip WHERE ip= ?;",(ip_addr2,))
        l = len(list(query))
        
        if l > 0:
            cursor.execute("DELETE FROM block_ip WHERE ip=?;", (ip_addr2,))
            conn.commit()
            string = f"IP: {ip_addr2} Unblocked!!"
            Label(unblock2, text=string,bg='white', width=30, fg='green',font=("Arial",15)).place(x=300,y=280)
        else:
            Label(unblock2, text="IP Already Unblocked!!", width=30,bg='white', fg='green',font=("Arial",15)).place(x=310,y=280)

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    
def View():
    global tree
    global b2
    conn = sqlite3.connect("networkusers.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM block_ip;")
    rows = cur.fetchall()
    for row in rows:
        tree.insert("",END, values=row)
    b2.configure(state="disable")
    conn.close()


def Ip_status(event=None):
    data_screen = Frame(bg='white', width=850, height = 540)
    data_screen.place(x=350, y=72)
    frame=Frame(data_screen,width=835,height=535)
    frame.grid(row=0,column=0)
    canvas = Canvas(frame,bg='white',width=835, height=535) # a canvas in the parent object
    f1 = Frame(canvas,bg='white') # a frame in the canvas
    # a scrollbar in the parent
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    hscrollbar = Scrollbar(frame, orient="horizontal", command=canvas.xview)
    # connect the canvas to the scrollbar
    canvas.configure(xscrollcommand=hscrollbar.set,yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y") # comment out this line to hide the scrollbar
    hscrollbar.pack(side="bottom",fill="x")
    canvas.pack(side="left", fill="both", expand=True) # pack the canvas
    # make the frame a window in the canvas
    canvas.create_window((4,4), window=f1, anchor="nw", tags="frame")
    # bind the frame to the scrollbar
    f1.bind("<Configure>", lambda x: canvas.configure(scrollregion=canvas.bbox("all")))
    frame.bind("<Down>", lambda x: canvas.yview_scroll(3, 'units')) # bind "Down" to scroll down
    frame.bind("<Up>", lambda x: canvas.yview_scroll(-3, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    frame.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(-1*(x.delta/40)), "units"))
    frame.bind("<Down>", lambda x: canvas.xview_scroll(3, 'units')) # bind "Down" to scroll down
    frame.bind("<Up>", lambda x: canvas.xview_scroll(-3, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    frame.bind("<MouseWheel>", lambda x: canvas.xview_scroll(int(-1*(x.delta/40)), "units"))
    #Label(f1,text='                                                        ',bg='white').grid(row=0,column=1)
    Label(f1,text = 'IP Table Status', bg='White', font=("ms serif", 25, 'bold')).grid(row=0,column=1)
    cmnd = "iptables -nvL"
    status_data = subprocess.check_output(cmnd, shell=True)
    status_data = str(status_data)
    status_data = status_data[2:len(status_data)-1]
    status_data = status_data.split('\\n')
    
    for i in range(len(status_data)):
        Label(f1, text=status_data[i],bg='white',font=("Times",15)).grid(row = i+1, column = 1)
    
    btn = Button(f1, text="Clear IP Table",font=("Times",13,'bold'),width='10', height='1', borderwidth=2, relief= RAISED, command = Clear_ip, activebackground = 'red', activeforeground = 'white',cursor='hand2')
    btn.grid(row=1, column=2)
    
    
def blocked_nodes(event=None):
    data_screen = Frame(bg='white', width=850, height = 540)
    data_screen.place(x=350, y=72)
    frame=Frame(data_screen,width=835,height=535)
    frame.grid(row=0,column=0)
    canvas = Canvas(frame,bg='white',width=835, height=535) # a canvas in the parent object
    f1 = Frame(canvas,bg='white') # a frame in the canvas
    # a scrollbar in the parent
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    hscrollbar = Scrollbar(frame, orient="horizontal", command=canvas.xview)
    # connect the canvas to the scrollbar
    canvas.configure(xscrollcommand=hscrollbar.set,yscrollcommand=scrollbar.set)
    hscrollbar.pack(side="bottom",fill="x")
    scrollbar.pack(side="right", fill="y") # comment out this line to hide the scrollbar
    canvas.pack(side="left", fill="both", expand=True) # pack the canvas
    # make the frame a window in the canvas
    canvas.create_window((4,4), window=f1, anchor="nw", tags="frame")
    # bind the frame to the scrollbar
    f1.bind("<Configure>", lambda x: canvas.configure(scrollregion=canvas.bbox("all")))
    frame.bind("<Down>", lambda x: canvas.yview_scroll(3, 'units')) # bind "Down" to scroll down
    frame.bind("<Up>", lambda x: canvas.yview_scroll(-3, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    frame.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(-1*(x.delta/40)), "units"))
    frame.bind("<Down>", lambda x: canvas.xview_scroll(3, 'units')) # bind "Down" to scroll down
    frame.bind("<Up>", lambda x: canvas.xview_scroll(-3, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    frame.bind("<MouseWheel>", lambda x: canvas.xview_scroll(int(-1*(x.delta/40)), "units"))
    Label(f1,text='                                                        ',bg='white').grid(row=0,column=1)
    Label(f1,text = 'Blocked Nodes', bg='White', font=("ms serif", 25, 'bold')).grid(row=0,column=2)
    
    cmnd="iptables -nvL"
    status_data = subprocess.check_output(cmnd,shell=True)
    status_data = str(status_data)
    status_data = status_data[2:len(status_data)-1]
    status_data = status_data.split("\\n")
    
    lis=[]
    for i in status_data:
        if i[0:13] == 'Chain FORWARD':
            break
        lis.append(i)
    
    for i in range(len(lis)):
        lblb = Label(f1,bd='5', text=lis[i], bg="white", font=("Times", 15))
        lblb.grid(row=i+1, column=2)
    
    
def Clear_ip():
    subprocess.check_output("iptables -F", shell=True)
    Ip_status()

def Tuxcut_sw(event=None):
    def mThread():
        x = subprocess.check_output("tuxcut/./tuxcut", shell=True)
    threading.Thread(target=mThread).start()

def Evillimiter_terminal(event=None):
    data_screen = Frame(bg='white', width=850, height = 540)
    data_screen.place(x=350, y=72)
    frame=Frame(data_screen,width=835,height=535)
    frame.grid(row=0,column=0)
    canvas = Canvas(frame,bg='white',width=835, height=535) # a canvas in the parent object
    f1 = Frame(canvas,bg='white') # a frame in the canvas
    # a scrollbar in the parent
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    hscrollbar = Scrollbar(frame, orient="horizontal", command=canvas.xview)
    # connect the canvas to the scrollbar
    canvas.configure(xscrollcommand=hscrollbar.set,yscrollcommand=scrollbar.set)
    hscrollbar.pack(side="bottom",fill="x")
    scrollbar.pack(side="right", fill="y") # comment out this line to hide the scrollbar
    #canvas.place(x=0,y=0)
    canvas.pack(side="left", fill="both", expand=True) # pack the canvas
    # make the frame a window in the canvas
    canvas.create_window((4,4), window=f1, anchor="nw", tags="frame")
    # bind the frame to the scrollbar
    f1.bind("<Configure>", lambda x: canvas.configure(scrollregion=canvas.bbox("all")))
    frame.bind("<Down>", lambda x: canvas.yview_scroll(3, 'units')) # bind "Down" to scroll down
    frame.bind("<Up>", lambda x: canvas.yview_scroll(-3, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    frame.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(-1*(x.delta/40)), "units"))
    frame.bind("<Down>", lambda x: canvas.xview_scroll(3, 'units')) # bind "Down" to scroll down
    frame.bind("<Up>", lambda x: canvas.xview_scroll(-3, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    frame.bind("<MouseWheel>", lambda x: canvas.xview_scroll(int(-1*(x.delta/40)), "units"))
    Label(f1,text = 'Evillimiter Guidlines', bg='White', font=("ms serif", 25, 'bold')).pack()
    
    #Admin Doc 1
    Path='Images/evillimiter_doc1.png'
    bg_img = ImageTk.PhotoImage(Image.open(Path))
    label = Label(f1, image = bg_img, bg='white')
    label.image = bg_img
    label.configure(image = bg_img)
    label.pack()
    #Admin Doc 2
    Path='Images/evillimiter_doc2.png'
    bg_img = ImageTk.PhotoImage(Image.open(Path))
    label = Label(f1, image = bg_img, bg='white')
    label.image = bg_img
    label.configure(image = bg_img)
    label.pack()
    
    x=subprocess.check_output("gnome-terminal", shell=True)
    
#password change
def admin_update(event=None):
    global username_test
    global labelu
    global username_test
    global btn
    global lbl1
    global new_password
    global password_enter
    global username_enter
    global lb
    global username
    global password
    global password_entry
    global username_entry
    
    data_screen = Frame(bg='white', width=850, height = 600)
    data_screen.place(x=350, y=72)
    f1 = Frame(data_screen,bg='white',width=850, height=600)
    f1.place(x=0,y=0)
    lb = Label(f1,font=("Times",15,'bold italic'),width=10)
    lb.place(x=0,y=0)
    lbl1=Label(lb)
    lbl1.place(x=0,y=0)
    
    lb.configure(width="600", height="500", bg='white')
    username_forget = StringVar()
    password_forget1 = StringVar()
    password_forget2 = StringVar()
    Label(lb, text="Password Update", font=("ms serif",20,"bold"),bg='white').place(x=140,y=110) 
    Label(lb, text="Username * ",font=("Times",15,'bold'),bg='white').place(x=90,y=190)
    username_test = Entry(lb,textvariable=username_forget,width="20", bd=3,font=("Times",15))
    username_test.place(x=200,y=190)
    Label(lb, text="Password * ", font=("Times",15,'bold'),bg='white').place(x=90,y=240)
    password_enter = Entry(lb, textvariable=password_forget1, show= '*', bd=3, width="20",font=("Times",15))
    password_enter.place(x=200,y=240)
    Label(lb, text="Confirm Password * ", font=("Times",15,'bold'),bg='white').place(x=15,y=300)
    new_password = Entry(lb, textvariable=password_forget2, show= '*', bd=3, width="20",font=("Times",15))
    new_password.place(x=200,y=290)
            
    btn = Button(lb, text="Submit",font=("Times",13,'bold'),width='10', height='1', borderwidth=2, relief= RAISED, command = submit_action, activebackground = 'light blue', activeforeground = 'white',cursor='hand2')
    btn.place(x=170,y=390)
    
    #Add new user
    username = StringVar()
    password = StringVar()
 
    Label(lb, text="Add User", bg="white", font=("ms serif",20,"bold")).place(x=550,y=110)
    Label(lb, text="Username * ",font=("Times",15,'bold'),bg='white').place(x=440,y=190)
    username_entry = Entry(lb, textvariable=username,width="20", bd=3,font=("Times",15))
    username_entry.place(x=550,y=190)
    Label(lb, text="Password * ", font=("Times",15,'bold'),bg='white').place(x=440,y=250)
    password_entry = Entry(lb, textvariable=password, show= '*', bd=3, width="20",font=("Times",15))
    password_entry.place(x=550,y=250)
    
    Button(lb, text="Register", command = register_user, font=("Times",13,'bold'),width='10', height='1', borderwidth=2, relief= RAISED, activebackground = 'light green', activeforeground = 'white',cursor='hand2').place(x=550,y=350)

def register_user(event=None):
    global username
    global password
    global username_entry
    global password_entry
    global lbl1
    #Add new user
    username_info = username.get()
    password_info = password.get()
    if username_info == "" or password_info == "":
        lbl1.destroy
        lbl1 = Label(lb, text="Please complete the required field!", bg='white', fg="red", font=("Arial", 15))
        lbl1.place(x=440,y=300)
    elif len(password_info) < 6:
        lbl1.destroy
        lbl1 = Label(lb, text="Size of password is more than 6 !!", bg='white', fg="red", font=("Arial", 15))
        lbl1.place(x=440,y=300)
    else:
        try:
            #post request
            payload = {'username': username_info, 'password': password_info}
            rqst = requests.post(url+"/post", data=payload)
            if rqst.status_code == 200:
                lbl1.destroy()
                lbl1 = Label(lb, text="User added successfuly!!", bg='white', fg="green", font=("Arial", 15))
                lbl1.place(x=490,y=300)
            elif rqst.status_code == 500:
                lbl1.destroy()
                lbl1 = Label(lb, text="User Already Exist!!", bg='white', fg="red", font=("Arial", 15))
                lbl1.place(x=490,y=300)
            else:
                lbl1.destroy()
                lbl1 = Label(lb, text="User not added", bg='white', fg="red", font=("Arial", 15))
                lbl1.place(x=490,y=300)
        except:
            lbl1.destroy()
            lbl1 = Label(lb, text="Server is off.. Try again later!!", fg="red", bg='white', font=("Arial", 15))
            lbl1.place(x=450,y=300)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    

# submit uername and further procede
def submit_action(event=None):    
    global lb
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
        lbl1 = Label(lb, text="Please complete the required field!!", bg='white', fg="red", font=("Arial", 15))
        lbl1.place(x=100,y=340)
        
    else:
        try:
            if passtest1 == passtest2:            
                payload = {'username': usertest, 'password': passtest2}
                rqst = requests.put(url+"/forget", data = payload)
                if rqst.status_code == 200:
                    lbl1.destroy()
                    lbl1 = Label(lb, text="Password changed!!", bg='white', fg="green", font=("Arial", 15))
                    lbl1.place(x=200,y=340)
                else:
                    lbl1.destroy()
                    lbl1 = Label(lb, text="Please enter your valid username!", bg='white', fg="red", font=("Arial", 15))
                    lbl1.place(x=150,y=340)
            else:
                lbl1.destroy()
                lbl1 = Label(lb, text="Password not matched!", bg='white', fg="red", font=("Arial", 15))
                lbl1.place(x=200,y=340)
        except:
            lbl1.destroy()
            lbl1 = Label(lb, text="Server is off.. Try again later!!", fg="red", bg='white', font=("Arial", 15))
            lbl1.place(x=150,y=340)
    username_test.delete(0, END)
    new_password.delete(0, END)
    password_enter.delete(0, END)
    

def Regitered_users(event=None):
    data_screen = Frame(bg='white', width=850, height = 540)
    data_screen.place(x=350, y=72)
    frame=Frame(data_screen,width=835,height=535)
    frame.grid(row=0,column=0)
    canvas = Canvas(frame,bg='white',width=835, height=535) # a canvas in the parent object
    f1 = Frame(canvas,bg='white') # a frame in the canvas
    # a scrollbar in the parent
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    hscrollbar = Scrollbar(frame, orient="horizontal", command=canvas.xview)
    # connect the canvas to the scrollbar
    canvas.configure(xscrollcommand=hscrollbar.set,yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y") # comment out this line to hide the scrollbar
    hscrollbar.pack(side="bottom",fill="x")
    canvas.pack(side="left", fill="both", expand=True) # pack the canvas
    # make the frame a window in the canvas
    canvas.create_window((4,4), window=f1, anchor="nw", tags="frame")
    # bind the frame to the scrollbar
    f1.bind("<Configure>", lambda x: canvas.configure(scrollregion=canvas.bbox("all")))
    frame.bind("<Down>", lambda x: canvas.yview_scroll(3, 'units')) # bind "Down" to scroll down
    frame.bind("<Up>", lambda x: canvas.yview_scroll(-3, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    frame.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(-1*(x.delta/40)), "units"))
    frame.bind("<Down>", lambda x: canvas.xview_scroll(3, 'units')) # bind "Down" to scroll down
    frame.bind("<Up>", lambda x: canvas.xview_scroll(-3, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    frame.bind("<MouseWheel>", lambda x: canvas.xview_scroll(int(-1*(x.delta/40)), "units"))
    
    #Get Active Users
    try:
        conn = sqlite3.connect("networkusers.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM port WHERE is_active= 0;")
        rows=cursor.fetchall()
        l = len(list(rows))
        non_active=[]
        if l > 0:
            for i in rows:
                non_active.append("       "+i[0])
        else:
            pass
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    
    #Get Non Active Users
    try:
        conn = sqlite3.connect("networkusers.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username,ip FROM port WHERE is_active= 1;")
        rows=cursor.fetchall()
        l = len(list(rows))
        active_user=[]
        user_ip=[]
        res = []
        if l > 0:
            for i in rows:
                active_user.append(i[0])
                user_ip.append(i[1])
            for i in range(len(user_ip)):
                res.append(active_user[i]+" : "+user_ip[i])
        else:
            pass
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    
    label1 = Label(f1, bg="white", width = "70", height="150")
    label1.grid(row=2,column=1)
    Label(label1, text = 'Non Active Users',bg='white', font=("ms serif",20,'bold')).place(x=70,y=10)
    label2 = Label(f1,bg="white", width = "70", height="150")
    label2.grid(row=2,column=3)    
    Label(label2, text = 'Active Users',bg='white', font=("ms serif",20,'bold')).place(x=70,y=10)
    l
    x=0
    for i in range(len(non_active)):
        Label(label1, text=non_active[i],bg='white',font=("Arial",17)).place(x=30, y=60+x)
        x +=37
    x=0
    for i in range(len(res)):    
        Label(label2, text=res[i],bg='white',font=("Arial",17)).place(x=30, y=60+x)
        x +=37
    
# Designing Main(first) window 
def main_account_screen():
    global main_screen
    global lbl1
    
    main_screen = Tk()
    main_screen.geometry("1200x625")
    main_screen.configure(bg='white')
    main_screen.title("Account Login")
    
    # Menu bar
    menu = Menu(main_screen)
    main_screen.config(menu=menu)
    
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
    
    login()
    
    main_screen.resizable(height = False, width = False)
    main_screen.mainloop()
    
main_account_screen()
