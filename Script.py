#Modules
import tkinter as tk
import os
import subprocess
import pickle
from PIL import ImageTk, Image



















#Image
root =tk.Tk()
root.configure(bg="#00736E")

root.resizable(width=True, height=True)

img = Image.open("drag.png")
img = img.resize((500, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = tk.Label(root, image=img,borderwidth=0)
panel.image = img
panel.pack()

###

#Labels
filename =tk.StringVar(root)
extension =tk.StringVar(root)
location =tk.StringVar(root)

tk.Label(root, text='Enter File Name',width=2500,
         font=("Footlight MT Light",30,"bold"),
         bg="#00736E").pack()

e1 = tk.Entry(root,font=("Ariel",15),
              textvariable = filename,width=80,
              fg="red",selectbackground='violet').pack()

tk.Label(root,text='Enter File Extension (.__)',
         width=2500,font=("Footlight MT Light",30,"bold"),
         bg="#00736E").pack()

e2 = tk.Entry(root,font=("Ariel",15),
              textvariable = extension,width=70,
              fg="red",selectbackground='violet').pack()

####

##Running functions
     #main function cum data load

    
countt=0   
def run(path):

    global countt
    data_file=open("data file.dat","rb+")
    
    countt=0
    
    
    q=filename.get()+("."+extension.get())
    if path==1:
        path=location.get()+":\\"
    for root, dirs, files in os.walk(path):
        
        if q in files:
            if root[-1]!="\\":
                root = (root+"\\"+q)
            else:
                root = (root+q)
            pickle.dump(root,data_file)
            print("File found in", root)
            countt+=1
            continue
    data_file.close()

    
    if countt==0:
        print("File not found in",path)
    if countt>=1:
        print("Data Updated\n")
        

#####



def full(path):
    global countt
    driveStr = subprocess.check_output("fsutil fsinfo drives")
    driveStr = driveStr.decode()
    driveStr = driveStr.strip().lstrip('Drives: ')
    drives = driveStr.split()
    for drive in drives:
        fi=run(drive)
        if countt>=1:
            break
    
def button(path):
    if path==2:
        button1 = tk.Button(root,
                    text='Submit',fg='White',
                    bg= '#013220',height = 2,
                    width = 15,
                        command=lambda:full(path)).pack()
    else:
        button1 = tk.Button(root,
                    text='Submit', fg='White',
                    bg= '#013220',height = 2,
                    width = 15,
                        command=lambda:run(path)).pack()
    
class cls():
    def __init__(self):
        self.count=1
    def C(self):
        if self.count==1:
            button("C:\\")
        self.count-=1
        
    def D(self):
        if self.count==1:
            button("D:\\")
        self.count-=1
        
    def E(self):
        if self.count==1:
            button("E:\\")
        self.count-=1

    def custom(self):
        if self.count==1:
            tk.Label(root, text='Select File Location',
                width=150,
                font=("Footlight MT Light",30,"bold"),
                bg="#00736E").pack()
            e3 = tk.Entry(root,font=("Ariel",12),
                textvariable = location,width=70,
                fg="red",
                selectbackground='violet').pack()
            button(1)
        self.count-=1

    def full_sweep(self):
        if self.count==1:
            button(2)
        self.count-=1
            
#####



X=cls()




        
##Directory choice
        
   

var = tk.IntVar()  
tk.Radiobutton(root, text='C', variable=var,
               font=("Agency Fb",15,"bold"),
               bg="#00736E",command=lambda:X.C()).pack()
tk.Radiobutton(root, text='D',variable=var,
               font=("Agency Fb",15,"bold"),
               bg="#00736E" ,command=lambda:X.D()).pack()
tk.Radiobutton(root, text='E',variable=var,
               font=("Agency Fb",15,"bold"),
               bg="#00736E",command=lambda:X.E()).pack()
tk.Radiobutton(root, text='Custom',variable=var,
               font=("Agency Fb",15,"bold"),
               bg="#00736E",command=lambda:X.custom()).pack()
tk.Radiobutton(root, text='Full Sweep',variable=var,
            font=("Agency Fb",15,"bold"),
            bg="#00736E",command=lambda:X.full_sweep()).pack()



###
   


root.mainloop()
print("ThankYou For Using Our Services")
