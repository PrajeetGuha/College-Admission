import tkinter as tk
import pandas as pd
from win32api import GetSystemMetrics
from PIL import Image,ImageTk,ImageEnhance
from dependencies import validation,utility,admin_statistics
from captcha.image import ImageCaptcha
import os,sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

logo_img = resource_path("assets/logo.png")
background_img = resource_path('assets/background_image.png')

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
        self.master.iconphoto(False,tk.PhotoImage(file = logo_img))
        self.master.title(int(0.15*self.width)*' ' + 'Student Portal')
        self.pack()
        
        self.font = f'Arial {int(0.013*self.height)} bold'
        
        self.main_Canvas = tk.Canvas(self,height = self.height, width = self.width, highlightthickness = 0,bg='white')
        self.main_Canvas.pack(padx = 0, pady = 0,fill = 'both', expand = True)
        self.home_window()
        
    def home_window(self):
        self.main_Canvas.delete('all')
        background_image = Image.open(background_img).resize((self.width, self.height))
        logo = Image.open(logo_img).resize((int(0.219*self.width), int(0.390*self.height)))
        new_background_image = Image.new('RGBA', (self.width,self.height))
        new_background_image.paste(background_image, (0,0))
        new_background_image.paste(logo, (int(self.width/2.55), int(self.height/11)), mask = logo)
        tk_background_Image = ImageTk.PhotoImage(new_background_image)
        
        self.main_Canvas.create_image(self.width/2, self.height/2, image = tk_background_Image)
        self.main_Canvas.image = tk_background_Image
        
        welcome_canvas = tk.Canvas(self.main_Canvas, height = self.height/3, width = self.width/1.5, bg = 'white',highlightcolor = 'black')
        self.main_Canvas.create_window(self.width/2, self.height/1.3, window = welcome_canvas)
        
        admission_button = tk.Button(self.main_Canvas, text = ' ADMISSION FORM ', fg = 'white',bg ='blue',font=self.font,command= self.form)
        self.main_Canvas.create_window(self.width/2, self.height/1.85, window = admission_button)
        
    def form(self):
        
        background_image = Image.open(background_img).resize((self.width, self.height))
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
        self.login_button = tk.Button(text='Login',fg ='white',bg ='blue',font=self.font,command=self.login_user)
        self.login_canvas.create_window(self.width_canv/2,self.height_canv*0.85,window=self.login_button)
        
        self.status = tk.Label(self.login_canvas, font = self.font, bg = 'white')
        self.login_canvas.create_window(self.width_canv/2,self.height_canv*0.93,window=self.status)
        
        #Passowrd
        self.password = tk.StringVar()
        entry1 = tk.Entry(root, show = '*', font = self.font, textvariable = self.password) 
        self.login_canvas.create_window(self.width_canv/1.5,self.height_canv*0.5,window=entry1)
        
        self.label1 = tk.Label(root, text='Password',font=self.font,bg='white')
        self.login_canvas.create_window(self.width_canv/4,self.height_canv*0.5, window=self.label1)
        
        show = tk.IntVar(self.login_canvas)
        show_password = tk.Checkbutton(self.login_canvas, variable = show, text = 'Show password', font = self.font, bg = 'white', activebackground = 'white')
        self.login_canvas.create_window(self.width_canv/1.5,self.height_canv*0.58, window=show_password)
        
        admin_button = tk.Button(self.main_Canvas, text = 'Admin', font = self.font, command = self.admin, bg = '#FF8033', fg = 'white', activebackground = '#FF8033', activeforeground = 'white')
        self.main_Canvas.create_window(0.95*self.width, 0.05*self.height, window = admin_button)
        
        def show_hide():
            
            if show.get() == 1:
                entry1.config(show = '')
                
            elif show.get() == 0:
                entry1.config(show = '*')
                
        show.trace('w', lambda x,y,z: show_hide())
        
        self.captcha_addition()
        self.captcha_input = tk.StringVar()
        captcha_entry = tk.Entry(self.login_canvas, text = self.font, textvariable = self.captcha_input)
        self.login_canvas.create_window(self.width_canv/1.55,self.height_canv*0.683, window=captcha_entry)
        
        self.captcha_input.trace('w', lambda x,y,z: self.captcha_input.set(self.captcha_input.get().upper()))
        
        reload_captcha = tk.Button(self.login_canvas, text = '⟳', command = self.captcha_addition, bd = 0, bg = 'white', activebackground = 'blue', activeforeground = 'white')
        self.login_canvas.create_window(self.width_canv/1.17,self.height_canv*0.683, window=reload_captcha)
        #Username
        self.username = tk.StringVar()
        entry2 = tk.Entry (root, font = self.font, textvariable = self.username) 
        self.login_canvas.create_window(self.width_canv/1.5,self.height_canv*0.4,window=entry2)
        label2 = tk.Label(root, text='Username',font=self.font,bg='white')
        self.login_canvas.create_window(self.width_canv/4,self.height_canv*0.4, window=label2)
        #back_button
        back_button= tk.Button(self.main_Canvas, text = '⬅️Back ',fg ='white',bg ='blue',font=self.font, command=self.home_window)
        self.main_Canvas.create_window(self.width/20,self.height/20, window =  back_button)

        line = self.login_canvas.create_line(0,self.height_canv/3.5,self.width_canv+5,self.height_canv/3.5)
        
        fonter = f'Arial {int(0.020*self.height)} bold'
        self.sign_in = tk.Button(self.main_Canvas, text = 'Sign In', font = fonter, bd = 0, bg = 'white',fg = 'black', command = self.form)
        self.register = tk.Button(self.main_Canvas, text = 'Register', font = fonter, bg = 'blue', fg = 'white', command = self.register_form)
        
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
        
        admin_button = tk.Button(self.main_Canvas, text = 'Admin', font = self.font, command = self.admin, bg = '#FF8033', fg = 'white', activebackground = '#FF8033', activeforeground = 'white')
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
        back_button= tk.Button(self.main_Canvas, text = '⬅️Back ',fg ='white',bg ='blue',font=self.font, command=self.form)
        self.main_Canvas.create_window(self.width/20,self.height/20, window =  back_button)
        
        background_image = Image.open(background_img).resize((self.width, self.height))
        tk_background_Image = ImageTk.PhotoImage(background_image)
        
        self.main_Canvas.create_image(self.width/2, self.height/2, image = tk_background_Image)
        self.main_Canvas.image = tk_background_Image
        
        #login_window
        self.width_canv = self.width/4
        self.height_canv = self.height/2.5
        self.login_canvas= tk.Canvas(self.main_Canvas, height = self.height_canv, width = self.width_canv, bg = 'white',highlightthickness = 0, relief = 'raised')
        self.main_Canvas.create_window(self.width_canv*2, self.height_canv*1.3, window = self.login_canvas)
        
        #login_button
        self.login_button = tk.Button(text='Login',fg ='white',bg ='blue',font=self.font,command=self.login_admin)
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
        show_password = tk.Checkbutton(self.login_canvas, variable = show, text = 'Show password', font = self.font, bg = 'white', activebackground = 'white')
        self.login_canvas.create_window(self.width_canv/1.5,self.height_canv*0.58, window=show_password)
        
        admin_button = tk.Button(self.main_Canvas, text = 'Admin', font = self.font, command = self.admin, bg = '#FF8033', fg = 'white', activebackground = '#FF8033', activeforeground = 'white')
        self.main_Canvas.create_window(0.95*self.width, 0.05*self.height, window = admin_button)
        
        def show_hide():
            
            if show.get() == 1:
                entry1.config(show = '')
                
            elif show.get() == 0:
                entry1.config(show = '*')
                
        show.trace('w', lambda x,y,z: show_hide())
        
        self.captcha_addition()
        self.captcha_input = tk.StringVar()
        captcha_entry = tk.Entry(self.login_canvas, text = self.font, textvariable = self.captcha_input)
        self.login_canvas.create_window(self.width_canv/1.55,self.height_canv*0.683, window=captcha_entry)
        
        self.captcha_input.trace('w', lambda x,y,z: self.captcha_input.set(self.captcha_input.get().upper()))
        
        reload_captcha = tk.Button(self.login_canvas, text = '⟳', command = self.captcha_addition, bd = 0, bg = 'white', activebackground = 'blue', activeforeground = 'white')
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
        back_button= tk.Button(self.main_Canvas, text = 'Log Out ',fg ='white',bg ='blue',font=self.font, command=self.form)
        self.main_Canvas.create_window(self.width/20,self.height/20, window =  back_button)
        
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