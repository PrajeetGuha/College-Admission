#for others

from win32api import GetSystemMetrics
import tkinter as tk
from PIL import Image,ImageTk

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
root = tk.Tk()
root.resizable(0,0)
root.state('zoomed')
dimension = f'{width}x{height}'
root.geometry(dimension)

main_Canvas = tk.Canvas(root,height = height, width = width, highlightthickness = 0)
main_Canvas.pack(padx = 0, pady = 0,fill = 'both', expand = True)

font = f'Arial {int(0.013*height)} bold'
back_button= tk.Button(main_Canvas, text = 'Log Out ',fg ='white',bg ='blue',font = font, command = None)
main_Canvas.create_window(width/20,height/20, window =  back_button)

background_image = Image.open('background_image_2.jpg').resize((width, height))
tk_background_Image = ImageTk.PhotoImage(background_image)

main_Canvas.create_image(width/2, height/2, image = tk_background_Image)
main_Canvas.image = tk_background_Image

default_field_values = {'Name':'','Email':'janowarsumideb@goru.com','Phone Number':'', 'Gender': '', 'Present Address': '', 'Permanent Address': '', 'Father_name':'', 'Mother_name':'', 'Father phone':'', 'Mother phone':'', 'X Total Score':'', 'X Percentage':'', 'XII Total Score':'', 'XII Percentage':'', 'X Board':'', 'XII Board':''}

root.mainloop()