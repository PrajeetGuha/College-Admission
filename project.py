import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
from win32api import GetSystemMetrics
from PIL import Image,ImageTk,ImageEnhance
from dependencies import validation,utility,admin_statistics
from dependencies import login_check as lc
from captcha.image import ImageCaptcha
import tkinter.messagebox as tmg
import re

class app(tk.Frame):
    
    def __init__(self,master = None):
        
        super().__init__()
        self.master = master
        self.width = GetSystemMetrics(0)
        self.height = GetSystemMetrics(1)
        self.master.resizable(0,0)
        self.master.state('zoomed')
        dimension = f'{self.width}x{self.height}'
        self.master.geometry(dimension)
        self.master.iconbitmap('assets/logo_icon.ico')
        self.master.title(int(0.15*self.width)*' ' + 'Student Portal')
        self.pack()
        
        self.font = f'Arial {int(0.013*self.height)} bold'
        
        self.main_Canvas = tk.Canvas(self,height = self.height, width = self.width, highlightthickness = 0,bg='white')
        self.main_Canvas.pack(padx = 0, pady = 0,fill = 'both', expand = True)
        self.home_window()
        
    def home_window(self):
        self.main_Canvas.delete('all')
        background_image = Image.open('assets/background_image.png').resize((self.width, self.height))
        logo = Image.open('assets/logo.png').resize((int(0.219*self.width), int(0.390*self.height)))
        new_background_image = Image.new('RGBA', (self.width,self.height))
        new_background_image.paste(background_image, (0,0))
        new_background_image.paste(logo, (int(self.width/2.55), int(self.height/11)), mask = logo)
        tk_background_Image = ImageTk.PhotoImage(new_background_image)
        
        self.main_Canvas.create_image(self.width/2, self.height/2, image = tk_background_Image)
        self.main_Canvas.image = tk_background_Image
        
        h_welcome = self.height/3
        w_welcome = self.width/1.5
        welcome_canvas = tk.Canvas(self.main_Canvas, height = h_welcome, width = w_welcome, bg = '#00004E',highlightthickness=0)
        self.main_Canvas.create_window(self.width/2, self.height/1.3, window = welcome_canvas)
        
        college_name=tk.Label(welcome_canvas,text="St. Thomas' College of Engineering & Technology",bg='#00004E',fg='white',font=f'Arial {int(0.093*h_welcome)} bold')
        welcome_canvas.create_window(w_welcome/2,h_welcome/6,window=college_name)
        details_string = '4,Diamond Harbour Road, Kidderpore, Kolkata - 700023\n\nAll Programmes (B.Tech in CSE, EE, ECE & IT) are NBA Accredited.'
        contacts_string = 'Contact Us: 8648891532 / 8648857332 / 8017993803   For Admission Queries - 8017993801(Mon - Sat 10:00 AM - 5:00 PM)\nEmail Us: stcet@stcet.ac.in   For Admission Queries -admission.stcet@gmail.com'
        details=tk.Label(welcome_canvas,text=details_string,bg='#00004E',fg='white',font=f'Arial {int(0.059*h_welcome)}')
        welcome_canvas.create_window(w_welcome/2,h_welcome/2,window=details)
        
        contacts = tk.Label(welcome_canvas,text=contacts_string,bg='#00004E',fg='white',font=f'Arial {int(0.039*h_welcome)}')
        welcome_canvas.create_window(w_welcome/2,h_welcome/1.2,window=contacts)
        
        admission_button = tk.Button(self.main_Canvas, text = ' ADMISSION FORM ', fg = 'white',bg ='blue',font=self.font,command= self.form,cursor = 'hand2')
        self.main_Canvas.create_window(self.width/2, self.height/1.85, window = admission_button)
        
    def form(self):
        
        background_image = Image.open('assets/background_image.png').resize((self.width, self.height))
        tk_background_Image = ImageTk.PhotoImage(background_image)
        
        self.main_Canvas.delete('all')
        self.main_Canvas.create_image(self.width/2, self.height/2, image = tk_background_Image)
        self.main_Canvas.image = tk_background_Image

        #login_window
        self.width_canv = self.width/4
        self.height_canv = self.height/2.5
        self.login_canvas= tk.Canvas(self.main_Canvas, height = self.height_canv, width = self.width_canv, bg = 'white',highlightthickness = 0, relief = 'raised')
        self.main_Canvas.create_window(self.width_canv*2, self.height_canv*1.3, window = self.login_canvas)
        
        #login_button
        self.login_button = tk.Button(text='Login',fg ='white',bg ='blue',font=self.font,command=self.login_user,cursor = 'hand2')
        self.login_canvas.create_window(self.width_canv/2,self.height_canv*0.85,window=self.login_button)
        
        self.status = tk.Label(self.login_canvas, font = self.font, bg = 'white')
        self.login_canvas.create_window(self.width_canv/2,self.height_canv*0.93,window=self.status)
        
        #Passowrd
        self.password = tk.StringVar()
        entry1 = tk.Entry(root, show = '*', font = self.font, textvariable = self.password) 
        self.login_canvas.create_window(self.width_canv/1.5,self.height_canv*0.5,window=entry1)
        
        self.label1 = tk.Label(root, text='Password',font=self.font,bg='white')
        self.login_canvas.create_window(self.width_canv/4,self.height_canv*0.5, window=self.label1)
        
        self.show = tk.IntVar(self.login_canvas)
        show_password = tk.Checkbutton(self.login_canvas, variable = self.show, text = 'Show password', font = self.font, bg = 'white', activebackground = 'white',cursor = 'hand2')
        self.login_canvas.create_window(self.width_canv/1.5,self.height_canv*0.58, window=show_password)
        
        admin_button = tk.Button(self.main_Canvas, text = 'Admin', font = self.font, command = self.admin, bg = '#FF8033', fg = 'white', activebackground = '#FF8033', activeforeground = 'white',cursor = 'hand2')
        self.main_Canvas.create_window(0.95*self.width, 0.05*self.height, window = admin_button)
        
        def show_hide():
            
            if self.show.get() == 1:
                entry1.config(show = '')
                
            elif self.show.get() == 0:
                entry1.config(show = '*')
                
        self.show.trace('w', lambda x,y,z: show_hide())
        
        self.captcha_addition()
        self.captcha_input = tk.StringVar()
        captcha_entry = tk.Entry(self.login_canvas, text = self.font, textvariable = self.captcha_input)
        self.login_canvas.create_window(self.width_canv/1.55,self.height_canv*0.683, window=captcha_entry)
        
        self.captcha_input.trace('w', lambda x,y,z: self.captcha_input.set(self.captcha_input.get().upper()))
        
        reload_captcha = tk.Button(self.login_canvas, text = '⟳', command = self.captcha_addition, bd = 0, bg = 'white', activebackground = 'blue', activeforeground = 'white',cursor = 'hand2')
        self.login_canvas.create_window(self.width_canv/1.17,self.height_canv*0.683, window=reload_captcha)
        #Username
        self.username = tk.StringVar()
        entry2 = tk.Entry (root, font = self.font, textvariable = self.username) 
        self.login_canvas.create_window(self.width_canv/1.5,self.height_canv*0.4,window=entry2)
        label2 = tk.Label(root, text='Username',font=self.font,bg='white')
        self.login_canvas.create_window(self.width_canv/4,self.height_canv*0.4, window=label2)
        #back_button
        back_button= tk.Button(self.main_Canvas, text = '⬅️Back ',fg ='white',bg ='blue',font=self.font, command=self.home_window,cursor = 'hand2')
        self.main_Canvas.create_window(self.width/20,self.height/20, window =  back_button)
        
        self.text_label = tk.Label(self.main_Canvas, text = 'Sign In',fg = 'blue', font = f'TkCaptionFont {int(0.045*self.height)} bold', bg = 'white')
        self.login_canvas.create_window(self.width/8,self.height*0.056,window = self.text_label)

        line = self.login_canvas.create_line(0,self.height_canv/3.5,self.width_canv+5,self.height_canv/3.5)
        
        fonter = f'Arial {int(0.020*self.height)} bold'
        self.sign_in = tk.Button(self.main_Canvas, text = 'Sign In', font = fonter, bd = 0, bg = 'white',fg = 'black', command = self.form,cursor = 'hand2')
        self.register = tk.Button(self.main_Canvas, text = 'Register', font = fonter, bg = 'blue', fg = 'white', command = self.register_form,cursor = 'hand2')
        
        self.main_Canvas.create_window(self.width_canv*1.614,self.height_canv*0.74, window =  self.sign_in)
        self.main_Canvas.create_window(self.width_canv*1.872,self.height_canv*0.74, window =  self.register)

    def  register_form(self):
        
        self.sign_in.config(bd = 2, bg = 'blue', fg = 'white')
        self.register.config(bd = 0, bg = 'white', fg = 'black')
        self.label1.config(text = 'New Password')
        self.captcha_addition()
        self.captcha_input.set('')
        self.password.set('')
        self.username.set('')
        self.status.config(text='')
        self.login_button.config(text = 'Register', command = self.register_user)
        self.show.set(0)
        self.text_label.config(text='Register')
        
        admin_button = tk.Button(self.main_Canvas, text = 'Admin', font = self.font, command = self.admin, bg = '#FF8033', fg = 'white', activebackground = '#FF8033', activeforeground = 'white',cursor = 'hand2')
        self.main_Canvas.create_window(0.95*self.width, 0.05*self.height, window = admin_button)
        
        #registration window
        
    def captcha_addition(self):
                      
        image = ImageCaptcha(width = 130, height = 130)
        captcha_word = utility.random_captcha()
        captcha = image.generate(captcha_word)
        captcha = Image.open(captcha).resize((int(0.292*self.width_canv),int(0.15*self.height_canv)))
        enhancer = ImageEnhance.Contrast(captcha)
        captcha = enhancer.enhance(1.5)
        tk_captcha = ImageTk.PhotoImage(captcha)
        self.login_canvas.create_image(self.width_canv/3.3,0.683*self.height_canv,image = tk_captcha)
        self.login_canvas.image = tk_captcha
        self.captcha = captcha_word
        
    def register_user(self):
        
        status_dict = {0:'Wrong Captcha', 1:'Username Invalid', 2:'Username Previously Registered', 3:'Password should be atleast 8 character long', 4:'Registration Done Successfully'}
        var_dict = {'username':self.username.get(),'password':self.password.get(),'real_captcha':self.captcha, 'user_captcha':self.captcha_input.get()}
        registration_status = utility.registration_status_code(var_dict)
        
