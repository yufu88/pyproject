import pandas as pd

#open excel
#pd.read_excel(r"C:\Users\88695\Documents\pyproject\事件資料.xlsx", engine = 'openpyxl')

information = {
    "event_name", "event_content", 
    "event_start_day", "event_start_time", 
    "event_end_day", "event_end", 
    "event_last_time", "event_overlap", 
    "event_period", "event_color", 
    "event_reminder", "event_reminder_time", 
    "event_countdown"
}

df = pd.DataFrame(information)
print(df)
#df.to_excel(r"C:\Users\88695\Documents\pyproject\事件資料.xlsx", engine = 'openpyxl')