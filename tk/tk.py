#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

def action1():
    var1.set("Status: 'Btn 1' button was clicked")
    var2.set("Instruction: Please click the 'Btn 2' button")

def action2():
    var1.set("Status: 'Btn 2' button was clicked")
    var2.set("Instruction: Please click the 'Btn 3' button")

def action3():
    var1.set("Status: 'Btn 3' button was clicked")
    var2.set("Instruction: Please click the 'x' to exit")

# Initiate toplevel widget
root = tk.Tk()

# Title
root.winfo_toplevel().title("Tkinter test app")

# Main frame
frame = tk.Frame(root)
frame.pack() # This geometry manager organizes widgets in blocks
# Subframe
top_frame = tk.Frame(root)
top_frame.pack(side='top')

# Buttons
btn1 = tk.Button(frame, text='Btn 1', fg='gainsboro', bg='#0070ad',
        activeforeground='white', activebackground='#12ABDB', command=action1)
btn1.pack(side='left')
btn2 = tk.Button(frame, text='Btn 2', fg='gainsboro', bg='#0070ad',
        activeforeground='white', activebackground='#12ABDB', command=action2)
btn2.pack(side='left')
btn3 = tk.Button(frame, text='Btn 3', fg='gainsboro', bg='#0070ad',
        activeforeground='white', activebackground='#12ABDB', command=action3)
btn3.pack(side='left')

# Labels
var1 = tk.StringVar()
label = tk.Label(top_frame, textvariable=var1, fg='#0070ad')
var1.set("Status: Initial")
label.pack(side='top')
var2 = tk.StringVar()
label = tk.Label(top_frame, textvariable=var2, fg='#0070ad')
var2.set("Instruction: Please click the 'Btn 1' button")
label.pack(side='top')

root.mainloop()
