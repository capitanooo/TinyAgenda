from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import datetime
import calendar
import time
import json

from bson import json_util

import  db


class App:



    def __init__(self, master):
        global v
        global tree
        global label
        global frame
        global cal


        frame = Frame(master, bd=1, relief=SUNKEN)
        frame.grid(row=0, column=0)

        logo = PhotoImage(file="oo.gif")


        ############ tree cration   ############
        tree =ttk.Treeview (frame)

        tree["columns"]=("Description","Date","Hours","Alert")

        tree.heading("Description", text="Description")
        tree.heading("Date", text="Date")
        tree.heading("Hours", text="Hours")
        tree.heading("Alert", text="Alert")



        label = Label(frame, text="fffff", width=30)
        label.pack()






        print( 'Now    :', datetime.datetime.now())
        print ('Today  :', datetime.datetime.today())
        print ('UTC Now:', datetime.datetime.utcnow())

        d = datetime.datetime.now()
        for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
            print (attr, ':', getattr(d, attr))




        ############ retrive  db ############
        b=db.nn(self)

        ############ insert_in tree ############
        for post in b:

            tree.insert("" , END , image=logo,    text=post['text'], values=(post['author'],post['tags']))


        ############ insert_in tree ############
        for index, item in enumerate(["one", "two", "three", "four"]):
            tree.insert("" , END,    text=item, values=("1A","1b"), image=logo)



        ############ insert_in tree ############
        tree.insert("", END, "dir3", text="Dir 3", image=logo)
        tree.insert("dir3", END, text=" sub dir 3",values=("3A",logo))
        tree.pack()

        ############ bottom frame  ############
        framebt = Frame(master, bd=1, relief=SUNKEN)
        framebt.grid(row=1)

        ############ bottom frame  Button ############
        w1 = Label(framebt, image=logo, text="Close")
        w1.image = logo

        w1.pack(side = LEFT)

        self.Insert = Button(framebt, text="Insert", command=self.showsinsertwindow)
        self.Insert.pack(side = LEFT)

        self.Remove = Button(framebt, text="Remove", command=self.retrive)
        self.Remove.pack(side = LEFT)

        v = StringVar()
        self.w = Label(framebt, textvariable= v)

        self.w.pack(side = LEFT)

    def lollo(self):
        global label
        label.configure(text=time.asctime())
        d = datetime.datetime.now()


        b=db.nn(self)
        print("New Event")

        for post in b:

            for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
                print (attr, ':', getattr(d, attr))

            year=getattr(d, 'year')
            month=getattr(d, 'month')
            day=getattr(d, 'day')
            hour=getattr(d, 'hour')
            minute=getattr(d, 'minute')


            if (int(post['Hours']) == int(minute)) and (int(post['Hours']) == int(minute)):
                print( ':xcxdsdssdsdsdsddddddnnnnnnnnnnnnnnnnnnnncxc')
                showinfo( "Answer", "Sorry, no answer available")



        frame.after(1000, self.lollo)



    ############ manage insertwindow ############
    def showsinsertwindow(self):
        insertwindow = Toplevel()
        insertwindow.geometry("400x300")
        insertwindow.title("insertwindow")



        handler = lambda: self.onCloseOtherFrame(insertwindow)

        fields = 'Description', 'Date', 'Hours', 'Alert'


        entries = []

        for field in fields:
          row = Frame(insertwindow)
          lab = Label(row, width=15, text=field, anchor='w')
          ent = Entry(row)

          row.pack(side=TOP, fill=X, padx=5, pady=5)
          lab.pack(side=LEFT)
          ent.pack(side=RIGHT, expand=YES, fill=X)

          entries.append((field, ent))



        # spinbox for year
        self.spin_year = Spinbox(insertwindow, from_ = -3000, to = 3000, width = 3)
        self.spin_year.pack(side = 'left', fill = X, expand = 1)
        self.spin_year.config(state = 'readonly')
        # spinbox for month
        self.spin_month = Spinbox(insertwindow,from_ = 1, to = 12,width = 3)
        self.spin_month.pack(side = 'left', fill = X, expand = 1)
        self.spin_month.config(state = 'readonly')
        # spinbox for hour
        self.spin_hour = Spinbox(insertwindow,from_ = 0, to = 23,width = 3)
        self.spin_hour.pack(side = LEFT, fill = X, expand = 1)
        self.spin_hour.config(state = 'readonly')
        # spinbox for minute
        self.spin_minute = Spinbox(insertwindow,from_ = 0, to = 59,width = 3)
        self.spin_minute.pack(side = LEFT, fill = X, expand = 1)
        self.spin_minute.config(state = 'readonly')









        month = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
        cbp3 = ttk.Labelframe(insertwindow, text='Pre-defined List')
        cb3 = ttk.Combobox(cbp3, values=month, state='readonly')
        cb3.bind('<<ComboboxSelected>>', self.showcalendar)

        cb3.current(1)  # set selection
        cb3.pack(pady=5, padx=10)
        cbp3.pack()


        global cal
        cal = StringVar()
        cal.set("New Text!")
        z = Label(insertwindow, width=15, textvariable=cal )
        
        z.pack()



        btn = Button(insertwindow, text="Close", command=lambda e=entries:  self.fetch(e))
        btn.pack()


    def showcalendar(self,month):

        global cal

        widget = month.widget           # get widget
        txt = widget.get()            # get current text
        vals = widget.current()  # get values
        print(vals)
        now = datetime.datetime.now()

        c = calendar.TextCalendar(calendar.SUNDAY).formatmonth(now.year, vals+1)
        cal.set(c)


    ############ retrive  insertwindow ############
    def fetch(self,entries):
       values = []
       for entry in entries:
          field = entry[0]
          text  = entry[1].get()
          values.append(text)
       tree.insert("", END, text="New Event",values=(values[0], values[1], values[2], values[3]), tags=('ttk', 'simple'))
       post = {"Description": values[0],"Date": values[1], "Hours": values[2],"Alert": values[3]}
       posts = db.posts
       post_id = posts.insert_one(post).inserted_id
       db.nn(self)






    def retrive(self):

        a=db.re(self)
        json.dumps(a, default=json_util.default)
        self.lollo()


        v.set(a['Hours'])

        b=db.nn(self)
        print("New Event")

        for post in b:
            print(post)

