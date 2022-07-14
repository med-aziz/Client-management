import mysql.connector
from tkinter import *
from tkinter import filedialog, Text
import re
import tkinter.messagebox
import json
from win32api import GetSystemMetrics

#Making APP SCREEN
root = Tk()

def window(mainscreen): 
    # Changing Apllication's Window Title
    mainscreen.title('Gestion Des Patientes')
    # Calls all pending idle tasks, without processing any other events. 
    # This can be used to carry out geometry management and redraw widgets if necessary, without calling any callbacks.
    mainscreen.update_idletasks()
    #width = mainscreen.winfo_width() # this returns what width does the app NEED to display everything
    #height = mainscreen.winfo_height() # this returns what height does the app NEED to display everything
    '''
    width = 600
    height = 600
    x = (mainscreen.winfo_screenwidth() // 2) - (width // 2)
    y = (mainscreen.winfo_screenheight() // 2) - (height // 2)
    mainscreen.geometry('{}x{}+{}+{}'.format(width,height,x,y))
    '''
    # Changing Screen Pop Up Cordinates
    mainscreen.geometry('+0+0')
    # Changing Program's Screen Icon
    mainscreen.iconbitmap('PatientIcon.ico')

window(root)

with open('data.json', 'r+') as f:
    data = json.load(f)
try:
    mydb = mysql.connector.connect(
        host = data['host_name'],
        user = data['user_name'],
        passwd = data['password'],
        database = data['db_name']
    )
except mysql.connector.errors.ProgrammingError:
    tkinter.messagebox.showinfo('erreur', 'Information de DataBase incorrecte\n Veulliez Ouvir le programme de configuration de databsae et vérifier les information du serveur SQL')
    quit()
except mysql.connector.errors.InterfaceError:
    tkinter.messagebox.showinfo('Error','Error Connecting To Server, Check if the SQL server is Running Otherwise Restart it, and give it a minute')
    quit()

#print(mydb)


my_cursor = mydb.cursor()


#my_cursor.execute("CREATE DATABASE clientdb")

"""
datatables = []
emtystring = "yes"
my_cursor.execute("SHOW TABLES")
for table_name in my_cursor:
    datatables.append(table_name[0])
for some_table in datatables:
    my_cursor.execute("DELETE FROM " + some_table + " WHERE Nom_et_Prénom = 'MARIEM KEFI'")
    mydb.commit()

"""

"""
my_cursor.execute("CREATE TABLE A_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE B_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE C_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE D_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE E_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE F_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE G_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE H_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE I_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE J_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE K_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE L_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE M_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE N_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE O_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE P_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE Q_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE R_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE S_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE T_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE U_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE V_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE W_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE X_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE Y_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
my_cursor.execute("CREATE TABLE Z_patients (Nom_et_Prénom VARCHAR(25), Nom_Du_Mari VARCHAR(20), Date_De_Naissance DATE, Patient_id INTEGER PRIMARY KEY)")
"""

