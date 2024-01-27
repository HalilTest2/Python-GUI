# -*- coding: utf-8 -*-
import tkinter as tk


def change_left():
    current_color = label1.cget("background")
    current_text = label1.cget("text")
    new_color = "lightblue" if current_color != "lightblue" else "red"
    new_text = "Nonavaliable" if current_text != "Nonavaliable" else "Avaliable"
    label1.config(bg=new_color)
    label1.config(text=new_text)

def change_right():
    current_color = label2.cget("background")
    current_text = label1.cget("text")
    new_color = "lightblue" if current_color != "lightblue" else "red"
    new_text = "Nonavaliable" if current_text != "Nonavaliable" else "Avaliable"
    label2.config(bg=new_color)
    label2.config(text=new_text)

def change_mid():
    current_color = label3.cget("background")
    current_text = label1.cget("text")
    new_color = "lightblue" if current_color != "lightblue" else "red"
    new_text = "Nonavaliable" if current_text != "Danger! Get in your line!" else "Avaliable"
    label3.config(bg=new_color)
    label3.config(text=new_text)

def change_top():
    current_color = label4.cget("background")
    current_text = label1.cget("text")
    new_color = "lightblue" if current_color != "lightblue" else "red"
    new_text = "Nonavaliable" if current_text != "Danger! Get in your line!" else "Avaliable"
    label4.config(bg=new_color)
    label4.config(text=new_text)


root = tk.Tk()
root.title("Renk Değiştirme Uygulaması")
root.geometry("640x400")

label1 = tk.Label(root, text="Avaliable", bg="lightblue")
label1.place(x=10, y=200)

label2 = tk.Label(root, text="right", bg="lightblue")
label2.place(x=590, y=200)

label3 = tk.Label(root, text="middle", bg="lightblue")
label3.place(x=320, y=200)

label4 = tk.Label(root, text="top", bg="lightblue")
label4.place(x=320, y=50)


button1 = tk.Button(root, text="TRIGGER1", command=change_left,  padx=30, pady=10)
button1.place(x=7000, y=300)

button2 = tk.Button(root, text="TRIGGER", command=change_right,  padx=30, pady=10)
button2.place(x=7000, y=300)

button3 = tk.Button(root, text="TRIGGER", command=change_mid,  padx=30, pady=10)
button3.place(x=7000, y=300)

button4 = tk.Button(root, text="TRIGGER", command=change_top,  padx=30, pady=10)
button4.place(x=7000, y=300)


def left(state):
    if state == True:
        button1.invoke()
    else:
        button1.invoke()

def right(state):
    if state == True:
        button2.invoke()
    else:
        button2.invoke()

def midd(state):
    if state == True:
        button3.invoke()
    else:
        button3.invoke()

def topp(state):
    if state == True:
        button4.invoke()
    else:
        button4.invoke()

root.mainloop()


