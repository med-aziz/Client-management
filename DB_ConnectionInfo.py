import mysql.connector
from tkinter import *
from win32api import GetSystemMetrics
import json
import tkinter.messagebox
import re
root = Tk()


def window(mainscreen):
    # changing application window's title:
    mainscreen.title('DataBase Info')
    # Calls all pending idle tasks, without processing any other events. 
    # This can be used to carry out geometry management and redraw widgets if necessary, without calling any callbacks.
    mainscreen.update_idletasks()
    # changing the window pop_up cordinates
    mainscreen.geometry('+0+0')
    # change program screen icon
    mainscreen.iconbitmap('PatientIcon.ico')

window(root)

class configuation():
    def __init__(self, master):
        self.dic = {}
        # Making canvas and displaying it:
        self.canvas = Canvas(master, height = GetSystemMetrics(1), width = GetSystemMetrics(0), bg = '#0069ff')
        self.canvas.pack()
        # making frame in master and diplaying it:
        self.frame = Frame(master, bg = '#ff9600')
        self.frame.place(relwidth= 0.8, relheight= 0.8, relx= 0.1, rely= 0.1)
        # Making host, user, passwd and db_name labels:
        self.host_name = Label(self.frame, text= 'Host Name: ', bg= '#ff9600', fg= 'white')
        self.host_name.config(font=('TkDefaultFont', 12))
        self.host_name.grid(row= 0, column= 0, sticky= W, pady= 10)
        self.user_name = Label(self.frame, text= 'User Name: ', bg= '#ff9600', fg= 'white')
        self.user_name.config(font =('TkDefaultFont',12))
        self.user_name.grid(row= 2, column= 0, sticky= W, pady= 10)
        self.passwd = Label(self.frame, text= 'Password', bg='#ff9600', fg= 'white')
        self.passwd.config(font=('TkDefaultFont', 12))
        self.passwd.grid(row= 4, column= 0, sticky= W, pady= 10)
        self.db_name = Label(self.frame, text= 'DataBase Name', bg= '#ff9600', fg= 'white')
        self.db_name.config(font=('TkDefaultFont',12))
        self.db_name.grid(row= 6, column= 0, sticky= W, pady= 10)
        self.host_name_field = Entry(self.frame)
        self.host_name_field.grid(row= 1, column= 0)
        self.user_name_field = Entry(self.frame)
        self.user_name_field.grid(row= 3, column= 0)
        self.passwd_field = Entry(self.frame, show= '*')
        self.passwd_field.grid(row= 5, column= 0)
        self.db_name_field = Entry(self.frame)
        self.db_name_field.grid(row= 7, column= 0) 
        self.submit_data_button = Button(self.frame, text= 'Submit Data', bg= '#ff9600', fg= 'white', width= 15, height= 2, command= self.Get_DB_info)
        self.submit_data_button.grid(row= 8, column=0, pady= 20)
        self.create_database_button = Button(self.frame, text= 'Create DataBase', bg= '#ff002e', fg= 'white', width= 15, height= 2, command= self.Create_database)
        self.create_database_button.grid(row= 9, column= 0, pady= 35)
        self.create_database_label = Label(self.frame, text= 'If Used, Wait Until Button Becomes Red again before Doing Anything Else\n !! Creating a Database Will Automatically Submit its Info', bg='#ff9600', fg='black')
        self.create_database_label.grid(row= 9, column= 1, pady= 35, sticky= W)
        self.remember_info()
    def Get_DATABASE_name(self):
        # Getting db_name from db_name field
        db_name = self.db_name_field.get()
        # Creating Pattern for the DataBase name
        pattern = re.compile(r'^[a-zA-Z]+[-a-zA-Z0-9_]+?$')
        # checking if db_name matches with pattern requirements
        # If not then show error message to user and retake input
        matches = pattern.findall(db_name)
        if len(matches) != 1:
            tkinter.messagebox.showinfo('Error', 'DATABASE Name Impossible Please Check!')
            return ""
        else:
            return db_name
    def Get_DB_info(self):
        if self.Get_DATABASE_name() == "":
            return
        self.dic['host_name'] = self.host_name_field.get()
        self.dic['user_name'] = self.user_name_field.get()
        self.dic['password']= self.passwd_field.get()
        self.dic['db_name'] = self.Get_DATABASE_name()
        with open('data.json', 'w') as j_file:
            json.dump(self.dic, j_file)
    def remember_info(self):
        try:
            f = open('data.json', 'r+')
        except FileNotFoundError:
            pass
        else:
            try:
                data = json.load(f)
                self.host_name_field.delete(0, END)
                self.user_name_field.delete(0, END)
                self.passwd_field.delete(0, END)
                self.db_name_field.delete(0, END)
                self.host_name_field.insert(0, data['host_name'])
                self.user_name_field.insert(0, data['user_name'])
                self.passwd_field.insert(0, data['password'])
                self.db_name_field.insert(0, data['db_name'])
            except KeyError:
                self.host_name_field.delete(0, END)
                self.user_name_field.delete(0, END)
                self.passwd_field.delete(0, END)
                self.db_name_field.delete(0, END)
                tkinter.messagebox.showinfo('Error',"Il y a un problème avec le fichier json du configuation\nde database, Veulliez Entrez et Submitez les information de database S'il Vous Plait")
            except TclError:
                return
    def Create_database(self):
        db_name = self.Get_DATABASE_name()
        mydb = mysql.connector.connect(
            host= self.host_name_field.get(),
            user= self.user_name_field.get(),
            passwd= self.passwd_field.get()
        )
        my_cursor = mydb.cursor()
        my_cursor.execute("CREATE DATABASE " + db_name)
        mydb = mysql.connector.connect(
            host= self.host_name_field.get(),
            user= self.user_name_field.get(),
            passwd= self.passwd_field.get(),
            database= db_name
        )
        my_cursor = mydb.cursor()
        for i in range(65, 91):
            my_cursor.execute("CREATE TABLE " + chr(i) + "_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
        self.Get_DB_info()

b = configuation(root)
root.mainloop()