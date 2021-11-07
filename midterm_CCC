from datetime import datetime
from tkinter import *
from tkcalendar import Calendar, DateEntry
import tkinter as tk
import tkinter.ttk as ttk

top = Tk()
top.geometry('400x400')
top.title('我的日曆')
top.update_idletasks()
cal = Calendar(top, selectmode='day')
date = cal.datetime.today()
cal.calevent_create(date, '軟式運算應用', ('有作業',10,00,12,00))
cal.calevent_create(date, '咪挺', ('不要遲到！',12,11,10,10))
cal.calevent_create(date, '咪挺', ('list測試',12,11,10,10))
cal.calevent_create(date + cal.timedelta(days=-2), '拍森', ('期中考',12,11,10,10))
cal.calevent_create(date + cal.timedelta(days=3), '軟式運算應用', ('有作業',12,11,10,10))

cal.tag_config('reminder', background='red', foreground='yellow')

cal.pack(fill="both", expand=True)

date = cal.datetime.today()
cal.calevent_create(date, '軟式運算應用', ('無',12,11,10,10))



def add_window():
    add_window = Toplevel(top)
    add_window.geometry('400x300')
    add_window.title('新增事件')

    
    fm0 = Frame(add_window)
    fm0.pack(side=TOP, fill=Y, expand=YES)

    Label(fm0, text='╰（‵□′）╯新增事件╰（‵□′）╯').pack(padx=10, pady=10)

    fm1 = Frame(add_window)
    fm1.pack(side=TOP, fill=Y, expand=YES)
    
    Label(fm1, text='選擇日期：').pack(padx=5, pady=5, side=LEFT)
        
    cal2 = DateEntry(fm1, width=12, background='darkblue',foreground='white', borderwidth=2, year=2021)
    cal2.pack(padx=5, pady=5)
    
    fm2 = Frame(add_window)
    fm2.pack(side=TOP, fill=Y, expand=YES)

    Label(fm2, text='起始時間：').pack( padx=5, pady=5, side=LEFT)
    start_hour = ttk.Combobox(fm2, values=["00","01","02","03","04","05","06","07","08","09","10","11","12"
                                        ,"13","14","15","16","17","18","19","20","21","22","23"],width=2)
    start_hour.pack(padx=5, pady=5, side=LEFT)
    Label(fm2, text=':').pack( padx=2, pady=2, side=LEFT)
    start_min = ttk.Combobox(fm2, values=["00","01","02","03","04","05","06","07","08","09","10"],width=2)
    start_min.pack(padx=5, pady=5, side=LEFT)

    fm3 = Frame(add_window)
    fm3.pack(side=TOP, fill=Y, expand=YES)

    Label(fm3, text='結束時間：').pack( padx=5, pady=5, side=LEFT)
    end_hour = ttk.Combobox(fm3, values=["00","01","02","03","04","05","06","07","08","09","10","11","12"
                                        ,"13","14","15","16","17","18","19","20","21","22","23"],width=2)
    end_hour.pack(padx=5, pady=5, side=LEFT)
    Label(fm3, text=':').pack( padx=2, pady=2, side=LEFT)
    end_min = ttk.Combobox(fm3, values=["00","01","02","03","04","05","06","07","08","09","10"],width=2)
    end_min.pack(padx=5, pady=5, side=LEFT)



    def add():
        date = cal2.get_date()
        name = event_name.get()
        content = (event_content.get(),start_hour.get(),start_min.get(),end_hour.get(),end_min.get())
        cal.calevent_create(date, name, content)
        add_window.destroy()

    fm4 = Frame(add_window)
    fm4.pack(side=TOP, fill=Y, expand=YES)

    mylabel2 = Label(fm4, text='名稱：').pack(padx=5, pady=5, side=LEFT)
    event_name = Entry(fm4)
    event_name.pack(padx=5, pady=5, side=LEFT)

    fm5 = Frame(add_window)
    fm5.pack(side=TOP, fill=Y, expand=YES)

    mylabel = Label(fm5, text='內容：').pack(padx=5, pady=5, side=LEFT)
    event_content = Entry(fm5)
    event_content.pack(padx=5, pady=5, side=LEFT)

    Button(add_window, text='新增',command=add).pack(padx=10, pady=10)

def pop_window(dummy_event):
    event_list = Toplevel(top)
    event_list.geometry('400x300')
    event_list.title('當日時程')
    D=cal.selection_get()
    event_listX = cal.get_calevents(date=D)
    event_listY = []
    event_listZ = []

    for i in event_listX:
        event_listY.append((cal.calevent_cget(i,"tags")))

    for i in event_listX:
        event_listZ.append(cal.calevent_cget(i,"text"))

    Label(event_list, text='當日時程：').pack()
    for i in range(len(event_listY)):
        Label(event_list, text='{Z} ({sh}:{sm} ~ {eh}:{em}) \n備註： {Y}'.format( Y=event_listY[i][0], Z=event_listZ[i], sh=event_listY[i][1], sm=event_listY[i][2], eh=event_listY[i][3], em=event_listY[i][4])).pack(ipadx=10)

    

Button(top, text='新增事件',command=add_window).pack(padx=10, pady=10)
top.bind("<Double-Button-1>", pop_window)
top.mainloop()
