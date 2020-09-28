words = ["Apple","Door","You","Fan","elephant","Hippopotamus","India","Acknowledgement","Boy","Girl","Laptop","Cup","Button","Almira"]
def labelslider():
    global count,sliderwords
    text = "Welcome to the typing speed increasement game"
    if (count >= len(text)):
        count = 0
        sliderwords = ""
    sliderwords += text[count]
    count += 1
    l1.config(text = sliderwords)
    l1.after(500,labelslider)
def timeless():
     global time,miss,score
     if time<11:
         l6.configure(fg="red")
     if time > 0:
         time -= 1
         l6.configure(text = time)
         l6.after(1000,timeless)# 1000 this is milisecond
     else:
         detail_label.configure(text =f"Hit = {score} | Miss = {miss} | Total score = {score-miss}" )    
         rr = messagebox.askretrycancel("Notification","For play again hit retry button")
         if (rr==True):
             score = 0
             miss = 0
             time = 30
             l2.configure(text = words[0])
             l4.configure(text = score)
             l6.configure(text = time,fg="blue")
             detail_label.configure(text ="Type word and hit Enter button")

def startgame(event):
    global score,miss
    #rr = messagebox.askretrycancel("Notification","For play again hit retry button")
    if time == 30:
        timeless()
    detail_label.configure(text = "")
    if wordentry.get() == l2['text']:
        random.shuffle(words)# it rearranges the list
        score += 1
        l4.configure(text = score)  
    else:
        miss += 1  
    random.shuffle(words)# it rearranges the list
    l2.config(text=words[0])
    #print(wordentry.get())
    wordentry.delete(0,END)
from tkinter import*
from tkinter import messagebox
import random
root = Tk()
#ROOT METHODS--------------------------------------
root.iconbitmap("E:/typing speed logo.png")#only.ico file is required but i dont have that's why i ake png
root.title("Speed Testing game")
root.geometry("800x600+280+50")#+280+50 fOR starting position in x,y
root.configure(bg="powder blue")
#VARIABLES=======================================
score = 0
time = 30
count=0
sliderwords = ""
miss = 0

#LABEL METHODS====================================================
l1 = Label(root,text = "",font=("lucida" ,"25", "italic bold"),bg="powder blue",fg="red",width=40)
l1.place(x=10,y=10)
labelslider()
random.shuffle(words)# it rearranges the list
l2 = Label(root,text = words[0],font=("lucida" ,"35", "italic bold"),bg="powder blue",width=20)
l2.place(x=100,y=220)

wordentry = Entry(root,font=("lucida" ,"20", "italic bold"),bd=10,relief=SUNKEN,justify="center")
wordentry.place(x=230,y=300)
wordentry.focus_set()
#=========================================================
l3 = Label(root,text = "Your Score:",font=("lucida" ,"20", "italic bold"),bg="powder blue",fg="black")
l3.place(x=30,y=100)

l4 = Label(root,text = score,font=("lucida" ,"20", "italic bold"),bg="powder blue",fg="black")
l4.place(x=70,y=150)

l5 = Label(root,text = "Time Remaining:",font=("lucida" ,"20", "italic bold"),bg="powder blue",fg="black")
l5.place(x=560,y=100)

l6 = Label(root,text = time ,font=("lucida" ,"20", "italic bold"),bg="powder blue",fg="black")
l6.place(x=650,y=150)

detail_label = Label(root,text = "Type word and hit Enter button" ,font=("arial" ,"28", "italic bold"),bg="powder blue",fg="dark grey")
detail_label.place(x=120,y=500)


root.bind('<Return>',startgame)
root.mainloop()
