from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mcp
from tkcalendar import DateEntry

#================================== Create Class ===================================

class guest:

#*********************************** 1st Window ************************************

    def __init__(self,hello):
        self.hello = hello
        self.hello.title('Welcome!!!') # Add title to first window
        self.hello.geometry('600x630+0+0') # Add dimensions to first window
        self.hello.config(bg='white')

        #============================== Display Frame ==============================
        
        Display_Frame = Frame(hello, bd=15, relief= RIDGE, bg='dark red')
        Display_Frame.place(x=0, y=90, width=600, height=540)

        #======================= Add title to Display Frame ========================
        
        title = Label(hello , text = 'WELCOME!!!',bd=6,relief= RAISED, font=('ALGERIAN',50,'bold','underline'), bg='black', fg='crimson')
        title.pack(side=TOP , fill='x')

        #========================= Details of Room charges =========================


        details=Label(Display_Frame, text='Following are the room charges per night:',bd=0,font=('Arial',18,'bold'), bg='dark red',fg='black')
        details.grid(row=1,column=0,sticky='w')
     
        details1=Label(Display_Frame, text='1. Standard Room : Rs. 25,000',bd=0,font=('Arial',18),bg='dark red', fg='black')
        details1.grid(row=2,column=0,sticky='w')

        details2=Label(Display_Frame, text='2. Premium Room : Rs. 28,000',bd=0,font=('Arial',18),bg='dark red', fg='black')
        details2.grid(row=3,column=0,sticky='w')

        details3=Label(Display_Frame, text='3. Lake View Room: Rs. 32,500',bd=0,font=('Arial',18),bg='dark red', fg='black')
        details3.grid(row=4,column=0,sticky='w')

        details4=Label(Display_Frame, text='4. City View Room: Rs. 36,000',bd=0,font=('Arial',18),bg='dark red', fg='black')
        details4.grid(row=5,column=0,sticky='w')

        details5=Label(Display_Frame, text='5. Business Class Room : Rs. 40,000',bd=0,font=('Arial',18),bg='dark red', fg='black')
        details5.grid(row=6,column=0,sticky='w')

        details6=Label(Display_Frame, text='6. Executive Suite: Rs. 50,000',bd=0,font=('Arial',18),bg='dark red', fg='black')
        details6.grid(row=7,column=0,sticky='w')

        details7=Label(Display_Frame, text='7. Grand Suite: Rs. 65,000',bd=0,font=('Arial',18),bg='dark red', fg='black')
        details7.grid(row=8,column=0,sticky='w')

        details8=Label(Display_Frame, text='8. Presidential Suite: Rs. 1,00,000',bd=0,font=('Arial',18),bg='dark red', fg='black')
        details8.grid(row=9,column=0,sticky='w')
        
        #======================== Details of Meal charges ==========================

        details9=Label(Display_Frame, text='Following are the meal charges per day \n \t\t(3 meals per day):',bd=0,font=('Arial',18,'bold'),bg='dark red', fg='black')
        details9.grid(row=10,column=0,sticky='w')

        details10=Label(Display_Frame, text='1. Standard Veg : Rs. 900',bd=0,font=('Arial',18),bg='dark red', fg='black')
        details10.grid(row=11,column=0,sticky='w')

        details11=Label(Display_Frame, text='2. Standard Non-Veg : Rs. 1,100',bd=0,font=('Arial',18),bg='dark red', fg='black')
        details11.grid(row=12,column=0,sticky='w')

        details12=Label(Display_Frame, text='3. Premium Veg : Rs. 1,500',bd=0,font=('Arial',18),bg='dark red', fg='black')
        details12.grid(row=13,column=0,sticky='w')

        details13=Label(Display_Frame, text='4. Premiun Non-Veg : Rs. 2,000',bd=0,font=('Arial',18),bg='dark red', fg='black')
        details13.grid(row=14,column=0,sticky='w')


        #========================= Button to open Main Menu ========================

        btn1 = Button(Display_Frame, text='CLICK HERE TO GO TO MAIN MENU',font=('snap ITC',9),bg='gold',fg='blue',activebackground='green',activeforeground='white',width=30, command=self.main_menu)
        btn1.grid(row=15, column=0, padx=100, pady=5)
        

        
