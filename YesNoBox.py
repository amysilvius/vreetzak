import tkinter as tk
from tkinter import messagebox

root= tk.Tk() # create window

canvas1 = tk.Canvas(root, width = 300, height = 150)
canvas1.pack()



def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Alcohol Addicts','Vindt je me leuk?',icon = 'question')
    if MsgBox == 'yes':
       tk.messagebox.showinfo('Alcohol Addicts','Mooi, ik jou ook :) Wanneer bier?')
       root.destroy()
    else:
        tk.messagebox.showinfo('Alcohol Addicts','Oh shit verkeerde Tijmen, sorry')
        root.destroy()
        

button1 = tk.Button (root, text='Klik op mij',command=ExitApplication)
canvas1.create_window(130, 80, window=button1)
  
  
root.mainloop()