class app_buttons():
    def __init__(self, master):
        self.datatables = []
        self.clicked = StringVar()
        # This is the list i'll store the current client chosen name possible id's so that i can
        # change info of client when pressed the button change info, and find patient info
        # when press find_info 
        # filling datatables list with names of all the tables in the current database with alphabetical order
        my_cursor.execute("SHOW TABLES")
        for table_name in my_cursor:
            self.datatables.append(table_name[0])


        # Making canvas in master and displaying it
        self.canvas = Canvas(master, height= GetSystemMetrics(1), width= GetSystemMetrics(0), bg='#263442')
        self.canvas.pack()
        # Making frame in master and displaying it
        self.frame = Frame(master, bg='#266666')
        self.frame.place(relwidth=0.8,relheight=0.8, relx=0.1, rely=0.1)
        # Making Add patient Button and displaying it
        self.Add_patient_button = Button(self.frame, text='Ajouter Une Patiente',bg='#263442', fg='white', command= self.add_patient)
        self.Add_patient_button.grid(row=5, column=1,padx=5,pady=5)
        # Making Delete patient Button and displaying it
        self.Delete_patient_button = Button(self.frame, text='Supprimer Cette Patiente',bg='#263442', fg='white', command= self.delete_patient)
        self.Delete_patient_button.grid(row=6, column=1, padx=5, pady=5)
        # Making find patient 'Nombre de fiche' Button and displaying it
        self.find_patient_Number_id = Button(self.frame, text='Trouver le Nombre de fiche du Patiente',bg='#291885', fg='white', command=self.find_client_id)
        self.find_patient_Number_id.grid(row=7, column=1, padx=5, pady=5)
        # Making Find Patient Button and displaying it
        self.find_patient_name = Button(self.frame, text='Trouver Une Patiente',bg='#263442', fg='white', command= self.find_patients)
        self.find_patient_name.grid(row=1, column=4, pady=5)
        # Making Choose Patient Button And displaying it
        self.choose_patient_name = Button(self.frame, text='Choisir Cette Patiente',bg='#263442', fg='white', command= self.choose_patient)
        self.choose_patient_name.grid(row=1, column=3, padx=50, pady=5)
        '''
        # Making Look for Patient Husband Button and displaying it
        self.find_patient_husband_button = Button(self.frame, text='Trouver époux',bg='#263442', fg='white', command=self.Look_For_patients_husband_name)
        self.find_patient_husband_button.grid(row=2, column=4, padx=50, pady=5)
        '''
        '''
        # Making Choose Husband Button and displaying it
        self.find_patient_husband_button = Button(self.frame, text='Choisir époux',bg='#263442', fg='white', command=self.Choose_husband)
        self.find_patient_husband_button.grid(row=2, column=3, padx=50, pady=5)
        '''


        # Making Nom of the husband Label / setting it up and displaying it!!!!!!!!!!!!!!
        self.Patient_husbands_surname= Label(self.frame, text="Nom de famille d'époux :", bg='#266666',fg='white')
        self.Patient_husbands_surname.config(font=('TkDefaultFont', 10))
        self.Patient_husbands_surname.grid(row=2, column=0, sticky=E, pady=10)
        # Making patient surname label  / Setting it up and displaying it
        self.Patient_surname= Label(self.frame, text='Nom de famille de Patiente :', bg='#266666',fg='white')
        self.Patient_surname.config(font=('TkDefaultFont', 10))
        self.Patient_surname.grid(row=0, column=0, sticky=E, pady=10)
        # Making patient forename label / setting it up and displaying it
        self.Patient_forename= Label(self.frame, text='Prénom de Patiente :', bg='#266666',fg='white')
        self.Patient_forename.config(font=('TkDefaultFont', 10))
        self.Patient_forename.grid(row=1, column=0, sticky=E, pady=10)
        # Making Patient Birthday Label  / Setting it up and displaying it
        self.Patient_Birthdate = Label(self.frame, text='Date de Naissance de Patiente :', bg='#266666',fg='white')
        self.Patient_Birthdate.config(font=('TkDefaultFont', 10))
        self.Patient_Birthdate.grid(row=3,column=0, sticky=E, pady=10)
        # Making Patient ('Nombre de fiche') Label  / Setting it up and displaying it
        self.Patient_number_id = Label(self.frame,text='Nombre de Fiche de Patiente :', bg='#266666',fg='white')
        self.Patient_number_id.config(font=('TkDefaultFont', 10))
        self.Patient_number_id.grid(row=4, column=0, sticky=E, pady=10)
        # Making Patient Name field  / Setting it up and displaying it
        self.Patient_surname_field = Entry(self.frame)
        self.Patient_surname_field.grid(row=0, column=1, pady=10)
        # Making Patient Name field  / Setting it up and displaying it
        self.Patient_forename_field = Entry(self.frame)
        self.Patient_forename_field.grid(row=1, column=1, pady=10)
        # Making Patient's husband full name:!!!!!!!!!!!
        self.Patient_husbands_surname_field = Entry(self.frame)
        self.Patient_husbands_surname_field.grid(row=2, column=1, pady=10)
        # Making Patient Birthday field / Setting it up and displaying it
        self.Patient_birthday_field = Entry(self.frame)
        self.Patient_birthday_field.grid(row=3, column=1, pady=10)
        # Making Patient Nombre de fiche field  / Setting it up and displaying it
        self.Patient_number_id_field = Entry(self.frame)
        self.Patient_number_id_field.grid(row=4, column=1, pady=10)
        # Making Get Patient info Label / setting it up and displaying it
        self.get_patient_info_Label = Label(self.frame,text='Information De Patiente :', bg='#266666',fg='white')
        self.get_patient_info_Label.config(font=('TkDefaultFont', 10))
        self.get_patient_info_Label.grid(row=8, column=0, pady=10)
        # Making Get Patient Info Button / setting it up and displaying it
        self.get_patient_info_Button = Button(self.frame, text='Trouver Information de Patiente',bg='#263442', fg='white', command= self.find_info)
        self.get_patient_info_Button.grid(row=8, column=1, padx=50, pady=5)
        # Making Change Patient info Button / setting it up and displaying it
        self.Change_patient_info_Button = Button(self.frame, text='Autre Patiente',bg='#263442', fg='white', command= self.change_info)
        self.Change_patient_info_Button.grid(row=8, column=2, padx=50, pady=5)
        
        # Make the initial drop Menuw with patient names in the already chosen file in Data 
        # Check if possible to make this self.drop existance and condition better
        self.drop = Label(self.frame)
    
    
    # Def Get_name allow us to take a surename from the patient sureName field with Checking user input and returning error message 
    # if input is impossible else returning the surename
    def Get_surname(self):
        #Making the name pattern to follow
        #--- Need more testing and improvement
        pattern = re.compile(r'^[^\d\s._+*/@=-]+[^\d\s._+*/@=-]+[ ]?[^\d\s._+*/@=-]+?$')    
        #checking if name input matches the format of the pattern specified
        #if not, show error message and retake name input
        #Getting the name input
        name = self.Patient_surname_field.get()
        matches = pattern.findall(name)
        if(len(matches) != 1):
            tkinter.messagebox.showinfo('Error','Nom De Famille De Patient Impossible, Veulliez Vérifier Svp!')
        else:
            return name


    # Def Get_name allow us to take a forename from the patient ForeName field with Checking user input and returning error message 
    # if input is impossible else returning the forename
    def Get_forename(self):
        #Making the name pattern to follow
        #--- Need more testing and improvement
        pattern = re.compile(r'^[^\d\s._+*/@=-]+[^\d\s._+*/@=-]+[ ]?[^\d\s._+*/@=-]+?$')
        #checking if name input matches the format of the pattern specified
        #if not, show error message and retake name input
        #Getting the name input
        name = self.Patient_forename_field.get()
        matches = pattern.findall(name)
        if(len(matches) != 1):
            tkinter.messagebox.showinfo('Error','Prénom De Patient Impossible, Veulliez Vérifier Svp!')
        else:
            return name
    
    
    # Def Get_Husbands_name allows us to take a name from the patient Name field with Checking user input and returning error message 
    # if input is impossible else returning the name
    def Get_Husbands_surname(self):
        #Making the name pattern to follow
        #--- Need more testing and improvement
        pattern = re.compile(r'(^[^\d\s._+*/@=-]+[ ]?[^\d\s._+*/@=-]+[ ]?[^\d\s._+*/@=-]+?$|^$)')
        #checking if name input matches the format of the pattern specified
        #if not, show error message and retake name input
        #Getting the name input
        husbands_name = self.Patient_husbands_surname_field.get()
        matches = pattern.findall(husbands_name)
        if(len(matches) != 1):
            tkinter.messagebox.showinfo('Error',"Nom D'époux de patiente est impossible!, Veulliez Vérifier Svp!")
        else:
            if husbands_name == "" :
                return "Non Mariée"
            return husbands_name
    

    # Def Get_Birth_date allows us to take a name from the patient Name field with Checking user input and returning error message 
    # if input is impossible else returning the name
    def Get_Birth_date(self):
        #Making the birth date Pattern to follow 
        # --- Need to make it so program gets date of the calendar and now allow the year given to surpass the current year in calendar
        #(could do the same thing by getting data from web api somehow) (Check current year)
        pattern  = re.compile(r'^(19|20)\d\d/(0[1-9]|[1][012])/(0[1-9]|[12][0-9]|3[01])$')
        #checking if birth date format matches the pattern specified
        #if not take a new Birth date input
        # Getting birth date input
        Birth_date = self.Patient_birthday_field.get()
        matches = pattern.findall(Birth_date)
        if(len(matches) != 1):
            tkinter.messagebox.showinfo('Error','Date de Naissance de Patient Non Valide, Veulliez Vérifier Svp!')
            return ""
        else:
            return Birth_date
    
    
    # Def Get_Patient_Number_id allows us to take a name from the patient Name field with Checking user input and returning error message 
    # if input is impossible else returning the name
    def Get_Patient_Number_id(self):
        #Making Pattern for Patient Number id
        pattern = re.compile(r'^\d+$')
        #checking if Client Number id format matches the pattern specified
        #if not take a new Client Number id input
        # Getting Client Number id input
        patient_Number_id = self.Patient_number_id_field.get()
        matches = pattern.findall(patient_Number_id)
        if len(matches) != 1 :
            tkinter.messagebox.showinfo('Error','Nombre De Fiche De Patient Non Valide, Veulliez Vérifié Svp!')
            return ""
        else:
            return patient_Number_id


    # Function that groups the client surname and forename together in the order (forename + surname)
    def Client_full_name(self):
        try:
            c_fullname = self.Get_forename() + " " + self.Get_surname()
        except TypeError:
            return
        return c_fullname



    # Function that inserts certain patient row in a table of the DATABASE depending on the first
    # letter of the forename
    def add_patient(self):
        try:
            patient_name = self.Client_full_name().upper()
            husband_name = self.Get_Husbands_surname().upper()
        except AttributeError:
            return
        birthday = self.Get_Birth_date()
        client_id = self.Get_Patient_Number_id()
        if birthday == "" or client_id == "":
            return
        # ---Get Name of the table as string from datatables list depending on the first letter
        # of the client forename 
        table = self.datatables[ord(patient_name[0])-65]
        # Make the sql Command to add the client info to the table selected above
        # transform the client id to int because it is string when taken from the field
        # and because i specified that the client id is an int in the DATABASE
        Line = "INSERT INTO" + " " + table + "(Nom_et_Prénom, Nom_Du_Mari, Date_De_Naissance, Patient_id) VALUES (%s,%s,%s,%s)"
        record1 = (patient_name, husband_name, birthday, int(client_id),)
        my_cursor.execute(Line, record1)
        # commit the changes to the database
        mydb.commit()
        # Look for rows in Database with the full information of the client you just entered
        Line = "SELECT * FROM" + " " + table + " WHERE (Nom_et_Prénom = %s) AND (Nom_Du_Mari = %s) AND (Date_De_Naissance = %s) AND (Patient_id = %s)"
        my_cursor.execute(Line, record1)
        # compare client_id of the row selected 
        for row in my_cursor:
            if row[3] == int(client_id):
                tkinter.messagebox.showinfo('Fait', 'Patiente Ajoutée !')
                break
    def delete_patient(self):
        Validation = tkinter.messagebox.askquestion('Validation de Supprimer','Voulez Vous Vraiment Supprimer Ce Patient De la Liste?')
        if Validation == 'yes':   
            try: 
                patient_name = self.Client_full_name().upper()
                husband_name = self.Get_Husbands_surname().upper()
            except AttributeError:
                return
            birthday = self.Get_Birth_date()
            client_id = self.Get_Patient_Number_id()
            if birthday == "" or client_id == "":
                return
            # ---Get Name of the table as string from datatables list depending on the first letter
            # of the client forename 
            table = self.datatables[ord(patient_name[0])-65]
            # Getting the number of rows that are currently in the table and putting it
            # in number_rows_before
            my_cursor.execute("SELECT COUNT(*) FROM " + table)
            for thing in my_cursor:
                number_rows_before = thing[0]
            # Deleting the patient using patient's info
            record1 = (patient_name, husband_name, birthday, int(client_id),)
            Line = "DELETE FROM " + table + " WHERE (Nom_et_Prénom = %s) AND (Nom_Du_Mari = %s) AND (Date_De_Naissance = %s) AND (Patient_id = %s)"
            my_cursor.execute(Line, record1)
            mydb.commit()
            # Getting the number of rows that are in the table after clicking delete the patient
            # and putting the number in number_rows_after
            my_cursor.execute("SELECT COUNT(*) FROM " + table)
            for thing1 in my_cursor:
                number_rows_after = thing1[0]
            # Showing a message to the user depending on if the client was deleted or not
            if number_rows_after < number_rows_before : 
                tkinter.messagebox.showinfo('Fait', 'Patiente a été supprimer!')
            else:
                tkinter.messagebox.showinfo('Error', 'Patiente Non Trouvé!')
        else:
            pass
    def find_client_id(self):
        try:
            patient_name = self.Client_full_name().upper()
            husband_name = self.Get_Husbands_surname().upper()
        except AttributeError:
            return
        birthday = self.Get_Birth_date()
        if birthday == "":
            return
        patient_id_possibilites = ""
        # ---Get Name of the table as string from datatables list depending on the first letter
        # of the client forename 
        table = self.datatables[ord(patient_name[0])-65]
        # Check if there is a patient in the table with the patient info given to you
        # if found at least 1 then continue otherwise tell user there is no such patient
        Line = "SELECT COUNT(*) FROM " + table +  " WHERE (Nom_et_Prénom = %s) AND (Nom_Du_Mari = %s) AND (Date_De_Naissance = %s)"
        record1 = (patient_name, husband_name, birthday,)
        my_cursor.execute(Line, record1)
        for thing0 in my_cursor:
            if thing0[0] == 0:
                tkinter.messagebox.showinfo('Error','Patiente Non Trouvé! Veuillez Valider Vos Données!')
            else:
                done_once = FALSE
                # Getting the client number id based on the client info
                Line = "SELECT Patient_id FROM " + table + " WHERE (Nom_et_Prénom = %s) AND (Nom_Du_Mari = %s) AND (Date_De_Naissance = %s)"
                my_cursor.execute(Line, record1)
                # Checking if there are multiple clients with the same info except id or Not
                # And giving user all possible info for client's info given
                for thing in my_cursor:
                    if done_once == FALSE:
                        patient_id_possibilites = patient_id_possibilites + str(thing[0])
                        done_once = TRUE
                    else:
                        patient_id_possibilites = patient_id_possibilites + ", " + str(thing[0])
                if patient_id_possibilites.count(',') == 0:
                    tkinter.messagebox.showinfo('Nombre De fiche de Patiente',f'1 Patiente trouvée\nNombre de fiche de Patiente = {patient_id_possibilites}')
                else:
                    tkinter.messagebox.showinfo('Nombre De fiche de Patiente',f'{patient_id_possibilites.count(",") + 1} Patientes trouvées \nNombres des fiches des Patientes = {patient_id_possibilites}')
    def find_patients(self):
        try:
            Patient_surname = self.Get_surname().upper()
            Patient_forename = self.Get_forename().upper()
        except AttributeError:
            return
        patient_found_list = []
        # ---Get Name of the table as string from datatables list depending on the first letter
        # of the client forename if forename field is not empty
        table = self.datatables[ord(Patient_forename[0])-65]
        # Fiding possible Client names using Like Operator In sql
        Line = "SELECT Nom_et_Prénom FROM " + table + " WHERE (Nom_et_Prénom LIKE %s) AND (Nom_et_Prénom LIKE %s) "
        record1 = ('%'+Patient_forename+'%', '%'+Patient_surname+'%',)
        my_cursor.execute(Line, record1)
        # making the list of possible patient names
        for patient in my_cursor:
            patient_found_list.append(patient[0])
        # putting all possible patient names in the dorp menu
        self.drop.destroy()
        self.clicked.set("NULL")
        self.drop = OptionMenu(self.frame, self.clicked, *patient_found_list)
        self.drop.config( bg='#266666',fg='white') 
        self.drop.grid(row=1, column=2)
    def choose_patient(self):
        # get the info from the dorp menu and put it in the fields if choose patient button
        # pressed and reset the drop menu to null after
        if self.clicked.get() != "Null":
            self.Patient_surname_field.delete(0, END)
            self.Patient_forename_field.delete(0, END)
            self.Patient_surname_field.insert(0, self.clicked.get().split(" ")[1])
            self.Patient_forename_field.insert(0, self.clicked.get().split(" ")[0])
            self.clicked.set("Null")
    # Function that returns the client possible info using the name of the client given in the
    # gui field
    def list_possible_client_info(self):
        try:
            patient_name = self.Client_full_name().upper()
        except AttributeError:
            return
        # List of all possible clients info with the given name
        info_possible = []
        # ---Get Name of the table as string from datatables list depending on the first letter
        # of the client forename if forename field is not empty
        table = self.datatables[ord(patient_name[0])-65]
        record1 = (patient_name, )
        Line = "SELECT Nom_Du_Mari, Date_De_Naissance FROM " + table + " WHERE Nom_et_Prénom = %s"
        my_cursor.execute(Line, record1)
        # Putting all info possibilities in the list
        for thing0 in my_cursor:
            info_possible.append(thing0)
        return info_possible
    # Function that puts the patient's info in the GUI in the fileds depending on the name
    # Given in the name fields
    def find_info(self):
        info_possible = self.list_possible_client_info()
        # Checking if there is at least one patient with the name given in the name fields
        # if so then show the first patient info on gui
        if len(info_possible) > 0: 
            # Getting the first possible client info to show up in the GUI Fields
            self.Patient_husbands_surname_field.delete(0, END)
            self.Patient_husbands_surname_field.insert(0, info_possible[0][0].lower())
            self.Patient_birthday_field.delete(0, END)
            self.Patient_birthday_field.insert(0, str(info_possible[0][1]).replace('-','/'))
        # otherwise there is no patient with the given name in the fields
        # then show error message "client not found"
        else:
            tkinter.messagebox.showinfo('Erreur! Patiente non trouvée',f"Veulliez Vérifier Le Nom et Prénom de patiente entrée S'il Vous Plait ")
    # function that changes the client info and puts them in the GUI and fills the fields
    def change_info(self):
        try:
            # getting current client info
            husband_name = self.Get_Husbands_surname().upper()
        except AttributeError:
            return
        birthday = self.Get_Birth_date()
        if birthday == "":
            return
        # getting list of possible client info with the current client name
        info_possible = self.list_possible_client_info()
        # checking where in the possible client list we are situated so we avoid 
        # a bug where we can only get two clients informations on screen because the comparason
        # won't reach the other client's informations if the first 2 clients informations are different
        # the index is the current case in the possible information 
        # if the index is the last case in the possible info list make it -1 so we can compare the
        # first case of the list since in the next loop we use index+1 which will allow us to start from 0 
        for thing in range(len(info_possible)):
            birthday_possible = str(info_possible[thing][1]).replace("-","/")
            if husband_name == info_possible[thing][0] and birthday == birthday_possible:
                index = thing
                if index == len(info_possible)-1:
                    index = -1
                break
        # compare the client info from the current information on screen to the end of the list
        # untill we find different client information (difference in husband family name or birthday)
        # and fill the fields in the gui with the next client information you find 
        for from_current in range(index+1,len(info_possible)):
            birthday_possible = str(info_possible[from_current][1]).replace("-","/")
            if husband_name == info_possible[from_current][0] and birthday == birthday_possible:
                pass
            else:
                self.Patient_husbands_surname_field.delete(0, END)
                self.Patient_husbands_surname_field.insert(0, info_possible[from_current][0].lower())
                self.Patient_birthday_field.delete(0, END)
                self.Patient_birthday_field.insert(0, str(info_possible[from_current][1]).replace("-","/"))
                break
    




            

                    


            





        


b = app_buttons(root)

root.mainloop()