#         print(self.captcha == self.captcha_input.get())
        
        if registration_status == 4:
            self.status.config(fg = 'green')
        else:
            self.status.config(fg = 'red')
            
        self.status.config(text = status_dict[registration_status])
    
    def login_user(self):
        
        status_dict = {0:'Wrong Captcha', 1:'Invalid Credentials'}
        var_dict = {'username':self.username.get(),'password':self.password.get(),'real_captcha':self.captcha, 'user_captcha':self.captcha_input.get()}
        login_status = utility.login_status_code(var_dict)
        
        if isinstance(login_status,dict):
            self.admission_form(login_status)
        else:
            self.status.config(fg = 'red', text = status_dict[login_status])
            
    def admin(self):
        
        self.main_Canvas.delete('all')
        back_button= tk.Button(self.main_Canvas, text = '⬅️Back ',fg ='white',bg ='blue',font=self.font, command=self.form,cursor = 'hand2')
        self.main_Canvas.create_window(self.width/20,self.height/20, window =  back_button)
        
        background_image = Image.open('assets/background_image.png').resize((self.width, self.height))
        tk_background_Image = ImageTk.PhotoImage(background_image)
        
        self.main_Canvas.create_image(self.width/2, self.height/2, image = tk_background_Image)
        self.main_Canvas.image = tk_background_Image
        
        #login_window
        self.width_canv = self.width/4
        self.height_canv = self.height/2.5
        self.login_canvas= tk.Canvas(self.main_Canvas, height = self.height_canv, width = self.width_canv, bg = 'white',highlightthickness = 0, relief = 'raised')
        self.main_Canvas.create_window(self.width_canv*2, self.height_canv*1.3, window = self.login_canvas)
        
        #login_button
        self.login_button = tk.Button(text='Login',fg ='white',bg ='blue',font=self.font,command=self.login_admin,cursor = 'hand2')
        self.login_canvas.create_window(self.width_canv/2,self.height_canv*0.85,window=self.login_button)
        
        self.status = tk.Label(self.login_canvas, font = self.font, bg = 'white')
        self.login_canvas.create_window(self.width_canv/2,self.height_canv*0.93,window=self.status)
        
        #Passowrd
        self.passcode = tk.StringVar()
        entry1 = tk.Entry(root, show = '*', font = self.font, textvariable = self.passcode) 
        self.login_canvas.create_window(self.width_canv/1.5,self.height_canv*0.5,window=entry1)
        
        self.label1 = tk.Label(root, text='Password',font=self.font,bg='white')
        self.login_canvas.create_window(self.width_canv/4,self.height_canv*0.5, window=self.label1)
        
        show = tk.IntVar(self.login_canvas)
        show_password = tk.Checkbutton(self.login_canvas, variable = show, text = 'Show password', font = self.font, bg = 'white', activebackground = 'white',cursor = 'hand2')
        self.login_canvas.create_window(self.width_canv/1.5,self.height_canv*0.58, window=show_password)
        
        def show_hide():
            
            if self.show.get() == 1:
                entry1.config(show = '')
                
            elif self.show.get() == 0:
                entry1.config(show = '*')
                
        show.trace('w', lambda x,y,z: show_hide())
        
        self.captcha_addition()
        self.captcha_input = tk.StringVar()
        captcha_entry = tk.Entry(self.login_canvas, text = self.font, textvariable = self.captcha_input)
        self.login_canvas.create_window(self.width_canv/1.55,self.height_canv*0.683, window=captcha_entry)
        
        self.captcha_input.trace('w', lambda x,y,z: self.captcha_input.set(self.captcha_input.get().upper()))
        
        reload_captcha = tk.Button(self.login_canvas, text = '⟳', command = self.captcha_addition, bd = 0, bg = 'white', activebackground = 'blue', activeforeground = 'white',cursor = 'hand2')
        self.login_canvas.create_window(self.width_canv/1.17,self.height_canv*0.683, window=reload_captcha)
        #Username
        self.admin_name = tk.StringVar()
        entry2 = tk.Entry (root, font = self.font, textvariable = self.admin_name) 
        self.login_canvas.create_window(self.width_canv/1.5,self.height_canv*0.4,window=entry2)
        label2 = tk.Label(root, text='Username',font=self.font,bg='white')
        self.login_canvas.create_window(self.width_canv/4,self.height_canv*0.4, window=label2)

        line = self.login_canvas.create_line(0,self.height_canv/3.5,self.width_canv+5,self.height_canv/3.5) 
        
        text_label = tk.Label(self.main_Canvas, text = 'Admin Login',fg = 'blue', font = f'TkCaptionFont {int(0.045*self.height)} bold', bg = 'white')
        self.login_canvas.create_window(self.width/8,self.height*0.056,window = text_label)
        
    def login_admin(self):
        
        status_dict = {0:'Wrong Captcha', 1:'Invalid Credentials',2:'Successful'}
        var_dict = {'username':self.admin_name.get(),'password':self.passcode.get(),'real_captcha':self.captcha, 'user_captcha':self.captcha_input.get()}
        admin_status = utility.admin_status_code(var_dict)
        
        if admin_status == 2:
            self.admin_form()
        else:
            self.status.config(fg = 'red', text = status_dict[admin_status])
            
    def admission_form(self, var_values):
        
        self.main_Canvas.delete('all')
        self.main_Canvas.config(bg = 'white')
        
        self.date=['01','02','03','04','05','06','07','08','09']
        self.month=['01','02','03','04','05','06','07','08','09','10','11','12']
        self.year=['98','99','00','01','02','03','04','05','06','07','08','09']
        self.dept=['CSE','IT','ECE','EE']
        self.board1=['CBSE','ICSE','WB','OTHERS']
        self.board2=['CBSE','ISC','WB','OTHERS']
        self.val=["Yes","No"]

        for i in range(10,32):
            j=str(i)
            self.date.append(j)
            if i<=21:
                self.year.append(j)
                
        self.a=0
        self.zzz1=0
        self.zzz2=0        
        def check_address():
            if self.a%2==0:
                permaA.insert(tk.END,presA.get(1.0,END))
                permaA.config(state='disabled')
                self.a=self.a+1
            else:
                permaA.delete("1.0", "end")
                permaA.config(state='active')
                self.a=self.a+1

        def check_id(email):
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            while(True):
                if(re.search(regex,email)):  
                    return True      
                else:  
                    tmg.showinfo("Error","Enter valid email id.")
                    return False
                if email==0:
                    break

        def guardian_phn_no(v1):
            V1=v1.get()[4:]
            pn=0
            try:
                n=0
                for i in V1:
                    k=int(i)
                    n+=1
                if n==10:
                    pn=1
                    return True
                else:
                    tmg.showinfo("Error","Enter valid guardian's phone number.")
            except:
                tmg.showinfo("Error","Enter valid guardian's phone number.")
            if pn==0:
                v1.set('+91 ')
                return False


        def student_phn_no(v2):
            V2=v2.get()[4:]
            pn=0
            try:
                n=0
                for i in V2:
                    k=int(i)
                    n+=1
                if n==10:
                    pn=1
                    return True
                else:
                    tmg.showinfo("Error","Enter valid student's phone number.")
            except:
                tmg.showinfo("Error","Enter valid student's phone number.")
            if pn==0:
                v2.set('+91 ')
                return False


        def DOB_dept_check(d1,m1,y1,de,comboExample):
            qq=int(y1)
            if d1 not in self.date:
                tmg.showinfo("Error","Enter valid date of birth.")
                return False
            elif d1=='31' or d1=='30' or d1=='29':
                if m1=='02' and d1!='29':    
                    tmg.showinfo("Error","Enter valid date of birth.")
                if d1=='29' and m1=='02' and qq%4!=0:
                    tmg.showinfo("Error","Enter valid date of birth.")
                if d1=='31':
                    if m1=='04' or m1=='06' or m1=='09' or m1=='11':
                        tmg.showinfo("Error","Enter valid date of birth.")
                        
                return False
            elif m1 not in self.month:
                tmg.showinfo("Error","Enter valid month of birth.")
                return False
            elif y1 not in self.year:
                tmg.showinfo("Error","Enter valid year of birth.")
                return False
            elif de not in self.dept:
                tmg.showinfo("Error","Enter valid department.")
                return False
            elif comboExample not in self.val:
                tmg.showinfo("Error","Invalid domicile certificate status.")
                return False
            else:
                return True

        def board_check(b10,b12):
            if b10 not in self.board1:
                tmg.showinfo("Error","Enter valid class X board name.")
                return False
            elif b12 not in self.board2:
                tmg.showinfo("Error","Enter valid class XII board name.")
                return False
            else:
                return True

        def cgpa_percentage_check(v,cgpa1):
            cccc=float(cgpa1)
            if v==1:
                if cccc<=10 and cccc>=0:
                    return True
                else:
                    tmg.showinfo("Error","Enter valid CGPA class X.")
                    return False
            if v==2:
                if cccc<=100 and cccc>=0:
                    return True
                else:
                    tmg.showinfo("Error","Enter valid percentage class X.")
                    return False


        width = self.width
        height = self.height
        col="antique white"
        col2="LightBlue1"
        
        font = f'Arial {int(0.013*height)} bold'
        font2= f'Arial {int(0.012*height)}'

        back_button= tk.Button(self.main_Canvas, text = '🏠 Log Out ',fg ='white',bg ='blue',font=self.font, command=self.form,cursor = 'hand2')
        self.main_Canvas.create_window(self.width/20,self.height/20, window =  back_button)

        background_image = Image.open('assets/background_image_2.jpg').resize((width, height))
        tk_background_Image = ImageTk.PhotoImage(background_image)

        self.main_Canvas.create_image(width/2, height/2, image = tk_background_Image)
        self.main_Canvas.image = tk_background_Image

        frame = tk.Frame(self.main_Canvas)
        self.main_Canvas.create_window(width/2.0217,height/1.89,window=frame)
        main_Canvas2=tk.Canvas(frame,height =0.88*height, width =0.992*width,scrollregion = (0,0,0,1.65*height),bg=col2)
        main_Canvas2.pack(side='left',expand=True,fill='both')

        scroll = tk.Scrollbar(frame,orient='vertical',command = main_Canvas2.yview)
        scroll.pack(side='left',fill='y')
        main_Canvas2.config(yscrollcommand = scroll.set)



        #Ishita's part
        frame=Canvas(main_Canvas2,relief="solid",borderwidth=1,width=0.80*width,height=0.19*height,bg=col)
        main_Canvas2.create_window(0.42*width,0.12*height,window=frame)

        name=Label(frame,text="* FIRST NAME :",bg=col,font=font)
        name.place(x=0.010*width,y=0.020*height)
        fentry1=StringVar()                                                       #1st name var
        fentry1=ttk.Entry(frame,font=font2)
        fentry1.place(x=0.14*width,y=0.020*height,width=0.25*width)

        name1=Label(frame,text="* LAST NAME :",bg=col,font=font)
        name1.place(x=0.42*width,y=0.020*height)
        fentry2=StringVar()                                                      #last name var
        fentry2=ttk.Entry(frame,font=font2)
        fentry2.place(x=0.52*width,y=0.020*height,width=0.25*width)

        name2=Label(frame,text="* FATHER'S NAME :",bg=col,font=font)
        name2.place(x=0.01*width,y=0.085*height)
        fentry3=StringVar()                                                     # father name var
        fentry3=ttk.Entry(frame,font=font2)
        fentry3.place(x=0.14*width,y=0.085*height,width=0.63*width)

        name3=Label(frame,text="* MOTHER'S NAME :",bg=col,font=font)
        name3.place(x=0.01*width,y=0.15*height)
        fentry4=StringVar()                                                      # mother name var
        fentry4=ttk.Entry(frame,font=font2)
        fentry4.place(x=0.14*width,y=0.15*height,width=0.63*width)

        #Aniket's Part
        f1=Canvas(main_Canvas2,relief="solid",borderwidth=1,width=0.33*width,height=0.06*height,bg=col)
        main_Canvas2.create_window(0.185*width,0.28*height,window=f1)
        l5=Label(f1,text="* GENDER :",font=font,bg=col)
        l5.place(x=0.010*width,y=0.02*height)
        ee5=IntVar()                                                             # gender var
        r1=Radiobutton(f1,text="MALE",font=font2,bg=col,variable=ee5,value=1)
        r1.place(x=0.09*width,y=0.02*height)
        r2=Radiobutton(f1,text="FEMALE",font=font2,bg=col,variable=ee5,value=2)
        r2.place(x=0.157*width,y=0.02*height)
        r3=Radiobutton(f1,text="OTHERS",font=font2,bg=col,variable=ee5,value=3)
        r3.place(x=0.24*width,y=0.02*height)

        f2=Canvas(main_Canvas2,relief="solid",borderwidth=1,width=0.21*width,height=0.06*height,bg=col)
        main_Canvas2.create_window(0.48*width,0.28*height,window=f2)
        ll=Label(f2,text="* DOB :",font=font,bg=col)
        ll.place(x=0.01*width,y=0.02*height)
        d1=ttk.Combobox(f2,value=self.date,width=int(0.0036*width))                  # date var of dob
        d1.place(x=0.070*width,y=0.02*height)
        d1.set("DD")
        m1=ttk.Combobox(f2,value=self.month,width=int(0.0036*width))                 # month var of dob
        m1.place(x=0.11*width,y=0.02*height)
        m1.set("MM")
        y1=ttk.Combobox(f2,value=self.year,width=int(0.0036*width))                   # year var of dob
        y1.place(x=0.15*width,y=0.02*height)
        y1.set("YY")

        f3=Canvas(main_Canvas2,relief="solid",borderwidth=1,width=0.21*width,height=0.06*height,bg=col)
        main_Canvas2.create_window(0.715*width,0.28*height,window=f3)
        l2=Label(f3,text="* DEPARTMENT :",font=font,bg=col)
        l2.place(x=0.01*width,y=0.02*height)
        de=ttk.Combobox(f3,value=self.dept,width=int(0.004*width))                     # department var
        de.place(x=0.13*width,y=0.02*height)


        #Shounak's Part
        f4=Canvas(main_Canvas2,relief="solid",borderwidth=1,width=0.80*width,height=0.19*height,bg=col)
        main_Canvas2.create_window(0.42*width,0.44*height,window=f4)

        ourMessage ="* GUARDIAN'S PHONE NUMBER :"                                #guardian's phn number
        messageVar = Label(f4,text=ourMessage,font=font,bg=col)
        messageVar.place(x=0.010*width,y=0.020*height)
        v1=tk.StringVar()
        ee1 = tk.Entry(f4,font=font2,width=int(0.045*height),textvariable=v1)
        ee1.place(x=0.195*width,y=0.020*height)
        v1.set("+91 ")
        ourMessage1 ="* STUDENT'S PHONE NUMBER :"                                #student's phn number
        messageVar1 = Label(f4,text=ourMessage1,font=font,bg=col)
        messageVar1.place(x=0.01*width,y=0.085*height)
        v2=tk.StringVar()
        ee2 = tk.Entry(f4,font=font2,width=int(0.045*height),textvariable=v2)
        ee2.place(x=0.195*width,y=0.088*height)
        v2.set("+91 ")

        ourMessage2 ="* DOMICILE CERTIFICATE :"
        messageVar2 = tk.Label(f4,text=ourMessage2,font=font,bg=col)
        messageVar2.place(x=0.01*width,y=0.15*height)
        comboExample = ttk.Combobox(f4,values=self.val,width=int(0.0036*width))     #domicile certificate presence
        comboExample.place(x=0.195*width,y=0.150*height)
        comboExample.current(1)

        #Ankita's Part
        canvas = tk.Canvas(main_Canvas2,height=0.48*height,relief="solid",borderwidth=1,width=0.44*width,bg=col)
        main_Canvas2.create_window(width*0.24,height*0.81,window=canvas)

        tk.Label(canvas,text="* MAIL ID :",font=font,bg=col).place(x=0.010*width,y=0.020*height)
        email = tk.StringVar()                                                                                     #email id
        tk.Entry(canvas,textvar=email,font=font2,relief="solid",bd=1,width=int(0.02*width),state='disabled').place(x=0.15*width,y=0.02*height)

        tk.Label(canvas,text="* PRESENT ADDRESS :",bg=col,font=font).place(x=0.010*width,y=0.085*height)
        presA = tk.Text(canvas,font=font2,relief="solid",bd=1,width=int(0.025*width),height =int(0.0085*height))   #present address
        presA.place(x=0.15*width,y=0.085*height)
        equal = tk.IntVar()

        tk.Label(canvas,text="* PERMANENT ADDRESS :",font=font,bg=col).place(x=0.010*width,y=0.265*height)
        check_ad = tk.Checkbutton(canvas,variable=equal,font=font2,bd=1,bg=col,text="Same as above address",command=check_address)
        check_ad.place(x=0.15*width,y=0.265*height)
        permaA = tk.Text(canvas,font=font2,relief="solid",width=int(0.025*width),height = int(0.0085*height))     #permenent address
        permaA.place(x=0.15*width,y=0.32*height)

        #Aniket's Part
        c=Canvas(main_Canvas2,relief="solid",borderwidth=1,width=0.33*width,height=0.254*height,bg=col)
        main_Canvas2.create_window(0.653*width,0.696*height,window=c)

        l10=Label(c,text="* CLASS X BOARD NAME :",font=font,bg=col)
        l10.place(x=0.01*width,y=0.02*height)
        b10=ttk.Combobox(c,values=self.board1,width=8)                            #class X board name
        b10.place(x=0.162*width,y=0.02*height)
        l101=Label(c,text="* CLASS X SCHOOL NAME :",font=font,bg=col)
        l101.place(x=0.01*width,y=0.085*height)
        en10=StringVar()
        en101=Entry(c,textvar=en10,font=font2,width=27,relief="solid",bd=1)  #class X school name
        en101.place(x=0.162*width,y=0.085*height)
        l102=Label(c,text="* CLASS XII SCHOOL NAME :",font=font,bg=col)
        l102.place(x=0.01*width,y=0.15*height)
        en12=StringVar()
        en102=Entry(c,textvar=en12,font=font2,width=27,relief="solid",bd=1)  #class XII school name
        en102.place(x=0.162*width,y=0.15*height)
        l12=Label(c,text="* CLASS XII BOARD NAME :",font=font,bg=col)
        l12.place(x=0.01*width,y=0.215*height)
        b12=ttk.Combobox(c,values=self.board2,width=8)                            #class XII board name
        b12.place(x=0.162*width,y=0.215*height)


        #Sumi's part
        c1=Canvas(main_Canvas2,relief="solid",borderwidth=1,width=0.33*width,height=0.19*height,bg=col)
        main_Canvas2.create_window(0.653*width,0.955*height,window=c1)

        Label(c1,text="* CGPA/PERCENTAGE OF X STANDARD:",font=font,bg=col).place(x=0.01*width,y=0.02*height)

        v=IntVar()                                                                                          #CGPA/Percentage class X
        cgpa_r = Radiobutton(c1,text="CGPA",variable=v,value=1,font=font2,bg=col)
        cgpa_r.place(x=0.235*width,y=0.02*height)
        perce_r = Radiobutton(c1,text="PERCENTAGE",variable=v,value=2,font=font2,bg=col)
        perce_r.place(x=0.235*width,y=0.085*height)
        
        cgpa1=Entry(c1, font=font2,width=5,relief="solid",bd=1)                                              #value of cgpa/percentage
        cgpa1.place(x=0.235*width,y=0.15*height)

        def callback1(*dummy):
            try:
                a = int(vv1.get())
                b = int(vv2.get())
                c = int(vv3.get())
                list = [a,b,c]
                for i in list:
                    if i<0 or i>100:
                        l1.config(text='')
                        return
                else:
                    s =round(sum(list)/3,2)
                    l1.config(text=str(s))  
                    self.zzz1=1
            except:
                l1.config(text='')
                self.zzz1=0
                return

        c2=Canvas(main_Canvas2,relief="solid",borderwidth=1,width=0.33*width,height=0.32*height,bg=col)
        main_Canvas2.create_window(0.653*width,1.25*height,window=c2)

        Label(c2,text="SUBJECT NAME (CLASS XII)",font=font,bg=col).place(x=0.01*width,y=0.02*height)
        Label(c2,text="MARKS",font=font,bg=col).place(x=0.235*width,y=0.02*height)

        Label(c2,text="* PHYSICS",font=font,bg=col).place(x=0.01*width,y=0.085*height)
        Label(c2,text="* CHEMISTRY",font=font,bg=col).place(x=0.01*width,y=0.15*height)
        Label(c2,text="* MATHEMATICS",font=font,bg=col).place(x=0.01*width,y=0.215*height)

        vv1=StringVar()                                                                             # physics marks
        vv2=StringVar()                                                                             #chemistry marks
        vv3=StringVar()                                                                             #maths marks

        e1=Entry(c2,width=5,bd=1,relief="solid",font=font2,textvariable=vv1)
        e1.place(x=0.235*width,y=0.085*height)
        e2=Entry(c2,width=5,bd=1,relief="solid",font=font2,textvariable=vv2)
        e2.place(x=0.235*width,y=0.15*height)
        e3=Entry(c2,width=5,bd=1,relief="solid",font=font2,textvariable=vv3)
        e3.place(x=0.235*width,y=0.215*height)

        vv1.trace('w',callback1)
        vv2.trace('w',callback1)
        vv3.trace('w',callback1)

        Label(c2,text="AGGREGATE %",font=font,bg=col).place(x=0.01*width,y=0.28*height)

        l1=Label(c2,text="",font=font2,bg="white",bd=1,width=5,relief="solid")                   # aggregate mark of class PCM
        l1.place(x=0.235*width,y=0.28*height)

        def callback(*dummy):
            try:
                a = int(t1.get())
                b = int(t2.get())
                c = int(t3.get())
                d = int(t4.get())
                e = int(t5.get())
                list = [a,b,c,d,e]
                for i in list:
                    if i<0 or i>100:
                        l.config(text='')
                        return
                else:
                    s =round(sum(list)/5,2)
                    l.config(text=str(s))  
                    self.zzz2=1
            except:
                l.config(text='')
                self.zzz2=0
                return

        c3=Canvas(main_Canvas2,relief="solid",borderwidth=1,width=0.44*width,height=0.45*height,bg=col)
        main_Canvas2.create_window(0.24*width,1.315*height,window=c3)
        Label(c3,text="ClASS XII MARKS",font=font,bg=col).place(x=0.01*width,y=0.02*height)
        Label(c3,text="SUBJECT NAME",font=font,bg=col).place(x=0.2*width,y=0.02*height)
        Label(c3,text="MARKS",font=font,bg=col).place(x=0.35*width,y=0.02*height)

        Label(c3,text="* FIRST SUBJECT",font=font,bg=col).place(x=0.01*width,y=0.085*height)
        Label(c3,text="* SECOND SUBJECT",font=font,bg=col).place(x=0.01*width,y=0.15*height)
        Label(c3,text="* THIRD SUBJECT",font=font,bg=col).place(x=0.01*width,y=0.215*height)
        Label(c3,text="* FOURTH SUBJECT",font=font,bg=col).place(x=0.01*width,y=0.28*height)
        Label(c3,text="* FIFTH SUBJECT",font=font,bg=col).place(x=0.01*width,y=0.345*height)

        t1=StringVar()                                                                            # 1st sub class 12
        t2=StringVar()                                                                            # 2nd sub class 12
        t3=StringVar()                                                                            # 3rd sub class 12
        t4=StringVar()                                                                            # 4th sub class 12
        t5=StringVar()                                                                            # 5th sub class 12

        e1a=Entry(c3,width=20,bd=1,relief="solid",font=font2)
        e1a.place(x=0.2*width,y=0.085*height)
        e2a=Entry(c3,width=20,bd=1,relief="solid",font=font2)
        e2a.place(x=0.2*width,y=0.15*height)
        e3a=Entry(c3,width=20,bd=1,relief="solid",font=font2)
        e3a.place(x=0.2*width,y=0.215*height)
        e4a=Entry(c3,width=20,bd=1,relief="solid",font=font2)
        e4a.place(x=0.2*width,y=0.28*height)
        e5a=Entry(c3,width=20,bd=1,relief="solid",font=font2)
        e5a.place(x=0.2*width,y=0.345*height)

        e1b=Entry(c3,width=5,bd=1,relief="solid",font=font2,textvariable=t1)
        e1b.place(x=0.35*width,y=0.085*height)
        e2b=Entry(c3,width=5,bd=1,relief="solid",font=font2,textvariable=t2)
        e2b.place(x=0.35*width,y=0.15*height)
        e3b=Entry(c3,width=5,bd=1,relief="solid",font=font2,textvariable=t3)
        e3b.place(x=0.35*width,y=0.215*height)
        e4b=Entry(c3,width=5,bd=1,relief="solid",font=font2,textvariable=t4)
        e4b.place(x=0.35*width,y=0.28*height)
        e5b=Entry(c3,width=5,bd=1,relief="solid",font=font2,textvariable=t5)
        e5b.place(x=0.35*width,y=0.345*height)

        t1.trace('w',callback)
        t2.trace('w',callback)
        t3.trace('w',callback)
        t4.trace('w',callback)
        t5.trace('w',callback)

        Label(c3,text="BEST OF FIVE AGGREGATE %",font=font,bg=col).place(x=0.01*width,y=0.41*height)

        l=Label(c3,text="",bg="white",bd=1,relief="solid",width=5,font=font2)                           # aggregate of class 12
        l.place(x=0.35*width,y=0.41*height)

        c4=Canvas(main_Canvas2,relief="solid",borderwidth=1,width=0.33*width,height=0.09*height,bg=col)
        main_Canvas2.create_window(0.653*width,1.494*height,window=c4)
        sss1=IntVar()
        sss2=IntVar()
        term1 = tk.Checkbutton(c4,font=font2,bd=1,bg=col,text="* All the information provided above is true to my knowledge.",variable=sss1)
        term1.place(x=0.01*width,y=0.02*height)
        term2 = tk.Checkbutton(c4,font=font2,bd=1,bg=col,text="* I will abide by the rules and regulations of the institute.",variable=sss2)
        term2.place(x=0.01*width,y=0.055*height)


        def click():
            if fentry1.get()=="":
                tmg.showinfo("Error","Enter first name.")
            elif fentry2.get()=="":
                tmg.showinfo("Error","Enter last name.")
            elif fentry3.get()=="":
                tmg.showinfo("Error","Enter father's name.")
            elif fentry4.get()=="":
                tmg.showinfo("Error","Enter mother's name.")
            elif ee5.get()==0:
                tmg.showinfo("Error","Enter gender.")
            elif d1.get()=="DD":
                tmg.showinfo("Error","Enter date of birth.")
            elif m1.get()=="MM":
                tmg.showinfo("Error","Enter month of birth.")
            elif y1.get()=="YY":
                tmg.showinfo("Error","Enter year of birth.")
            elif de.get()=="":
                tmg.showinfo("Error","Enter department.")
            elif v1.get()=="" or v1.get()=="+91":
                tmg.showinfo("Error","Enter guardian's phone number.")
            elif v2.get()=="" or v2.get()=="+91":
                tmg.showinfo("Error","Enter student's phone number.")
            elif comboExample.get()=="":
                tmg.showinfo("Error","Enter domicile certificate status.")
            elif email.get()=="":
                tmg.showinfo("Error","Enter email id.")
            elif b10.get()=="":
                tmg.showinfo("Error","Enter class X board name.")
            elif en10.get()=="":
                tmg.showinfo("Error","Enter class X school name.")
            elif en12.get()=="":
                tmg.showinfo("Error","Enter class XII school name.")
            elif b12.get()=="":
                tmg.showinfo("Error","Enter class XII board name.")
            elif len(presA.get(1.0,END))==1:
                tmg.showinfo("Error","Enter present address.")
            elif len(permaA.get(1.0,END))==1:
                tmg.showinfo("Error","Enter permanent address.")
            elif v.get()==0:
                tmg.showinfo("Error","Select an alternative (CGPA/Percentage for class X).")
            elif cgpa1.get()=="":
                tmg.showinfo("Error","Enter CGPA/Percentage for class X.")
            elif self.zzz1==0:
                tmg.showinfo("Error","Enter valid PCM marks.")
            elif e1a.get()=="" or e2a.get()=="" or e3a.get()=="" or e4a.get()=="" or e5a.get()=="":
                tmg.showinfo("Error","Enter class XII subject name(s).")
            elif self.zzz2==0:
                tmg.showinfo("Error","Enter valid class XII marks.")
            elif sss1.get()==0:
                tmg.showinfo("Error","Please accept terms and conditions.")
            elif sss2.get()==0:
                tmg.showinfo("Error","Please accept terms and conditions.")
            else:
                if not DOB_dept_check(d1.get(),m1.get(),y1.get(),de.get(),comboExample.get()):
                    return
                elif not guardian_phn_no(v1):
                    return
                elif not student_phn_no(v2):
                    return
                elif not check_id(email.get()):
                    return
                elif not board_check(b10.get(),b12.get()):
                    return
                elif not cgpa_percentage_check(v.get(),cgpa1.get()):
                    return
                else:
                    record = var_values['record']
                    var_values.pop('record')
                    var_values['Registration Number'] = lc.registration_number()
                    var_values['Name'] = fentry1.get().strip() + ' ' + fentry2.get().strip()
                    var_values['DOB'] = d1.get() + '/' + m1.get() + '/' + y1.get()
                    var_values['Father\'s Name'] = fentry3.get()
                    var_values['Mother\'s Name'] = fentry4.get()
                    var_values['Gender'] = {1:'Male',2:'Female',3:'Others'}[ee5.get()]
                    var_values['Domicile'] = comboExample.get()
                    var_values['Dept'] = de.get()
                    var_values['Guardian\'s Phone Number'] = v1.get()[4:]
                    var_values['Student\'s Phone Number'] = v2.get()[4:]
                    var_values['Present Address'] = presA.get(1.0,END)
                    var_values['Permanent Address'] = permaA.get(1.0,END)
                    var_values['High School Name'] = en10.get()
                    var_values['High School Board Name'] = b10.get()
                    var_values['High School Marks'] = cgpa1.get() + {1:'(CGPA)', 2:'%'}[v.get()]
                    var_values['Higher Secondary School Name'] = en12.get()
                    var_values['Higher Secondary Board Name'] = b12.get()
                    var_values['High Secondary Marks(P,C,M,Agg)'] = f'({vv1.get()},{vv2.get()},{vv3.get()},{round(sum([int(vv1.get()),int(vv2.get()),int(vv3.get())])/3,2)})'
                    
                    bst_5 = f'{e1a.get()}:{t1.get()},{e2a.get()}:{t2.get()},{e3a.get()}:{t3.get()},{e4a.get()}:{t4.get()},{e5a.get()}:{t5.get()}'
                    a = int(t1.get())
                    b = int(t2.get())
                    c = int(t3.get())
                    d = int(t4.get())
                    e = int(t5.get())
                    lst = [a,b,c,d,e]
                    s =round(sum(lst)/5,2)
                    bst_5 += f',Aggregate:{s}'
                    var_values['Higher Secondary Best of 5'] = bst_5
                    
                    lc.submit_save(list(var_values.values()),record)
                    self.admission_form(var_values)
