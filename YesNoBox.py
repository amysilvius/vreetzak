import tkinter as tk
from tkinter import messagebox

root= tk.Tk() # create window

canvas1 = tk.Canvas(root, width = 300, height = 150)
canvas1.pack()

# Gemaakt door Amy/vreetzak

def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Alcohol Addicts',"Houd je van tosti's?",icon = 'question')
    if MsgBox == 'yes':
       tk.messagebox.showinfo('Alcohol Addicts','2 plakjes kaas toch?')
    #  root.destroy()
    else:
        tk.messagebox.showinfo('Alcohol Addicts','Schande')
        root.destroy()
    MsgBox = tk.messagebox.askquestion ('Alcohol Addicts',"Houd je van bier?",icon = 'question')
    if MsgBox == 'yes':
       tk.messagebox.showinfo('Alcohol Addicts','Een echte man')
    #  root.destroy()
    else:
        tk.messagebox.showinfo('Alcohol Addicts','Wat een teleurstelling')
    #  root.destroy()
    MsgBox = tk.messagebox.askquestion ('Alcohol Addicts',"Houd je van katten?",icon = 'question')
    if MsgBox == 'yes':
       tk.messagebox.showinfo('Alcohol Addicts','Goed zo')
    #  root.destroy()
    else:
        tk.messagebox.showinfo('Alcohol Addicts','Leugenaar')
    #  root.destroy()
    MsgBox = tk.messagebox.askquestion ('Alcohol Addicts',"Houd je van boeren laten?",icon = 'question')
    if MsgBox == 'yes':
       tk.messagebox.showinfo('Alcohol Addicts','*burp*')
    #  root.destroy()
    else:
        tk.messagebox.showinfo('Alcohol Addicts','Ben je wel een echte man?')
    #  root.destroy()
    MsgBox = tk.messagebox.askquestion ('Alcohol Addicts',"Houd je van schildpadden?",icon = 'question')
    if MsgBox == 'yes':
       tk.messagebox.showinfo('Alcohol Addicts','Ahh, je wordt er warm van')
    #  root.destroy()
    else:
        tk.messagebox.showinfo('Alcohol Addicts','Ahh, je wordt er koud van')
    #  root.destroy()
    MsgBox = tk.messagebox.askquestion ('Alcohol Addicts',"Ken je Python?",icon = 'question')
    if MsgBox == 'yes':
       tk.messagebox.showinfo('Alcohol Addicts','Goed bezig!')
    #  root.destroy()
    else:
        tk.messagebox.showinfo('Alcohol Addicts','Ik ook niet')
    #  root.destroy()
    MsgBox = tk.messagebox.askquestion ('Alcohol Addicts','Vindt je Amy leuk?',icon = 'question')
    if MsgBox == 'yes':
       tk.messagebox.showinfo('Alcohol Addicts','Mooi, ik jou ook :) Wanneer bier?')
    #  root.destroy()
    else:
        tk.messagebox.showerror('Alcohol Addicts','Oh shit verkeerde Tijmen, sorry')
    #  root.destroy()
    MsgBox = tk.messagebox.askquestion ('Alcohol Addicts',"Heb je ook op de meeste vragen Ja geantwoord? Dan heb je veel in gemeen met Amy",icon = 'question')
    if MsgBox == 'yes':
       tk.messagebox.showinfo('Alcohol Addicts','Bijna een perfecte match!')
    #  root.destroy()
    else:
        tk.messagebox.showinfo('Alcohol Addicts','Bijna een perfecte match!')
    #  root.destroy()
    MsgBox = tk.messagebox.askquestion ('Alcohol Addicts',"Waarom hebben gorillas grote neusgaten?",icon = 'question')
    if MsgBox == 'ok':
       tk.messagebox.askokcancel('Alcohol Addicts','Grote vingers')
    #  root.destroy()
    MsgBox = tk.messagebox.askquestion ('Alcohol Addicts',"Hoe betaalt een dinosaurus z'n rekening?",icon = 'question')
    if MsgBox == 'ok':
       tk.messagebox.askokcancel('Alcohol Addicts','Met een tyrannosaurus checks')
    #  root.destroy()

    

        

button1 = tk.Button (root, text='Klik op mij',command=ExitApplication)
canvas1.create_window(130, 80, window=button1)
  
  
root.mainloop()