#*********************************** 2nd Window ************************************

    def main_menu(self):

        #============================ Create Main Menu =============================

        root = Toplevel(bg='black')
        root.title('Hotel Management System')
        root.geometry('1358x768-0+0')
        root.config(bg='black')


        title = Label(root , text = 'Vank Hoff Hotel',bd=6,relief= RAISED, font=('ALGERIAN',50,'bold','underline'), bg='black', fg='crimson')
        title.pack(side=TOP , fill='x')

        #================================ Variables ================================

        self.Room_No_var=StringVar() # variable to store room number
        
        self.type_var=StringVar() # variable to store room type
        
        self.name_var=StringVar() # variable to store name
        
        self.gender_var=StringVar() # variable to store gender
        
        self.contact_var=StringVar() # variable to store contact number
        
        self.in_var=StringVar() # variable to store check in date
        
        self.out_var=StringVar() # variable to store check out date
        
        self.days_var=StringVar() # variable to store number of days of stay
        
        self.nationality_var=StringVar() # variable to store nationality
        
        self.dob_var=StringVar() # variable to store date of birth
        
        self.email_var=StringVar() # variable to store email id

        self.id_var=StringVar() # variable to store identity type
        
        self.address_var=StringVar() # variable to store address
        
        self.meal_var=StringVar() # variable to store meal type
        
        self.search_by=StringVar() # variable to store search variable
        
        self.search_txt=StringVar() # variable to store search text
        
        self.stay_var=IntVar() # variable to calculate stay charge
        
        self.food_var=IntVar() # variable to calculate meal charge
        
        self.sub_total=IntVar() # variable to calculate sub total

        self.tax_var=IntVar() # variable to calculate tax on sub total
        
        self.total_bill=IntVar() # variable to calculate total bill


        #=========================== Set initial value to Null =====================

        self.Room_No_var.set("")
        
        self.type_var.set("")
        
        self.name_var.set("")
        
        self.gender_var.set("")
        
        self.contact_var.set("")

        self.in_var.set("")
        
        self.out_var.set("")
        
        self.days_var.set("")
        
        self.nationality_var.set("")

        self.dob_var.set("")

        self.email_var.set("")
        
        self.id_var.set("")

        self.address_var.set("")
        
        self.meal_var.set("")
        
        self.search_by.set("")
        
        self.search_txt.set("")
        
        #=============================== Manage Frame ==============================

        Manage_Frame = Frame(root, bd=6, relief= SUNKEN, bg='blue')
        Manage_Frame.place(x=5, y=90, width=1350, height=640)

        #====================== Add widgets in Manage Frame ========================

        lbl_Name= Label(Manage_Frame, text='NAME:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        lbl_Name.grid(row=0, column=0, pady=3, padx=20, sticky='w')

        enter_Name = Entry(Manage_Frame,textvariable=self.name_var,font=('arial',15,'bold'), bd=5, relief= GROOVE,width=25)
        enter_Name.grid(row=0, column=1, pady=3, padx=0, sticky='w')
        

        lbl_Room_Type= Label(Manage_Frame, text='ROOM TYPE:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        lbl_Room_Type.grid(row=1, column=0, pady=3, padx=20, sticky='w')

        combo_Room_Type = ttk.Combobox(Manage_Frame,textvariable=self.type_var,font=('arial',15,'bold'), state='readonly', width=24,height=5)
        combo_Room_Type['values']=('Standard Room','Premium Room','Lake View Room','City View Room','Business Class Room','Executive Suite','Grand Suite','Presidential Suite')
        combo_Room_Type.grid(row=1, column=1, pady=0, padx=0)
        combo_Room_Type.current()


        lbl_Room= Label(Manage_Frame, text='ROOM NO:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        lbl_Room.grid(row=2, column=0, pady=3, padx=20, sticky='w')
        
        combo_room_no = ttk.Combobox(Manage_Frame,textvariable=self.Room_No_var,font=('arial',15,'bold'), state='readonly', width=24,height=5)
        combo_room_no['values']=('1011','1012','1013','1014','1015','1016','1017','1018','1019','1020','2011','2012','2013','2014','2015','2016',
                                 '2017','2018','2019','2020','3011','3012','3013','3014','3015','3016','3017','3018','3019','3020','4011','4012',
                                 '4013','4014','4015','4016','4017','4018','4019','4020','5011','5012','5013','5014','5015','5016','5017','5018',
                                 '5019','5020','6011','6012','6013','6014','6015','6016','6017','6018','6019','6020','7011','7012','7013','7014',
                                 '7015','7016','7017','7018','7019','7020','8011','8012','8013','8014','8015','8016','8017','8018','8019','8020',
                                 '9011','9012','9013','9014','9015','9016','9017','9018','9019','9020')
        combo_room_no.grid(row=2, column=1, pady=3, padx=0)


        lbl_Gender= Label(Manage_Frame, text='GENDER:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        lbl_Gender.grid(row=3, column=0, pady=3, padx=20, sticky='w')

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=('arial',15,'bold'), state='readonly', width=24)
        combo_gender['values']=('Male','Female','Other')
        combo_gender.grid(row=3, column=1, pady=3, padx=0)


        lbl_Contact= Label(Manage_Frame, text='CONTACT:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        lbl_Contact.grid(row=4, column=0, pady=3, padx=20, sticky='w')

        lbl_Contact = Entry(Manage_Frame,textvariable=self.contact_var,font=('arial',15,'bold'), bd=5, relief= GROOVE,width=25)
        lbl_Contact.grid(row=4, column=1, pady=3, padx=0, sticky='w')


        lbl_in= Label(Manage_Frame, text='CHECK IN DATE:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        lbl_in.grid(row=5, column=0, pady=3, padx=20, sticky='w')

        check_in = DateEntry(Manage_Frame,textvariable=self.in_var,font=('arial',15,'bold'), width=24,background='darkblue', foreground='white', borderwidth=2,state='readonly')
        check_in.grid(row=5, column=1, pady=3, padx=0, sticky='w')


        lbl_out= Label(Manage_Frame, text='CHECK OUT DATE:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        lbl_out.grid(row=6, column=0, pady=3, padx=20, sticky='w')

        check_out = DateEntry(Manage_Frame,textvariable=self.out_var,font=('arial',15,'bold'), width=24,background='darkblue', foreground='white', borderwidth=2,state='readonly')
        check_out.grid(row=6, column=1, pady=3, padx=0, sticky='w')


        lbl_days= Label(Manage_Frame, text='NO. OF DAYS:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        lbl_days.grid(row=7, column=0, pady=3, padx=20, sticky='w')

        lbl_days = Entry(Manage_Frame,textvariable=self.days_var,font=('arial',15,'bold'), bd=5, relief= GROOVE,width=25)
        lbl_days.grid(row=7, column=1, pady=3, padx=0, sticky='w')


        lbl_nationality= Label(Manage_Frame, text='NATIONALITY:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        lbl_nationality.grid(row=8, column=0, pady=3, padx=20, sticky='w')

        combo_nationality = ttk.Combobox(Manage_Frame,textvariable=self.nationality_var,font=('arial',15,'bold'), state='readonly', width=24,height=8)
        combo_nationality['values']=('Afghan','Albanian','Algerian','American','Andorran','Angolan','Antiguans','Argentinean','Armenian','Australian','Austrian','Azerbaijani','Bahamian',
                                     'Bahraini','Bangladeshi','Barbadian','Barbudans','Batswana','Belarusian','Belgian','Belizean','Beninese','Bhutanese','Bolivian','Bosnian','Brazilian',
                                     'British','Bruneian','Bulgarian','Burkinabe','Burmese','Burundian','Cambodian','Cameroonian','Canadian','Cape Verdean','Canrat African','Chadian',
                                     'Chilean','Chinese','Colombian','Comoran','Congolese','Costa Rican','Croatian','Cuban','Cyprot','Czech','Danish','Djinouti','Dominican','Dutch','East Timorese',
                                     'Ecuadorean','Egyptian','Emirian','Equatorial Guinean','Eritrean','Estonian','Ethiopian','Fijian','filipino','Finnish','French','Gabonese','Gambian','Georgian',
                                     'German','Ghanian','Greek','Grenadian','Guatemalan','Guinea-Bissauan','Guinean','Guyanese','Haitian','Herzegovinian','Honduran','Hungarian','Icelander','Indian',
                                     'Indonesian','Iranian','Iraqi','Irish','Israeli','Italian','Ivorian','Jamaican','Japanese','Jordanian','Kazakhstani','Kenyan','Kittian and Nevisian','Kuwaiti',
                                     'kuwaiti','kyrgyz','laotian','latvian','lebanese','liberian','libyan','liechtensteiner','lithuanian','luxembourger','macedonian','malagasy','malawian','malaysian',
                                     'maldivan','malian','maltese','marshallese','mauritanian','mauritian','mexican','micronesian','moldovan','monacan','mongolian','moroccan','mosotho','motswana',
                                     'mozambican','namibian','nauruan','nepalese','New Zealander','Ni-Vanuatu','Nicaraguan','Nigerien','North Korean','Northern Irish','Norwegian','Omani','Pakistani',
                                     'Palauan','Panamanian','Papua New Guinean','Paraguayan','Peruvian','Polish','Portugese','Qatari','Romanian','Russian','Rwandan','Saint Lucian','Salvadoran',
                                     'Samoan','San Marinese','Sao Tomean','Saudi Arabian','Scottish','Senegalese','Serbian','Seychellois','Sierra Leonean','Singaporean','Slovakian','Soloman Islander',
                                     'Somali','South African','South Korean','Spanish','Sri Lankan','Sudanese','Surinamer','Swazi','Swedish','Swiss','Syrian','Taiwanese','Tajik','Tanzanian','Thai',
                                     'Togolese','Tongon','Trinidanian or Tobagonian','Tunisian','Turkish','Tuvaluan','Ugandan','Ukrainian','Uruguayan','Uzbekistani','Venezuelan','Vietnamese',
                                     'Welsh','Yemenite','Zambian','Zimbabwean')
        combo_nationality.grid(row=8, column=1, pady=3, padx=0)


        lbl_dob= Label(Manage_Frame, text='DATE OF BIRTH:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        lbl_dob.grid(row=9, column=0, pady=3, padx=20, sticky='w')

        dob = DateEntry(Manage_Frame,textvariable=self.dob_var,font=('arial',15,'bold'), width=24, year=2001,background='darkblue', foreground='white', borderwidth=2,state='readonly')
        dob.grid(row=9, column=1, pady=3, padx=0, sticky='w')


        email_id= Label(Manage_Frame, text='EMAIL ID:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        email_id.grid(row=10, column=0, pady=3, padx=20, sticky='w')

        lbl_email = Entry(Manage_Frame,textvariable=self.email_var,font=('arial',15,'bold'), bd=5, relief= GROOVE,width=25)
        lbl_email.grid(row=10, column=1, pady=3, padx=0, sticky='w')


        lbl_id= Label(Manage_Frame, text='ID TYPE:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        lbl_id.grid(row=11, column=0, pady=3, padx=20, sticky='w')

        combo_id_type = ttk.Combobox(Manage_Frame,textvariable=self.id_var,font=('arial',15,'bold'), state='readonly', width=24)
        combo_id_type['values']=('Driving License','Passport','Voter ID','Aadhar Card','PAN Card')
        combo_id_type.grid(row=11, column=1, pady=3, padx=0)
        combo_id_type.current()


        address= Label(Manage_Frame, text='ADDRESS:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        address.grid(row=12, column=0, pady=3, padx=20, sticky='w')

        lbl_address = Entry(Manage_Frame,textvariable=self.address_var,font=('arial',15,'bold'), bd=5, relief= GROOVE,width=25)
        lbl_address.grid(row=12, column=1, pady=3, padx=0, sticky='w')


        lbl_meal= Label(Manage_Frame, text='MEAL TYPE:',bg='blue',fg='Silver', font=('arial',15,'bold'))
        lbl_meal.grid(row=13, column=0, pady=3, padx=20, sticky='w')

        combo_meal_type = ttk.Combobox(Manage_Frame,textvariable=self.meal_var,font=('arial',15,'bold'), state='readonly', width=24)
        combo_meal_type['values']=('Standard Veg','Standard Non-Veg','Premium Veg','Premium Non-Veg')
        combo_meal_type.grid(row=13, column=1, pady=3, padx=0)
        combo_meal_type.current()


        #============================== Button Frame ===============================

        Btn_Frame = Frame(Manage_Frame, bd=5, bg='crimson', relief = RAISED)
        Btn_Frame.place(x=12, y=550, width=500,height=50)

        #================================== Buttons ================================

        Addbtn = Button(Btn_Frame, text='ADD',font=('snap ITC',9),bg='gold',fg='blue',activebackground='green',activeforeground='white',width=8, command=self.add_guests)
        Addbtn.grid(row=0, column=0, padx=8, pady=5)
        
        updatebtn = Button(Btn_Frame, text='UPDATE',font=('snap ITC',9),bg='gold',fg='blue',activebackground='green',activeforeground='white', width=8,command=self.update_data)
        updatebtn.grid(row=0, column=1, padx=8, pady=5)
        
        deletebtn = Button(Btn_Frame, text='DELETE',font=('snap ITC',9),bg='gold',fg='blue',activebackground='green',activeforeground='white', width=8,command=self.delete_data)
        deletebtn.grid(row=0, column=2, padx=8, pady=5)
        
        clearbtn = Button(Btn_Frame, text='CLEAR',font=('snap ITC',9),bg='gold',fg='blue',activebackground='green',activeforeground='white', width=8,command=self.clear)
        clearbtn.grid(row=0, column=3, padx=8, pady=5)
        
        billbtn = Button(Btn_Frame, text='BILL',font=('snap ITC',9),bg='gold',fg='blue',activebackground='green',activeforeground='white', width=8,command=self.wind)
        billbtn.grid(row=0, column=4, padx=8, pady=5)

        #================================= Search ==================================

        lblsearch = Label(Manage_Frame, text='Search By:',bg='blue',fg='lime', font=('arial',20,'bold','italic','underline'))
        lblsearch.grid(row=0, column=2, pady=5, padx=10, sticky='w')

        combo_search = ttk.Combobox(Manage_Frame,textvariable=self.search_by,font=('arial',15,'bold'), state='readonly', width=15)
        combo_search['values']=('Room_No','Name','Contact')
        combo_search.grid(row=0, column=2, pady=3, padx=165, sticky='w')


        txt_search = Entry(Manage_Frame,textvariable=self.search_txt,font=('arial',15,'bold'), bd=2,relief=GROOVE ,width=15)
        txt_search.grid(row=0, column=2, pady=3, padx=365, sticky='w')

        searchbtn = Button(Manage_Frame, text='Search', width=10, pady=3,command=self.search_data)
        searchbtn.grid(row=0, column=2, padx=550, pady=3,sticky='w')
        
        showallbtn = Button(Manage_Frame, text='Show All', width=10, pady=3,command=self.fetch_data)
        showallbtn.grid(row=0, column=2, padx=640, pady=3,sticky='w')


        #=============================== Table Frame ===============================


        Table_Frame = Frame(Manage_Frame, bd=6, relief= GROOVE, bg='black')
        Table_Frame.place(x=525, y=50, width=800, height=550)

        scroll_x = Scrollbar(Table_Frame, orient = HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient = VERTICAL)
        self.guest_table = ttk.Treeview(Table_Frame, columns=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'), xscrollcommand=scroll_x.set ,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.guest_table.xview)                             
        scroll_y.config(command=self.guest_table.yview)
        self.guest_table.heading('1', text='Room No.')
        self.guest_table.heading('2', text='Room Type')
        self.guest_table.heading('3', text='Name')
        self.guest_table.heading('4', text='Gender')
        self.guest_table.heading('5', text='Contact')
        self.guest_table.heading('6', text='Check In')
        self.guest_table.heading('7', text='Check Out')
        self.guest_table.heading('8', text='No Of Days')
        self.guest_table.heading('9', text='Nationality')
        self.guest_table.heading('10', text='Date Of Birth')
        self.guest_table.heading('11', text='Email')
        self.guest_table.heading('12', text='Identity')
        self.guest_table.heading('13', text='Address')
        self.guest_table.heading('14', text='Meal Type')
        
        self.guest_table['show']='headings'
        
        self.guest_table.column('1',width=70)
        self.guest_table.column('2',width=150)
        self.guest_table.column('3',width=150)
        self.guest_table.column('4',width=70)
        self.guest_table.column('5',width=150)
        self.guest_table.column('6',width=150)
        self.guest_table.column('7',width=150)
        self.guest_table.column('8',width=120)
        self.guest_table.column('9',width=200)
        self.guest_table.column('10',width=100)
        self.guest_table.column('11',width=200)
        self.guest_table.column('12',width=100)
        self.guest_table.column('13',width=120)
        self.guest_table.column('14',width=150)

        self.guest_table.pack(fill= BOTH,expand='1')
        self.guest_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
        
#==================================== FUNCTIONS ====================================

    #***************************** add_guests Function *****************************    
        
    def add_guests(self):
        if self.Room_No_var.get()=='' or self.type_var.get()=='' or self.gender_var.get()=='' or self.contact_var.get()=='' or self.in_var.get()=='' or self.out_var.get()=='' or self.days_var.get()=='' or  self.nationality_var.get()=='' or self.dob_var.get()=='' or self.email_var.get()=='' or self.id_var.get()=='' or self.address_var.get()=='' or self.meal_var.get()=='' :
            messagebox.showerror('Error','All Fields Are Required')
        else:
            con=mcp.connect(host='localhost', user='root', password='pass', database='hms')
            cur=con.cursor()
            cur.execute('insert into guest_det values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                                                    (self.Room_No_var.get(),
                                                                     self.type_var.get(),
                                                                     self.name_var.get(),
                                                                     self.gender_var.get(),
                                                                     self.contact_var.get(),
                                                                     self.in_var.get(),
                                                                     self.out_var.get(),
                                                                     self.days_var.get(),
                                                                     self.nationality_var.get(),
                                                                     self.dob_var.get(),
                                                                     self.email_var.get(),
                                                                     self.id_var.get(),
                                                                     self.address_var.get(),
                                                                     self.meal_var.get()
                                                                     ))
            con.commit()
            
            self.fetch_data()

            self.clear()

            con.close()

            messagebox.showinfo('Success','Record has been inserted')
            
    #***************************** fetch_data Function *****************************


    def fetch_data(self):
        
        con=mcp.connect(host='localhost', user='root', passwd='pass', database='hms')
        cur=con.cursor()
        cur.execute('select * from guest_det')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.guest_table.delete(* self.guest_table.get_children())
            for row in rows:
                self.guest_table.insert('',END, values=row)

            con.commit()
        con.close()
        
        self.clear()
     
    #******************************** clear Function *******************************


    def clear(self):
        
        self.Room_No_var.set("")

        self.type_var.set("")

        self.name_var.set("")

        self.gender_var.set("")

        self.contact_var.set("")

        self.days_var.set("")

        self.search_by.set("")

        self.search_txt.set("")

        self.nationality_var.set("")

        self.in_var.set("")

        self.out_var.set("")

        self.dob_var.set("")

        self.nationality_var.set("")

        self.email_var.set("")

        self.address_var.set("")

        self.meal_var.set("")

        self.id_var.set("")
        
    #***************************** get_cursor Function *****************************

        
    def get_cursor(self,ev):
        
        cursor_row=self.guest_table.focus()
        content=self.guest_table.item(cursor_row)
        
        self.row=content['values']
        
        self.Room_No_var.set(self.row[0])
        self.type_var.set(self.row[1])
        self.name_var.set(self.row[2])
        self.gender_var.set(self.row[3])
        self.contact_var.set(self.row[4])
        self.in_var.set(self.row[5])
        self.out_var.set(self.row[6])
        self.days_var.set(self.row[7])
        self.nationality_var.set(self.row[8])
        self.dob_var.set(self.row[9])
        self.email_var.set(self.row[10])
        self.id_var.set(self.row[11])
        self.address_var.set(self.row[12])
        self.meal_var.set(self.row[13])
        

    #***************************** update_data Function ****************************


    def update_data(self):
        
        con=mcp.connect(host='localhost', user='root', password='pass', database='hms')
        cur=con.cursor()
        cur.execute('update guest_det set Room_Type=%s,Name=%s,Gender=%s,Contact=%s,Check_in_Date=%s,Check_out_Date=%s,No_of_Days=%s,Nationality=%s,Date_of_Birth=%s,Email_id=%s,Identity=%s,Address=%s,Meal_Type=%s where Room_No=%s',(
                                                                     self.type_var.get(),
                                                                     self.name_var.get(),
                                                                     self.gender_var.get(),
                                                                     self.contact_var.get(),
                                                                     self.in_var.get(),
                                                                     self.out_var.get(),
                                                                     self.days_var.get(),
                                                                     self.nationality_var.get(),
                                                                     self.dob_var.get(),
                                                                     self.email_var.get(),
                                                                     self.id_var.get(),
                                                                     self.address_var.get(),
                                                                     self.meal_var.get(),
                                                                     self.Room_No_var.get()
                                                                          ))
        con.commit()
        self.fetch_data()
        self.clear()
        messagebox.showinfo('Update Success','Record has been updated')
        con.close()

    #***************************** delete_data Function ****************************

    def delete_data(self):
        
        con=mcp.connect(host='localhost', user='root', passwd='pass', database='hms')
        cur=con.cursor()
        cur.execute('delete from guest_det where room_no= %s;',(self.Room_No_var.get(),))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo('Success','Record has been deleted')
         
    #***************************** search_data Function ****************************

    def search_data(self):
        
        con=mcp.connect(host='localhost', user='root', passwd='pass', database='hms')
        cur=con.cursor()
        sby=self.search_by.get()
        
        if sby== 'Name':
            q="select * from guest_det where Name LIKE '%"+str(self.search_txt.get())+"%'"
        else:
            q="select * from guest_det where "+str(self.search_by.get())+" = "+str(self.search_txt.get())

        cur.execute(q)
        rows=cur.fetchall()
        if len(rows)!=0:
            self.guest_table.delete(* self.guest_table.get_children())
            for row in rows:
                self.guest_table.insert('',END, values=row)

            con.commit()
        con.close()
        self.clear()

    #******************************** bill Function ********************************


    def bill(self):
        
        if self.type_var.get()=='Standard Room':
            self.stay_var=25000*int(self.days_var.get())

        elif self.type_var.get()=='Premium Room':
            self.stay_var=28000*int(self.days_var.get())

        elif self.type_var.get()=='Lake View Room':
            self.stay_var=32500*int(self.days_var.get())

        elif self.type_var.get()=='City View Room':
            self.stay_var=36000*int(self.days_var.get())

        elif self.type_var.get()=='Business Class Room':
            self.stay_var=40000*int(self.days_var.get())

        elif self.type_var.get()=='Executive Suite':
            self.stay_var=50000*int(self.days_var.get())

        elif self.type_var.get()=='Grand Suite':
            self.stay_var=65000*int(self.days_var.get())

        else:   # when self.type_var.get()=='Presidential Suite'
            self.stay_var=100000*int(self.days_var.get())
                
        
    #****************************** food_bill Function *****************************    


    def food_bill(self):

        if self.meal_var.get()=='Standard Veg':
            self.food_var=900*int(self.days_var.get())

        elif self.meal_var.get()=='Standard Non-Veg':
            self.food_var=1100*int(self.days_var.get())

        elif self.meal_var.get()=='Premium Veg':
            self.food_var=1500*int(self.days_var.get())

        else:
            self.food_var=2000*int(self.days_var.get())
                
        self.clear()

    #******************************** tax Function *********************************

    def tax(self):
        self.tax_var=int(0.18*(self.stay_var+self.food_var))


#*********************************** 2nd Window ************************************

    def wind(self):
        
        top = Toplevel(bg='tan')
        top.geometry('610x730+370+0')
        top.title('Receipt')

        #=============================== Main Frame ================================
        
        Main_Frame = Frame(top, bd=30, relief= RIDGE, bg='dark red')
        Main_Frame.place(x=0, y=0, width=610, height=730)

        #========================== Widgets in Main Frame ==========================

        lbl_Name= Label(Main_Frame, text='NAME:',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_Name.grid(row=0, column=0, pady=3, padx=10, sticky='w')

        lbl_Name1 = Label(Main_Frame, text=self.name_var.get(),font=('arial',15,'bold'), bd=5, relief= GROOVE,width=20)
        lbl_Name1.grid(row=0, column=1, pady=3, padx=0, sticky='w')


        lbl_Room = Label(Main_Frame, text='ROOM NO:',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_Room.grid(row=1, column=0, pady=3, padx=10, sticky='w')

        lbl_Room1 = Label(Main_Frame, text=self.Room_No_var.get(),font=('arial',15,'bold'),bd=5,relief=GROOVE,width=20)
        lbl_Room1.grid(row=1, column=1, pady=3, padx=0, sticky='w')


        lbl_type = Label(Main_Frame, text='ROOM TYPE:',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_type.grid(row=2, column=0, pady=3, padx=10, sticky='w')

        lbl_type1 = Label(Main_Frame, text=self.type_var.get(),font=('arial',15,'bold'),bd=5,relief=GROOVE,width=20)
        lbl_type1.grid(row=2, column=1, pady=3, padx=0, sticky='w')


        lbl_contact= Label(Main_Frame, text='CONTACT:',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_contact.grid(row=3, column=0, pady=3, padx=10, sticky='w')

        lbl_contact1 = Label(Main_Frame, text=self.contact_var.get(),font=('arial',15,'bold'), bd=5, relief= GROOVE,width=20)
        lbl_contact1.grid(row=3, column=1, pady=3, padx=0, sticky='w')


        lbl_email = Label(Main_Frame, text='EMAIL ID:',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_email.grid(row=4, column=0, pady=3, padx=10, sticky='w')

        lbl_email1 = Label(Main_Frame, text=self.email_var.get(),font=('arial',15,'bold'), bd=5, relief= GROOVE,width=20)
        lbl_email1.grid(row=4, column=1, pady=3, padx=0, sticky='w')


        lbl_in = Label(Main_Frame, text='CHECK IN DATE:',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_in.grid(row=5, column=0, pady=3, padx=10, sticky='w')

        lbl_in1 = Label(Main_Frame, text=self.in_var.get(),font=('arial',15,'bold'),bd=5,relief=GROOVE,width=20)
        lbl_in1.grid(row=5, column=1, pady=3, padx=0, sticky='w')


        lbl_out= Label(Main_Frame, text='CHECK OUT DATE:',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_out.grid(row=6, column=0, pady=3, padx=10, sticky='w')

        lbl_out1 = Label(Main_Frame, text=self.out_var.get(),font=('arial',15,'bold'), bd=5, relief= GROOVE,width=20)
        lbl_out1.grid(row=6, column=1, pady=3, padx=0, sticky='w')


        lbl_days = Label(Main_Frame, text='NO. OF DAYS:',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_days.grid(row=7, column=0, pady=3, padx=10, sticky='w')

        lbl_days1 = Label(Main_Frame, text=self.days_var.get(),font=('arial',15,'bold'),bd=5,relief=GROOVE,width=20)
        lbl_days1.grid(row=7, column=1, pady=3, padx=0, sticky='w')
        

        lbl_meal_type = Label(Main_Frame, text='MEAL TYPE:',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_meal_type.grid(row=8, column=0, pady=3, padx=10, sticky='w')

        lbl_meal_type1 = Label(Main_Frame, text=self.meal_var.get(),font=('arial',15,'bold'),bd=5,relief=GROOVE,width=20)
        lbl_meal_type1.grid(row=8, column=1, pady=3, padx=0, sticky='w')


        self.bill()     

        lbl_stay_charge = Label(Main_Frame, text='STAY CHARGE:',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_stay_charge.grid(row=9, column=0, pady=3, padx=10, sticky='w')

        lbl_stay_charge1 = Label(Main_Frame, text='Rs. '+str(self.stay_var),font=('arial',15,'bold'),bd=5,relief=GROOVE,width=20)
        lbl_stay_charge1.grid(row=9, column=1, pady=3, padx=0, sticky='w')


        self.food_bill()

        lbl_food_charge = Label(Main_Frame, text='MEAL CHARGE:',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_food_charge.grid(row=10, column=0, pady=3, padx=10, sticky='w')

        lbl_food_charge1 = Label(Main_Frame, text='Rs. '+str(self.food_var),font=('arial',15,'bold'),bd=5,relief=GROOVE,width=20)
        lbl_food_charge1.grid(row=10, column=1, pady=3, padx=0, sticky='w')


        self.sub_total=self.food_var+self.stay_var

        lbl_sub_total = Label(Main_Frame, text='SUB TOTAL:',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_sub_total.grid(row=11, column=0, pady=3, padx=10, sticky='w')

        lbl_sub_total_1 = Label(Main_Frame, text='Rs. '+str(self.sub_total),font=('arial',15,'bold'),bd=5,relief=GROOVE,width=20)
        lbl_sub_total_1.grid(row=11, column=1, pady=3, padx=0, sticky='w')


        self.tax()
        
        lbl_tax = Label(Main_Frame, text='TAX (18%) :',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_tax.grid(row=12, column=0, pady=3, padx=10, sticky='w')

        lbl_tax1 = Label(Main_Frame, text='Rs. '+str(self.tax_var),font=('arial',15,'bold'),bd=5,relief=GROOVE,width=20)
        lbl_tax1.grid(row=12, column=1, pady=3, padx=0, sticky='w')


        self.total_bill=self.tax_var + self.sub_total

        lbl_total_bill = Label(Main_Frame, text='TOTAL BILL:',bg='dark red',fg='Black', font=('arial',20,'bold'))
        lbl_total_bill.grid(row=13, column=0, pady=3, padx=10, sticky='w')

        lbl_total_bill_1 = Label(Main_Frame, text='Rs. '+str(self.total_bill),font=('arial',15,'bold'),bd=5,relief=GROOVE,width=20)
        lbl_total_bill_1.grid(row=13, column=1, pady=3, padx=0, sticky='w')

        #============================== Button Frame ===============================

        Btn_Frame = Frame(Main_Frame, bd=0, bg='dark red', relief = RAISED)
        Btn_Frame.place(x=180, y=620, width=180,height=50)

        btn1 = Button(Btn_Frame, text='PRINT',font=('snap ITC',9),bg='gold',fg='blue',activebackground='green',activeforeground='white',width=16,command=top.destroy)
        btn1.grid(row=0, column=0, padx=6, pady=5)

#=================================== Begins Here ===================================

hello=Tk()
ob = guest(hello)