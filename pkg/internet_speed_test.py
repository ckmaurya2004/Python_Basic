from tkinter import *
import speedtest


def speed_test():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+ "Mbps"
    up = str(round(sp.upload()/(10**6),3))+ "Mbps"

    down_lab_text.config(text = down)
    up_lab_text.config(text = up)




speed = Tk()
speed.title("Internet Speed Tester")
speed.geometry('500x500')
speed.config(bg='blue')

sp_lab = Label(speed,text="Internet Speed Tester",font=("Time New Roman",20,"bold") ,bg='blue',fg="white")
sp_lab.place(x =60,y =50,height=30,width=380)

down_lab = Label(speed,text="Downloading Speed ",font=("Time New Roman",20,"bold"),bg="blue" )
down_lab.place(x =60,y =120,height=30,width=380)

down_lab_text = Label(speed,text="00 ",font=("Time New Roman",20,"bold") )
down_lab_text.place(x =100,y =180,height=50,width=300)

up_lab = Label(speed,text="Uploading Speed ",font=("Time New Roman",20,"bold"),bg="blue" )
up_lab.place(x =60,y =280,height=30,width=380)

up_lab_text = Label(speed,text="00 ",font=("Time New Roman",20,"bold") )
up_lab_text.place(x =100,y =340,height=50,width=300)

button = Button(speed,text=" Speed Test ",font=("Time New Roman",20,"bold") ,relief=RAISED,bg='red',command=speed_test)
button.place(x =150,y =440,height=50,width=200)


speed.mainloop()