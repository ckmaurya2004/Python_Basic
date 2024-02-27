from textblob import TextBlob
from tkinter import *


def correct_spelling():
    get_data = entry1.get()
    corr = TextBlob(get_data)
    data = corr.correct()

    entry2.delete(0,END)
    entry2.insert(0,data)


def main_window():
    global entry1,entry2
    win = Tk()
    win.title("Spelling Checker")
    win.geometry('500x400')
    win.config(bg='blue')
   
    win.resizable(False,False) # means window size fix not change
    label1 = Label(win,text="Incorrect Spelling",font=("Time New Roman",20,'bold'),bg='blue',fg="white")
    label1.place(x = 100,y = 20,height=50,width=300)

    entry1 = Entry(win,font=("Time New Roman",20))
    entry1.place(x = 100,y = 90,height=50,width=300)

    label2 =  Label(win,text="Correct Spelling",font=("Time New Roman",20,'bold'),bg='blue',fg="white")
    label2.place(x = 100,y = 170,height=50,width=300)

    entry2 = Entry(win,font=("Time New Roman",20))
    entry2.place(x = 100,y = 250,height=50,width=300)

    button = Button(win, text="Done",font=("Time New Roman",20),bg="red",command=correct_spelling)
    button.place(x = 180,y = 320,height=50,width=100)




    win.mainloop()

main_window()