from tkinter import * 
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_text.get(1.0,END)
    textget = change(text=msg, src=s, dest=d)
    dest_text.delete(1.0,END)
    dest_text.insert(END,textget) # type: ignore


    


root = Tk() # class
root.title('Translator')
root.geometry("500x700")
root.config(bg='blue')

lab_text = Label(root,text = "Translator",font=("Time New Roman",20,"bold"))
lab_text.place(x = 100,y=40,height=30,width=300)

frame = Frame(root).pack(side=BOTTOM) # placement ke liye.


lab_text = Label(root,text = "Source Text",font=("Time New Roman",20,"bold"))
lab_text.place(x = 100,y=100,height=20,width=300)


sor_text = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor_text.place(x = 10,y=130,height=150,width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,values=list_text)
comb_sor.place(x = 10,y=300,height=40,width=100)
comb_sor.set("english")


button = Button(frame,text="Tranlate",relief=RAISED,command=data) # 3d type ka relief=RAISED
button.place(x = 120,y=300,height=40,width=100)

comb_dest = ttk.Combobox(frame,values=list_text)
comb_dest.place(x = 230,y=300,height=40,width=100)
comb_dest.set("english")

lab_text = Label(root,text = "Destination Text",font=("Time New Roman",20,"bold"))
lab_text.place(x=100,y=360,height=50,width=300)

dest_text = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_text.place(x = 10,y=420,height=150,width=480)



root.mainloop()