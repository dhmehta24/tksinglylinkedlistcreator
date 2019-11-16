__author__ = 'Divyesh Mehta'
__version__ = '1.2'

# Python Version 3.7.4

from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

root = Tk()
root.resizable(False,True)
root.maxsize(1366,720)
root.geometry("1220x680+10+10")
root.title("Singly Linked List Creation System")

root.configure(bg = "#FF7F50")
labelfont = ('times',32,'bold')
creditfont = ('comic sans',12,'bold')

title = Label(root,text = "Singly Linked List Creator",justify = CENTER,bg = "#FF7F50",fg = "maroon",relief = FLAT)
title.place(x = 340,y = 15) 
title.config(font = labelfont)

credit = Label(root,text = "Made By:-  ig@dhmehta24 ",justify = CENTER,font = creditfont,bg = "#FF7F50",relief = FLAT)
credit.place(x = 850,y=40)

label = Label(root,text = "Enter the Data That You  Want To Enter In The Node :",relief = FLAT,bg = "white smoke")
label.place(x=50,y=100)

limlabel = Label(root,text = "Enter the limit of Nodes:",relief = FLAT,bg = "white smoke")
limlabel.place(x=700,y=100)

dataentry = StringVar()
eb = Entry(root,textvariable=dataentry,width = 30,bg = "light green")
eb.place(x=350,y=100)
eb.focus()

limit = IntVar()
lim = Entry(root,textvariable=limit,width = 30,bg = "light green")
lim.place(x = 850,y = 100)

w = Canvas(root,width = 1180,height = 420,bd = 4,relief = SUNKEN,bg = "#EEE8AA")
w.pack(padx=10,pady=10)
w.place(x = 10,y = 200)

f = 1180
hbar = Scrollbar(root,orient=HORIZONTAL)
hbar.config(command=w.xview)
w.config(xscrollcommand = hbar.set)

w.create_rectangle(50,160,150,220,fill = "sky blue")
w.create_line(100,160,100,220)
null = w.create_text(75,190,text = "NULL")
w.create_text(125,190,text = "*start")
sts = 0
rts = 1
flag = 0
r = 75
j = 75
d = 0
h = 1
counter = 1
counterlim = limit.get()
node = []

def process():
    btn2.configure(state=NORMAL)
    btn4.configure(state=NORMAL)
    btn5.configure(state = NORMAL)
    global sts,rts,counter,counterlim,node,d,h
    #check limit
    if limit.get()==0:
        mb.showerror('Limit Error','Set The Limit First')
        sts = 0
        return
    #check node is empty or not
    elif dataentry.get()=="":
        mb.showerror('Error','A Node Must NOT have to be EMPTY  !!!!')
        sts = 0
        btn2.configure(state=DISABLED)
    else:
        global r,i,h
        ele = str(dataentry.get())
        node.append(ele)
        w.delete(null)
        if (flag!=0):
            global k
            r = r + 150
            taga = ("node" + str(i))
            k = w.create_text(r,190,text=dataentry.get(),tag = "data" + str(i))
        else:
            w.create_text(75,190,text = dataentry.get(),tag = "firstl")
        rts = 0
        d = 0
        add.configure(state=DISABLED)
        eb.configure(state = DISABLED)

        
def entop(event):
    global sts
    if sts!=0:
        return
    sts = 1
    process()

eb.bind('<Return>',entop)
axe = 50
why = 150
zed = 100
valk = 200
wiz = 150
s = 125
i = v = 1
def addnode():
    global sts,rts,d
    #check limit
    if limit.get()==0:
        mb.showerror('Limit Error','Set The Limit First')
        btn2.configure(state = DISABLED)
        d = 1 
        rts = 1
        sts = 0
        return
    else:
        add.configure(state=NORMAL)
        btn5.configure(state = NORMAL)
        eb.configure(state = NORMAL)
        sts = 0
        rts = 1
        d = 1 
        #check Data Entry bar is empty or not
        if dataentry.get()=="":
            mb.showerror('Error','A Node Must NOT have to be EMPTY  !!!!')
        else:
            global flag,counter,node
            counter = counter + 1
            counterlim = limit.get()
            #check max limit
            if counter > counterlim:
                mb.showerror('Node Limit Reached','The Maximum No of Nodes Has Been Created')
                add.configure(state=DISABLED)
                btn2.configure(state=DISABLED)
                eb.configure(state = DISABLED)
                counter = counterlim
                d = 0
            else:
                flag = flag + 1
                global s,j,null,v,i,h
                global axe
                axe = axe + 150
                why = axe + 100
                zed = axe + 50
                wiz = why-150
                valk = axe - 5
                s = s + 150
                j = j + 150
                q = s - 150
                v = v + 1
                h = axe + 25
                i = i + 1
                taga = ("node" + str(i))
                w.create_rectangle(axe,160,why,220,fill = "sky blue",tag = taga)
                w.create_line(zed,160,zed,220,tag = taga)
                w.create_line(wiz,190,axe,190,tag = taga)
                w.create_line(axe,190,valk,195,tag = taga)
                w.create_line(axe,190,valk,185,tag = taga)
                null = w.create_text(j,190,text="NULL")
                temp = w.create_text(s,190,text="*temp",tag = "endf")
                if counter>2:
                    ptr = w.create_text(q,190,text="*ptr",tag = "pointer" + str(i))
                    w.delete("endf")
                    w.delete("end")
                    if counter == counterlim:
                        end = w.create_text(s,190,text="*end",tag = "end")
                    else:
                        temp = w.create_text(s,190,text="*temp",tag = "endf")
                #auto scroll
                if why>=1130:
                    global f
                    f = f + 150
                    hbar.pack(side=BOTTOM,fill=X)
                    w.config(scrollregion=[0,0,f,f])
                    w.xview('scroll',3,'units')
                eb.delete(0,END)
    btn2.configure(state=DISABLED)


