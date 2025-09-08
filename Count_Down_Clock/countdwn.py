#  A Countdown Timer 
from tkinter import *
from playsound import playsound
import time

is_running = False
#--Configurationn

root = Tk()
root.title("Timer Clock")
root.geometry("350x400")
root.config(bg="gray10")
root.resizable(False,False)

title = Label(root, text="Timer", font='arial 25 bold',bg="#000",fg="yellow")
title.pack(pady=10)

#--Current Time

Label(root,font=("arial 16 bold"),text="Current Time:",bg="salmon").place(x=65,y=70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000,clock)

current_time = Label(root,font=("arial 15 bold"),text="",fg="#000",bg="#fff")
current_time.place(x=175,y=70)
clock()

#timer setting

hr = StringVar()
Entry(root, textvariable=hr, width=2,font="arial 40").place(x=30,y=155)
hr.set("00")

min = StringVar()
Entry(root, textvariable=min, width=2,font="arial 40").place(x=130,y=155)
min.set("00")

sec = StringVar()
Entry(root, textvariable=sec, width=2,font="arial 40").place(x=223,y=155)
sec.set("00")

Label(root,text="hours", font="arial 12", bg='black',fg='white').place(x=92,y=200)

Label(root,text="min", font="arial 12", bg='black',fg='white').place(x=190,y=200)

Label(root,text="sec", font="arial 12", bg='black',fg='white').place(x=285,y=200)

def timer():
    times = int(hr.get())*3600 + int(min.get())*60+int(sec.get())

    while times > -1:
        minute, second = (divmod(times,60))

        hour =0 
        if minute > 60:
            hour, minute = divmod(minute,60)

        sec.set(second)
        min.set(minute)
        hr.set(hour)

        root.update()
        time.sleep(1)

        if times == 0:
            
            playsound("/Users/Anas/Downloads/ring2-mp3-6551.mp3")
            sec.set("00")
            min.set("00")
            hr.set("00")
        times -= 1  



btn =Button(root,text="Start", bg="red2", bd=0,fg="red",width=20,height=2, font='arial 12',command=timer)
btn.place(x=75,y=288)




root.mainloop()