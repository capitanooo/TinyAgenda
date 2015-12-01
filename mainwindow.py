from tkinter import *
from tkinter import ttk
import json

from bson import json_util

import  db


class App:



    def __init__(self, master):
        global v
        global tree

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

        cities = ('Toronto', 'Ottawa', 'Montreal', 'Vancouver', 'St. John')
        cbp3 = ttk.Labelframe(insertwindow, text='Pre-defined List')
        cb3 = ttk.Combobox(cbp3, values=cities, state='readonly')
        cb3.current(1)  # set selection
        cb3.pack(pady=5, padx=10)
        cbp3.pack()

        btn = Button(insertwindow, text="Close", command=lambda e=entries:  self.fetch(e))
        btn.pack()



    ############ retrive  insertwindow ############
    def fetch(self,entries):
       values = []
       for entry in entries:
          field = entry[0]
          text  = entry[1].get()
          values.append(text)
       tree.insert("", END, text="New Event",values=(values[0], values[1], values[2], values[3]), tags=('ttk', 'simple'))






    def retrive(self):

        a=db.re(self)
        json.dumps(a, default=json_util.default)


        v.set(a['author'])

        b=db.nn(self)
        print("New Event")

        for post in b:
            print(post)