def entup(event):
    global rts
    if rts!=0:
        return
    rts = 1
    addnode()
    
eb.bind('<Shift_L>',entup)


def reset():
    global sts,rts,j,null,counter,d
    d = 0
    sts = 0
    rts = 1
    j = 75
    counter = 1
    btn2.configure(state=DISABLED)
    add.configure(state=NORMAL)
    global axe,flag,s,r,f,v,i
    axe = 50
    s = 125
    flag = 0
    r = 75
    f = 1180
    i = v = 1
    h = 0 
    w.delete("all")
    w.create_rectangle(50,160,150,220,fill="sky blue")
    w.create_line(100,160,100,220)
    w.create_text(125,190,text = "*start")
    null = w.create_text(75,190,text = "NULL")
    w.config(scrollregion= [0,0,1,1])
    limit.set(0)
    btn4.configure(state = DISABLED)
    btn5.configure(state = NORMAL)
    eb.configure(state = NORMAL)
    eb.delete(0,END)
    return


def deleten():
    global i,counter,axe,why,j,s,r,f,rts,sts,d
    counterlim = limit.get()
    w.delete("node" + str(i))
    w.delete("data" + str(i))
    w.delete("endf")
    if counter == 1:
        w.delete("firstl")
        reset()
        limit.set(counterlim)
        btn5.configure(state = DISABLED)
    else:
        add.configure(state = DISABLED)
        btn2.configure(state = NORMAL)
        if counter == counterlim:
            w.delete("end")
        w.delete(null)
        counter = counter + 1
        if i < counter:
            w.delete("pointer" + str(i+1))
        i = i - 1
        counter = counter - 2
        if d==1:
            r = r + 150
        axe = axe - 150
        j = j - 150
        r = r - 150
        s = s - 150
        f = f - 150
        w.config(scrollregion = [0,0,f,f])
        dataentry.set("*")
        d = 0
        rts = 0
        sts = 1


def entpos():
    msg = mb.askyesno("Warning!!!","This Function is still under development,Do you want to continue ???")
    if msg == True:
        global axe,r,i,node,counter,null,h
        counterlim = limit.get()
        if counter == counterlim:
            counterlim = counterlim + 1
            limit.set(counterlim)
        ask = sd.askinteger('Data Insertion Prompt Wizard','Enter The Position: ',parent = root)
        if ask > counter:
            mb.showerror('Invalid Input','No Node Found At Given Position')
            counterlim = counterlim - 1
            limit.set(counterlim)
        else :
            addnode()
            h = 0 
            t = (ask * 150) - 100
            x = counter - 1
            u = (x - ask)*150
            v = (counter - ask)*150
            r = r - u
            n = (counter * 150) - 75
            for m in range (int(x),int(ask-1),-1):
                w.delete("data" + str(m))
                w.delete(null)
                if ask ==1:
                    w.delete("firstl")
            for m in range (ask,counter,1):
                dataentry.set(str(node[m-1]))
                process()
            r = (r - u) - 150
            null = w.create_text(r,190,text = "NULL")
            eb.configure(state = NORMAL)
            add.configure(state = NORMAL)
            btn2.configure(state = DISABLED)
            i = ask
            r = r - 150
            node.clear()
    else:
        return
    

add = Button(root,text = "Add Data Into Node",command=lambda:process(),width=20,relief = RAISED)
add.place(x=60,y=150)

btn2 = Button(root,text = "Add New Node From Last",state = DISABLED,command = lambda:addnode(),width=20,relief = RAISED)
btn2.place(x=230,y=150)

btn3 = Button(root,text = "Clear Entry",command = lambda:eb.delete(0,END),width=20,relief = RAISED)
btn3.place(x=570,y=150)

btn4 = Button(root,text = "Reset Progress",command = lambda:reset(),width=20,relief = RAISED)
btn4.place(x=740,y=150)

btn5 = Button(root,text = "Delete Node From Last",command = lambda:deleten(),width=20,relief = RAISED)
btn5.place(x=910,y=150)

btn6 = Button(root,text = "Add Node At Poisition",command = lambda:entpos(),width = 20,relief = RAISED)
btn6.place(x=400,y=150)

root.mainloop()
