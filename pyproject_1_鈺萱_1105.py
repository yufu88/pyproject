# Import Required Library
from datetime import datetime
from tkinter import *
from babel.dates import datetime_
from tkcalendar import Calendar
import tkinter as tk

# Create Object
org_cal = Tk()

# Add Calendar
cal = Calendar(org_cal, selectmode = 'day')
cal.pack(pady = 20)

def add_event(event_date, event_name):
    cal.calevent_create(event_date, event_name)


# date = cal.datetime(2012, 12,26)
# cal.calevent_create(date, 'Hello World', 'day')
# cal.calevent_create(datetime(2021, 11,5), 'birth','day')
#id = cal.get_calevents(tag='day')
#day = cal.get_calevents(tag='day')
# #dddd = cal.calevent_cget(1, 'date')
# print(day)
# print(dddd)

# add_event(2021,11,26,'dieeeee')
# add_event(2021,11,8,'tryyyyyy')
# day = cal.get_calevents()
# dddd = cal.calevent_cget(day[0], 'text')
# print(dddd)

# Execute Tkinter
cal.mainloop()