#                     print(var_values)
        email.set(var_values['Email Id'])
    
        c5=Canvas(main_Canvas2,relief="solid",borderwidth=1,width=0.042*width,height=0.032*height)
        main_Canvas2.create_window(0.795*width,1.6*height,window=c5)
        submit_button= tk.Button(c5, text = 'Submit ',fg ='white',bg ='blue',font = font,command=click,cursor = 'hand2')         #submit button
        #submit_button.bind("<Button-1>",click)
        submit_button.pack()
        
        if var_values['Registration Number'] != '':
            
            reg = var_values['Registration Number']
            font_reg = f'Arial {int(0.04*self.height)} bold'
            label = tk.Label(self.main_Canvas,text=f'Registration Number:{reg}',fg = 'white',bg = '#00004E',font=font_reg)
            self.main_Canvas.create_window(self.width*0.5,self.height/20,window=label)
            
            submit_button.config(state='disabled',cursor='arrow')
            
            a,b = var_values['Name'].split()
            fentry1.insert(0,a)
            fentry2.insert(0,b)
            fentry1.config(state='disabled')
            fentry2.config(state='disabled')

            fentry3.insert(0,var_values['Father\'s Name'])
            fentry3.config(state='disabled')
        
            fentry4.insert(0,var_values['Mother\'s Name'])
            fentry4.config(state='disabled')
            
            ee5.set({'Male':1,'Female':2,'Others':3}[var_values['Gender']])
            r1.config(state='disabled')
            r2.config(state='disabled')
            r3.config(state='disabled')
            
            d,m,y = var_values['DOB'].split('/')
            d1.set(d)
            m1.set(m)
            y1.set(y)
            d1.config(state='disabled')
            m1.config(state='disabled')
            y1.config(state='disabled')
        
            de.set(var_values['Dept'])
            de.config(state='disabled')
            
            g_num = '+91 ' + var_values['Guardian\'s Phone Number']
            v1.set(g_num)
            ee1.config(state='disabled')
            
            s_num = '+91 ' + var_values['Student\'s Phone Number']
            v2.set(s_num)
            ee2.config(state='disabled')
            
            comboExample.set(var_values['Domicile'])
            comboExample.config(state='disabled')
            
            presA.insert(1.0,var_values['Present Address'])
            permaA.insert(1.0,var_values['Permanent Address'])
            presA.config(state='disabled')
            permaA.config(state='disabled')
            check_ad.config(state='disabled')
            
            en10.set(var_values['High School Name'])
            en101.config(state='disabled')
            b10.set(var_values['High School Board Name'])
            b10.config(state='disabled')
            
            marks = 0
            if var_values['High School Marks'][-1] == '%':
                v.set(2)
                marks = var_values['High School Marks'][:-1]
            else:
                v.set(1)
                marks = var_values['High School Marks'][:-6]
            
            cgpa1.insert(0,marks)
            cgpa1.config(state='disabled')
            cgpa_r.config(state='disabled')
            perce_r.config(state='disabled')
            
            en12.set(var_values['Higher Secondary School Name'])
            en102.config(state='disabled')
            b12.set(var_values['Higher Secondary Board Name'])
            b12.config(state='disabled')
            
            p,c,m,a = var_values['High Secondary Marks(P,C,M,Agg)'][1:-1].split(',')
            vv1.set(p)
            vv2.set(c)
            vv3.set(m)
            e1.config(state='disabled')
            e2.config(state='disabled')
            e3.config(state='disabled')
            l1.config(text=a)
            
            #e1b,e2b,e3b,e4b,e5b value
            subjects = []
            marks = []
            for item in var_values['Higher Secondary Best of 5'].split(','):
                s,m = item.split(':')
                subjects.append(s)
                marks.append(m)
                
            t1.set(marks[0])
            t2.set(marks[1])
            t3.set(marks[2])
            t4.set(marks[3])
            t5.set(marks[4])
            l.config(text = marks[5])
            
            e1a.insert(0,subjects[0])
            e2a.insert(0,subjects[1])
            e3a.insert(0,subjects[2])
            e4a.insert(0,subjects[3])
            e5a.insert(0,subjects[4])
            
            e1a.config(state='disabled')
            e2a.config(state='disabled')
            e3a.config(state='disabled')
            e4a.config(state='disabled')
            e5a.config(state='disabled')
            
            e1b.config(state='disabled')
            e2b.config(state='disabled')
            e3b.config(state='disabled')
            e4b.config(state='disabled')
            e5b.config(state='disabled')
            
            sss1.set(1)
            sss2.set(1)
            term1.config(state='disabled')
            term2.config(state='disabled')
            
        def on_mousewheel(event):
            main_Canvas2.yview_scroll(int(-1*(event.delta/120)), "units")
        
        #scroll bind
        def bound_to_mousewheel(event):
            main_Canvas2.bind_all("<MouseWheel>", on_mousewheel)   
        
        #scroll unbind
        def unbound_to_mousewheel(event):
            main_Canvas2.unbind_all("<MouseWheel>") 
        
        #scroll bind on enter
        main_Canvas2.bind('<Enter>', bound_to_mousewheel)
        
        #scroll unbind on exit
        main_Canvas2.bind('<Leave>', unbound_to_mousewheel)
            
    def admin_form(self):
        
        self.main_Canvas.delete('all')
        back_button= tk.Button(self.main_Canvas, text = 'Log Out ',fg ='white',bg ='blue',font=self.font, command=self.form)
        self.main_Canvas.create_window(self.width/20,self.height/20, window =  back_button)
        
        button = tk.Button(self.main_Canvas,text='See Database',bg = 'blue',fg='white',activebackground='blue',activeforeground='white',font=self.font,command=utility.open_file)
        self.main_Canvas.create_window(self.width/2,self.height/4,window=button)
        
        labeltext = f'Total Applications: {admin_statistics.count_applicants()}'
        total_Count = tk.Label(self.main_Canvas,text = labeltext,fg = 'green',bg='white',font = f'Arial {int(0.045*self.height)} bold')
        self.main_Canvas.create_window(self.width/2,self.height/6,window=total_Count)
        
root = tk.Tk()
a = app(root)
a.mainloop()