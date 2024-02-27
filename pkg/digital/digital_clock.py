from tkinter import *
from datetime import datetime


def date_time():
    time = datetime.now()
    hr = time.strftime('%I') # give hour as 24 time
    minute = time.strftime('%M') # give minute 
    sec = time.strftime('%S') # give second as seconds
    am = time.strftime('%p') # give am/pm

    date = time.strftime("%d") # give date
    month = time.strftime('%m') # give month
    year = time.strftime('%y') # give year
    day = time.strftime('%a') # give day

    lab_hr.config(text=hr)
    lab_min.config(text=minute)
    lab_sec.config(text=sec)
    lab_am.config(text=am)

    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    
    lab_hr.after(200,date_time) #  after() data ko change means recolling  krta h yha pr data miliseconds me jata h jaise 200






clock = Tk()
clock.title("Digital Clock")
clock.geometry("1000x500")
clock.config(bg="blue")


# ******** time **********

lab_hr = Label(clock,text='00',font=('Time New Roman',50,'bold'),bg="red",fg="white")
lab_hr.place(x=120,y=50,height=110,width =100 )

lab_hr_text = Label(clock,text='Hour',font=('Time New Roman',20,'bold'),bg="red",fg="white")
lab_hr_text.place(x = 120,y=190,height=40,width=100)


lab_min = Label(clock,text='00',font=('Time New Roman',50,'bold'),bg="red",fg="white")
lab_min.place(x=340,y=50,height=110,width =100 )

lab_min_text = Label(clock,text='Min',font=('Time New Roman',20,'bold'),bg="red",fg="white")
lab_min_text.place(x=340,y=190,height=40,width =100 )

lab_sec = Label(clock,text='00',font=('Time New Roman',50,'bold'),bg="red",fg="white")
lab_sec.place(x=560,y=45,height=110,width =100 )

lab_sec_text = Label(clock,text='sec',font=('Time New Roman',20,'bold'),bg="red",fg="white")
lab_sec_text.place(x=560,y=185,height=40,width =100 )

lab_am = Label(clock,text='00',font=('Time New Roman',30,'bold'),bg="red",fg="white")
lab_am.place(x=780,y=50,height=110,width =100 )

lab_am_text = Label(clock,text='Am/PM',font=('Time New Roman',15,'bold'),bg="red",fg="white")
lab_am_text.place(x=780,y=190,height=40,width =100 )

#  ************date*************

lab_date = Label(clock,text='00',font=('Time New Roman',50,'bold'),bg="red",fg="white")
lab_date.place(x=120,y=260,height=110,width =100 )

lab_date_text = Label(clock,text='Date',font=('Time New Roman',20,'bold'),bg="red",fg="white")
lab_date_text.place(x = 120,y=390,height=40,width=100)


lab_month = Label(clock,text='00',font=('Time New Roman',50,'bold'),bg="red",fg="white")
lab_month.place(x=340,y=260,height=110,width =100 )

lab_month_text = Label(clock,text='Month',font=('Time New Roman',20,'bold'),bg="red",fg="white")
lab_month_text.place(x=340,y=390,height=40,width =100 )

lab_year = Label(clock,text='00',font=('Time New Roman',50,'bold'),bg="red",fg="white")
lab_year.place(x=560,y=255,height=110,width =100 )

lab_year_text = Label(clock,text='Year',font=('Time New Roman',20,'bold'),bg="red",fg="white")
lab_year_text.place(x=560,y=385,height=40,width =100 )

lab_day = Label(clock,text='00',font=('Time New Roman',30,'bold'),bg="red",fg="white")
lab_day.place(x=780,y=255,height=110,width =100 )

lab_day_text = Label(clock,text='Day',font=('Time New Roman',15,'bold'),bg="red",fg="white")
lab_day_text.place(x=780,y=390,height=40,width =100 )





date_time()


clock.mainloop()
