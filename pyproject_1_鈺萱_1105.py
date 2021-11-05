# Import Required Library
from datetime import datetime
from tkinter import *
from tkcalendar import Calendar

# Create Object
org_cal = Tk()

# Add Calendar
cal = Calendar(org_cal, selectmode = 'day')
cal.pack(pady = 20)

def add_event(event_date, event_name):
    cal.calevent_create(event_date, event_name)

# Execute Tkinter
cal.mainloop()