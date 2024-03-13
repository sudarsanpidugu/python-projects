from tkinter import *
import pymysql
from tkinter import ttk

class NTHStudentsData:
        def __init__(self,root):
                self.root = root
                self.root.title('Welcome to Software Planet')
                self.root.geometry('1410x700')
                title = Label(self.root, text='Welcome to Software Planet',
                        bd=4,
                        relief=GROOVE, bg='green', fg='white', font=('Comic Sans MS',20,'bold'))
                title.pack(fill=X, side=TOP)

                self.roll_no_var = StringVar()
                self.first_name_var = StringVar()
                self.last_name_var = StringVar()
                self.email_var = StringVar()
                self.mobile_var =StringVar()
                self.course_name_var = StringVar()
                self.fee_var = StringVar()
                self.institute_var = StringVar()
                self.qualification_var = StringVar()
                self.location_var =  StringVar()

                self.searchby = StringVar()
                self.searchtxt = StringVar()




        # ==================== # Creating Left DataEntry Frame:-- # =============================/=
                DataEntryFrame = Frame(self.root, bg='green', bd=5, relief=GROOVE)
                DataEntryFrame.place(x=10, y=60, width=400, height=630)

                title = Label(DataEntryFrame, text='Students Data Entry', bg='green', fg='white', font=('times new roman',20,'bold'))
                title.grid(row=0, columnspan=2, padx=10, pady=10)

        # RoolNo, FirstName, LastName, Email, Mobile, Course Name, Fee, Institution, Qualification, Location.

        # =======Roll Name ==========
                lb1_roll_no =Label(DataEntryFrame,text="Roll No:", bg='green', fg='white', font=('times new roman',15,'bold'))
                lb1_roll_no.grid(row=1,column=0,sticky='W',)
                
                txt_rool_no=Entry(DataEntryFrame, textvariable=self.roll_no_var, font=('times new roman',15, 'bold'))
                txt_rool_no.grid(row=1,column=1,sticky='E')

        # =======First Name ==========
                lb2_first_name=Label(DataEntryFrame, text='First Name:', bg='green', fg='white', font=('times new roman',15,'bold'))
                lb2_first_name.grid(row=2,column=0, sticky='W', pady=10)
                
                txt_first_name=Entry(DataEntryFrame, textvariable=self.first_name_var, font=('times new roman',15, 'bold'))
                txt_first_name.grid(row=2,column=1,sticky='E')
        # =======Last Name ==========
                lb3_lst_name=Label(DataEntryFrame,text='Last Name:', bg='green', fg='white', font=('times new roman',15,'bold'))
                lb3_lst_name.grid(row=3,column=0, sticky='W')
                
                txt_last_name=Entry(DataEntryFrame, textvariable=self.last_name_var,font=('times new roman',15, 'bold'))
                txt_last_name.grid(row=3,column=1,sticky='E')

        # ======= Email ==========
                EmailLb1=Label(DataEntryFrame,text="Email:", bg='green', fg='white', font=('times new roman',15,'bold'))
                EmailLb1.grid(row=4,column=0,sticky='W',pady=10)
                
                EmailEntry=Entry(DataEntryFrame,textvariable=self.email_var, font=('Times New Roman',15))
                EmailEntry.grid(row=4,column=1,sticky='E')

        # ======= Mobile ==========
                MobileLb1=Label(DataEntryFrame,text="Mobile:", bg='green', fg='white', font=('times new roman',15,'bold'))
                MobileLb1. grid(row=5,column=0,sticky='W', )
                
                MobileEntry=Entry(DataEntryFrame, textvariable=self.mobile_var, font=('Times New Roman',15))
                MobileEntry.grid(row=5,column=1,sticky='E')
                
        # ======= Course Name ==========
                courseLb1=Label(DataEntryFrame,text="Course Name:", bg='green', fg='white', font=('times new roman',15,'bold'))
                courseLb1. grid(row=6,column=0,sticky='W', pady=10)
                
                courseEntry=Entry(DataEntryFrame , textvariable=self.course_name_var,font=('Times New Roman',15))
                courseEntry.grid(row=6,column=1,sticky='E')
                
        # ======= Fee ==========
                FeeLb1=Label(DataEntryFrame,text="Fee:", bg='green', fg='white', font=('times new roman',15,'bold'))
                FeeLb1.grid(row=7,column=0,sticky='W', )

                FeeEntry=Entry(DataEntryFrame,textvariable=self.fee_var,font=('Times New Roman',15))
                FeeEntry.grid(row=7,column=1,sticky='E')
                
        # ======= Institution ==========
                InstitutionLb1=Label(DataEntryFrame,text="Institute:", bg='green', fg='white', font=('times new roman',15,'bold'))
                InstitutionLb1.grid(row=8,column=0,sticky='W',pady=10)
                
                InstitutionEntry=Entry(DataEntryFrame,textvariable=self.institute_var,font=('Times New Roman',15))
                InstitutionEntry.grid(row=8,column=1,sticky='E')
                
        # ======= Qualification ==========
                QualificationLb1=Label(DataEntryFrame,text="Qualification:", bg='green', fg='white', font=('times new roman',15,'bold'))
                QualificationLb1.grid(row=9,column=0,sticky='W',)

                QualificationEntry=Entry(DataEntryFrame,textvariable=self.qualification_var,font=('Times New Roman',15))
                QualificationEntry.grid(row=9,column=1,sticky='E')
                
        # ======= Location ==========
                LocationLb1=Label(DataEntryFrame,text="Location:",bg='green', fg='white', font=('times new roman',15,'bold'))
                LocationLb1. grid(row=10,column=0,sticky='W', pady=10)

                LocationEntry=Entry(DataEntryFrame,textvariable=self.location_var,font=('Times New Roman',15))
                LocationEntry.grid(row=10,column=1,sticky='E')


        #      ============= Buttons ===============
                
                btn_frame = Frame(DataEntryFrame, bd=4, relief=GROOVE, bg='green')
                btn_frame.place (x=10,y=510, width=370, height=50)
                
                btn_add = Button(btn_frame, command=self.adding_data, text='Add', font=('time new roman', 12,'bold'),width=7,bg='blue',fg='white')
                btn_add.grid(row=0, column=0, padx=5, pady=6)
                
                updateBtn = Button(btn_frame, command=self.update_data,text='Update', font=('time new roman', 12,'bold'),width=7,bg='yellow',fg='red')
                updateBtn.grid(row=0, column=1,padx=5, pady=6)
                
                deleteBtn=Button(btn_frame, command=self.delete_data,text='Delete', font=('time new roman', 12,'bold'),width=7,bg='red',fg='white')
                deleteBtn.grid(row=0, column=2,padx=5, pady=6)
                
                clearBtn = Button(btn_frame, command=self.clear, text='Clear', font=('time new roman', 12,'bold'),width=7,bg='pink',fg='white')
                clearBtn.grid(row=0, column=3,padx=5, pady=6)

                # ===================== # DataDisplayFrame # ====================================
                
                DataDisplayFrame = Frame(self.root, bg='green', bd=5, relief=GROOVE)
                DataDisplayFrame.place(x=420, y=60, width=980, height=630)

                lb1_search = Label(DataDisplayFrame, text='Search By', width=15,bg='green',fg='white',font=('time new roman',13,'bold'))
                lb1_search.grid(row=0, column=0, padx=20, pady=15)

                combo_search = ttk.Combobox(DataDisplayFrame,textvariable=self.searchby,font=('times new roman',13,'bold'),width=15)
                combo_search['values']=('qualification','Institute','Location')
                combo_search.grid(row=0,column=1,sticky='W')

                txt_search = Entry(DataDisplayFrame,textvariable=self.searchtxt,font=('times new roman',13,'bold'),width=15)
                txt_search.grid(row=0,column=2,padx=40)

                btnSearch =Button(DataDisplayFrame,command=self.search_data,text='Search',bg='blue',fg='white',font=('times new roman',13,'bold'),width=10)
                btnSearch.grid(row=0,column=3)

                btnShowall = Button(DataDisplayFrame,command=self.fetch_data,text='Show All',bg='yellow',fg='red',font=('times new roman',13,'bold'),width=10)
                btnShowall.grid(row=0,column=4,padx=30)

                                # =========================Table Frame ===================================

                table_frame = Frame(DataDisplayFrame,bd=5,relief=GROOVE)
                table_frame.place(x=10,y=60,width=950,height=550)

                self.Student_Table = ttk.Treeview(table_frame,columns=('roll_no','first_name','last_name','email','mobile','course_name','fee','institute','qualification','location'))

                self.Student_Table.heading('roll_no',text='Roll No')
                self.Student_Table.heading('first_name',text='First Name')
                self.Student_Table.heading('last_name',text='Last Name')
                self.Student_Table.heading('email',text='Email')
                self.Student_Table.heading('mobile',text='Mobile')
                self.Student_Table.heading('course_name',text='Course Name')
                self.Student_Table.heading('fee',text='Fee')
                self.Student_Table.heading('institute',text='Institute')
                self.Student_Table.heading('qualification',text='Quelification')
                self.Student_Table.heading('location',text='Location')

                self.Student_Table['show']='headings'

                self.Student_Table.column('roll_no',width=70,anchor=CENTER)
                self.Student_Table.column('first_name',width=100,anchor=CENTER)
                self.Student_Table.column('last_name',width=100,anchor=CENTER)
                self.Student_Table.column('email',width=130,anchor=CENTER)
                self.Student_Table.column('mobile',width=100,anchor=CENTER)
                self.Student_Table.column('course_name',width=100,anchor=CENTER)
                self.Student_Table.column('fee',width=80,anchor=CENTER)
                self.Student_Table.column('institute',width=70,anchor=CENTER)
                self.Student_Table.column('qualification',width=80,anchor=CENTER)
                self.Student_Table.column('location',width=90,anchor=CENTER)

                self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)
                self.Student_Table.pack()
                self.fetch_data()

        def adding_data(self):
              connection = pymysql.connect(host='localhost', user='root', password='root', db='softwaredb')
              cursor = connection.cursor()
              cursor.execute('insert into softwarestudentsinto values(%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)',
                           (self.roll_no_var.get(),
                           self.first_name_var.get(),
                           self.last_name_var.get(),
                           self.email_var.get(),
                           self.mobile_var.get(),
                           self.course_name_var.get(),
                           self.fee_var.get(),
                           self.institute_var.get(),
                           self.qualification_var.get(),
                           self.location_var.get(),
                           ))
              connection.commit()
              self.fetch_data()
              self.clear()
              connection.close()

            
        def fetch_data(self):
               connection = pymysql.connect(host='localhost', user='root', password='root', db='softwaredb')
               cursor = connection.cursor()
               cursor.execute('select * from softwarestudentsinto') 
               rows = cursor.fetchall()
               if len(rows) != 0:
                      self.Student_Table.delete(*self.Student_Table.get_children())
                      for row in rows:
                             self.Student_Table.insert('',END,values=row)
                      connection.commit()
               connection.close()  

        def clear(self):
                self.roll_no_var.set('')
                self.first_name_var.set('')
                self.last_name_var.set('')
                self.email_var.set('')
                self.mobile_var.set('')
                self.course_name_var.set('')
                self.fee_var.set('')
                self.institute_var.set('')
                self.qualification_var.set('')
                self.location_var.set('')

        def get_cursor(self,var):
               
               cursor_row = self.Student_Table.focus()
               content =self.Student_Table.item(cursor_row)
               row = content['values']
               self.roll_no_var.set(row[0])
               self.first_name_var.set(row[1])
               self.last_name_var.set(row[2])
               self.email_var.set(row[3])
               self.mobile_var.set(row[4])
               self.course_name_var.set(row[5])
               self.fee_var.set(row[6])
               self.institute_var.set(row[7])
               self.qualification_var.set(row[8])
               self.location_var.set(row[9])

        def update_data(self):
               connection = pymysql.connect(host='localhost', user='root', password='root', db='softwaredb')
               cursor = connection.cursor()
               cursor.execute('update softwarestudentsinto set first_name=%s, last_name=%s, emaile=%s, mobile=%s, coursename=%s, fee=%s, institution=%s, qualification=%s, location=%s where roll_no=%s',
                              (self.first_name_var.get(),
                              self.last_name_var.get(),
                              self.email_var.get(),
                              self.mobile_var.get(),
                              self.course_name_var.get(),
                              self.fee_var.get(),
                              self.institute_var.get(),
                              self.qualification_var.get(),
                              self.location_var.get(),
                              self.roll_no_var.get()))
               connection.commit()
               self.fetch_data()
               self.clear()
               connection.close()

        def delete_data(self):
               connection = pymysql.connect(host='localhost', user='root', password='root', db='softwaredb')
               cursor = connection.cursor()
               cursor.execute('delete from softwarestudentsinto where roll_no=%s', self.roll_no_var.get())
               connection.commit()
               self.fetch_data()
               self.clear()
               connection.close()

        def search_data(self):
              connection = pymysql.connect(host='localhost', user='root', password='root', db='softwaredb')
              cursor = connection.cursor()
              cursor.execute("select * from softwarestudentsinto "
                             "where "+str(self.searchby.get())+" like '%"+str(self.searchtxt.get())+"%'")
              rows = cursor.fetchall()

              if len(rows) != 0:
                      self.Student_Table.delete(*self.Student_Table.get_children())
                      for row in rows:
                             self.Student_Table.insert('',END,values=row)
                      connection.commit()
              connection.close()
             
          
               

                
               


root = Tk()
obj = NTHStudentsData(root)
root.mainloop()

