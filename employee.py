from tkinter import *
from tkinter import messagebox,ttk
import pymysql  # pip install mysql
import time
import os
import tempfile
class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Managemnt System")    
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="white")
        title=Label(self.root, text="Employee Payroll Management System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.root, text="All Employees",command=self.employee_frame, font=("times new roman",13,"bold"),bg="grey",fg="white").place(x=1110,y=10,width=130,height=30)
     # =================frame 1=================================================================
       #-------variables--------
        self.var_emp_code=StringVar()
        self.var_emp_designation=StringVar()
        self.var_emp_name=StringVar()
        self.var_emp_age=StringVar()
        self.var_emp_gender=StringVar()
        self.var_emp_email=StringVar()
        self.var_emp_qualification=StringVar()
        self.var_emp_dob=StringVar()
        self.var_emp_experience=StringVar()
        self.var_emp_proof_id=StringVar()   #aadhar card
        self.var_emp_doj=StringVar()
        self.var_emp_contact_no=StringVar()
        self.var_emp_address=StringVar()


        frame1=Frame(self.root, bd=5, relief=RIDGE,bg="white")
        frame1.place(x=10,y=70,width=750,height=620)
        title=Label(frame1, text="Employee Details",font=("times new roman",20),bg="darkgrey",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
       
        lb1=Label(frame1, text="Employee Id",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=70)
        self.txt_id=Entry(frame1, font=("times new roman",15,"bold"),textvariable=self.var_emp_code,bg="lightyellow",fg="black")
        self.txt_id.place(x=170,y=70,width=200)
        btn_search=Button(frame1, text="Search",command=self.search, font=("times new roman",15,"bold"),bg="hotpink",fg="black").place(x=500,y=70,width=170,height=30)
        #==========row1===========================
        designation=Label(frame1, text="Designation",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=120)
        txt_disignation=Entry(frame1, font=("times new roman",15,"bold"),textvariable=self.var_emp_designation,bg="lightyellow",fg="black").place(x=170,y=125,width=200)
        
        DOB=Label(frame1, text="D.O.B",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=390,y=120)
        txt_DOB=Entry(frame1, font=("times new roman",15,"bold"),textvariable=self.var_emp_dob,bg="lightyellow",fg="black").place(x=500,y=125,width=200)
      
       # ==========row2 ============================
        DOJ =Label(frame1, text="D.O.J",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=170)
        txt_DOJ=Entry(frame1, font=("times new roman",15,"bold"),textvariable=self.var_emp_doj,bg="lightyellow",fg="black").place(x=170,y=175,width=200)
        
        DOB=Label(frame1, text="Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=390,y=170)
        txt_name=Entry(frame1, font=("times new roman",15,"bold"),textvariable=self.var_emp_name,bg="lightyellow",fg="black").place(x=500,y=175,width=200)

        # ========row 3===================

        age =Label(frame1, text="Age",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=220)
        txt_age=Entry(frame1, font=("times new roman",15,"bold"),textvariable=self.var_emp_age,bg="lightyellow",fg="black").place(x=170,y=225,width=200)
        
        experience=Label(frame1, text="Experience",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=390,y=220)
        txt_experience=Entry(frame1, font=("times new roman",15,"bold"),textvariable=self.var_emp_experience,bg="lightyellow",fg="black").place(x=500,y=225,width=200)

       # ===========row4============

        gender =Label(frame1, text="Gender",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=270)
        txt_gender=Entry(frame1, font=("times new roman",15,"bold"),textvariable=self.var_emp_gender,bg="lightyellow",fg="black").place(x=170,y=275,width=200)
        
        Proofid=Label(frame1, text="Proof Id",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=390,y=270)
        txt_proofid=Entry(frame1, font=("times new roman",15,"bold"),textvariable=self.var_emp_proof_id,bg="lightyellow",fg="black").place(x=500,y=275,width=200)

       #======row 5==========
        Email=Label(frame1, text="Email",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=320)
        txt_email=Entry(frame1, font=("times new roman",15,"bold"),textvariable=self.var_emp_email,bg="lightyellow",fg="black").place(x=170,y=325,width=200)
        
        contact=Label(frame1, text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=390,y=320)
        txt_contact=Entry(frame1, font=("times new roman",15,"bold"),textvariable=self.var_emp_contact_no,bg="lightyellow",fg="black").place(x=500,y=325,width=200)
      # ===========row 6==============
        qualification =Label(frame1, text="Qualification",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=370)
        txt_qual=Entry(frame1, font=("times new roman",15,"bold"),textvariable=self.var_emp_qualification,bg="lightyellow",fg="black").place(x=170,y=375,width=440,height=50)
       #========row 7========= 
        address=Label(frame1, text="Address",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=445)
        txt_address=Entry(frame1, font=("times new roman",15,"bold"),textvariable=self.var_emp_address,bg="lightyellow",fg="black").place(x=170,y=450,width=440,height=80)





     #==================frame2 =================================================================
     #-----------variables--------------

        self.var_emp_month=StringVar()
        self.var_emp_year=StringVar()
        self.var_emp_basicpay=StringVar()
        self.var_emp_totaldays=StringVar()
        self.var_emp_absent=StringVar()
        self.var_emp_present=StringVar()
        self.var_emp_bonus=StringVar()
        self.var_emp_netsalary=StringVar()
        
        frame2=Frame(self.root, bd=5, relief=RIDGE,bg="white")
        frame2.place(x=770,y=70,width=580,height=300)

        
        title2=Label(frame2, text="Employee Salary Details",font=("times new roman",20),bg="darkgrey",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

         #==========row1===========================
        month=Label(frame2, text="Month",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=50)
        txt_month=Entry(frame2, font=("times new roman",15,"bold"),textvariable=self.var_emp_month,bg="lightyellow",fg="black").place(x=90,y=50,width=100)
        
        year=Label(frame2, text="Year",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=190,y=50)
        txt_year=Entry(frame2, font=("times new roman",15,"bold"),textvariable=self.var_emp_year,bg="lightyellow",fg="black").place(x=240,y=50,width=100)
      
        basicpay=Label(frame2, text="Basic Pay",font=("times new roman",13,"bold"),bg="white",fg="black").place(x=350,y=50)
        txt_basicpay=Entry(frame2, font=("times new roman",15,"bold"),textvariable=self.var_emp_basicpay,bg="lightyellow",fg="black").place(x=430,y=50,width=100)
       # ==========row2 ============================
        totaldays =Label(frame2, text="Total Days",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=90)
        txt_totaldays=Entry(frame2, font=("times new roman",15,"bold"),textvariable=self.var_emp_totaldays,bg="lightyellow",fg="black").place(x=120,y=95,width=120)
        
        Absents=Label(frame2, text="Absents",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=90)
        txt_absents=Entry(frame2, font=("times new roman",15,"bold"),textvariable=self.var_emp_absent,bg="lightyellow",fg="black").place(x=350,y=95,width=120)

        # ========row 3===================

        Presents =Label(frame2, text="Presents",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=130)
        txt_present=Entry(frame2, font=("times new roman",15,"bold"),textvariable=self.var_emp_present,bg="lightyellow",fg="black").place(x=120,y=135,width=120)
        
        Bonus=Label(frame2, text="Bonus",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=130)
        txt_bonus=Entry(frame2, font=("times new roman",15,"bold"),textvariable=self.var_emp_bonus,bg="lightyellow",fg="black").place(x=350,y=135,width=120)

       # ===========row4============

        netsalary =Label(frame2, text="Net Salary",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=170)
        txt_netsalary=Entry(frame2, font=("times new roman",15,"bold"),textvariable=self.var_emp_netsalary,bg="lightyellow",fg="black")
        txt_netsalary.place(x=120,y=175,width=150,)
        
        self.btn_save=Button(frame2, text="Save",command=self.add, font=("times new roman",15,"bold"),bg="yellow",fg="black")
        self.btn_save.place(x=10,y=220,width=90,height=30)
        btn_reset=Button(frame2, text="Reset",command=self.clear, font=("times new roman",15,"bold"),bg="lightgreen",fg="black").place(x=110,y=220,width=90,height=30)
        btn_Calculate=Button(frame2, text="Calculate",command=self.calculate, font=("times new roman",15,"bold"),bg="lightblue",fg="black").place(x=210,y=220,width=90,height=30)
        self.btn_Update=Button(frame2, text="Update",state=DISABLED,command=self.update, font=("times new roman",15,"bold"),bg="lightgrey",fg="black")
        self.btn_Update.place(x=310,y=220,width=90,height=30)
        self.btn_delete=Button(frame2, text="Delete",state=DISABLED,command=self.delete, font=("times new roman",15,"bold"),bg="red",fg="black")
        self.btn_delete.place(x=410,y=220,width=90,height=30)
        
     # ================frame3 ==================================================================
        frame3=Frame(self.root, bd=5, relief=RIDGE,bg="white")
        frame3.place(x=770,y=380,width=580,height=310)

        #======calculator=====
        self.var_text=StringVar()
        self.var_operator=''
        def btn_click(num):
              self.var_operator=self.var_operator+str(num)
              self.var_text.set(self.var_operator)
              print(num)

        def result():
              res=str(eval(self.var_operator))
              self.var_text.set(res)
              self.var_operator='' 

        def clear_cal():
              self.var_text.set('')
              self.var_operator=''           

        cal_frame=Frame(frame3,bg="white",bd=2,relief=RIDGE)
        cal_frame.place(x=2,y=2,width=215,height=300)
        calculator=Label(cal_frame, text="Calculator",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=22,y=5)
        txt_result=Entry(cal_frame,bg='lightyellow',textvariable=self.var_text,font=('times new roman',15,"bold"),justify=RIGHT).place(x=0,y=50,relwidth=1,height=45)
        # row 1
        btn_7=Button(cal_frame,text='7',command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=3,y=95,width=50,height=50)
        btn_8=Button(cal_frame,text='8',command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=55,y=95,width=50,height=50)
        btn_9=Button(cal_frame,text='9',command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=105,y=95,width=50,height=50)
        btn_divide=Button(cal_frame,text='/',command=lambda:btn_click('/'),font=("times new roman",15,"bold")).place(x=157,y=95,width=50,height=50)

        # row 2
        btn_4=Button(cal_frame,text="4",command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=3,y=145,width=50,height=50)
        btn_5=Button(cal_frame,text="5",command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=55,y=145,width=50,height=50)
        btn_6=Button(cal_frame,text="6",command=lambda:btn_click(6),font=("times new roman",15,"bold")).place(x=105,y=145,width=50,height=50)
        btn_multiply=Button(cal_frame,text="*",command=lambda:btn_click('*'),font=("times new roman",15,"bold")).place(x=157,y=145,width=50,height=50)
        

        # row 3
        btn_1=Button(cal_frame,text="1",command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=3,y=195,width=50,height=50)
        btn_2=Button(cal_frame,text="2",command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=55,y=195,width=50,height=50)
        btn_3=Button(cal_frame,text="3",command=lambda:btn_click(3),font=("times new roman",15,"bold")).place(x=105,y=195,width=50,height=50)
        btn_minus=Button(cal_frame,text="-",command=lambda:btn_click('-'),font=("times new roman",15,"bold")).place(x=157,y=195,width=50,height=50)
       
        # row 4
        btn_0=Button(cal_frame,text="0",command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=3,y=245,width=50,height=50)
        btn_plus=Button(cal_frame,text="+",command=lambda:btn_click('+'),font=("times new roman",15,"bold")).place(x=55,y=245,width=50,height=50)
        btn_clear=Button(cal_frame,text="C",command=clear_cal,font=("times new roman",15,"bold")).place(x=105,y=245,width=50,height=50)
        btn_equal=Button(cal_frame,text="=",command=result,font=("times new roman",15,"bold")).place(x=157,y=245,width=50,height=50)
       
       #==========salary reciept frame====================

        sal_frame=Frame(frame3,bg="white",bd=2,relief=RIDGE)
        sal_frame.place(x=220,y=2,width=350,height=300)
        title2=Label(sal_frame, text="Salary Reciept",font=("times new roman",20),bg="darkgrey",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        sal_frame2=Frame(sal_frame,bg='white',bd=2,relief=RIDGE)
        sal_frame2.place(x=0,y=36,relwidth=1,height=225)
        
        # salary reciept
        self.sample=f'''
    \tCompany Name, XYZ\n\tAddress : xyz
    ----------------------------------------
    Employee ID\t\t: 
    Salary of\t\t: MM-YYYY
    Generated on\t\t: DD-MM-YYYY
    ----------------------------------------
    Total Days\t\t: DD
    Total Present\t\t: DD
    Total Absent\t\t:  DD
    Bonus\t\t:  Rs.------
    Basic Pay\t\t: Rs----
    Net Salary\t\t: Rs. -----
    ----------------------------------------
    This is computer generated slip, not required any Signature
        '''
        
        scroll_y=Scrollbar(sal_frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_reciept=Text(sal_frame2,font=("times new roman",13),bg='lightyellow',yscrollcommand=scroll_y.set)
        self.txt_salary_reciept.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_reciept.yview)
        self.txt_salary_reciept.insert(END,self.sample)

        #print button
        self.btn_print=Button(sal_frame, text="Print",state=DISABLED,command=self.print, font=("times new roman",15,"bold"),bg="lightpink",fg="black")
        self.btn_print.place(x=190,y=265,width=120,height=30)

        self.check_connection()
        
        #============ALL FUNCTIONS DEFINED HERE===========
    def search(self): 
         try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
            rows=cur.fetchone()
            #print(rows)
            if rows ==None:
                 messagebox.showerror("Error","Invalid Employee Id.Please try with another ID",parent=self.root)
            else:
                 print(rows)
                 self.var_emp_code.set(rows[0]) 
                 self.var_emp_designation.set(rows[1]) 
                 self.var_emp_doj.set(rows[2]) 
                 self.var_emp_age.set(rows[3]) 
                 self.var_emp_gender.set(rows[4])   
                 self.var_emp_email.set(rows[5])                    
                 self.var_emp_dob.set(rows[6]) 
                 self.var_emp_name.set(rows[7])                    
                 self.var_emp_experience.set(rows[8]) 
                 self.var_emp_proof_id.set(rows[9])                          
                 self.var_emp_contact_no.set(rows[10]) 
                 self.var_emp_qualification.set(rows[11]) 
                 self.var_emp_address.set(rows[12])
                 self.var_emp_month.set(rows[13]) 
                 self.var_emp_year.set(rows[14]) 
                 self.var_emp_basicpay.set(rows[15]) 
                 self.var_emp_totaldays.set(rows[16]) 
                 self.var_emp_absent.set(rows[17])   
                 self.var_emp_present.set(rows[18]) 
                 self.var_emp_bonus.set(rows[19]) 
                 self.var_emp_netsalary.set(rows[20]) 
                 file=open('salary_reciept/'+str(rows[21]),'r')
                 self.txt_salary_reciept.delete('1.0',END)
                 for i in file:
                     self.txt_salary_reciept.insert(END,i)
                 file.close()
                 self.btn_save.config(state=DISABLED)
                 self.btn_Update.config(state=NORMAL)
                 self.btn_delete.config(state=NORMAL)
                 self.txt_id.config(state="readonly")
                 self.btn_print.config(state=NORMAL)
                
                 


         except Exception as ex:
             messagebox.showerror("error",f'error due to :{str(ex)}')
   #clear function
    def clear(self):
                 self.btn_save.config(state=NORMAL)
                 self.btn_Update.config(state=DISABLED)
                 self.btn_delete.config(state=DISABLED)
                 self.btn_print.config(state=DISABLED)
                 self.txt_id.config(state=NORMAL)
                 self.var_emp_code.set('') 
                 self.var_emp_designation.set('') 
                 self.var_emp_doj.set('') 
                 self.var_emp_age.set('') 
                 self.var_emp_gender.set('')   
                 self.var_emp_email.set('')                    
                 self.var_emp_dob.set('') 
                 self.var_emp_name.set('')                    
                 self.var_emp_experience.set('') 
                 self.var_emp_proof_id.set('')                          
                 self.var_emp_contact_no.set('') 
                 self.var_emp_qualification.set('') 
                 self.var_emp_address.set('')
                 self.var_emp_month.set('') 
                 self.var_emp_year.set('') 
                 self.var_emp_basicpay.set('') 
                 self.var_emp_totaldays.set('') 
                 self.var_emp_absent.set('')   
                 self.var_emp_present.set('') 
                 self.var_emp_bonus.set('') 
                 self.var_emp_netsalary.set('') 
                 self.txt_salary_reciept.delete('1.0',END)
                 self.txt_salary_reciept.insert(END,self.sample)
  
  
    # delete function
   
    def delete(self): 
     if self.var_emp_code.get()=='':
            messagebox.showerror("Error","Employee ID is required")
     else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
            rows=cur.fetchone()
            #print(rows)
            if rows ==None:
                 messagebox.showerror("Error","Invalid Employee Id.Please try with another ID",parent=self.root),
            else:
                op=messagebox.askyesno("confirm","Do you really want to delete ?")
                if op==True:
                 cur.execute("delete from emp_salary where e_id=%s",(self.var_emp_code.get()))
                 con.commit()
                 con.close()
                 messagebox.showinfo("SUCCESS","Employee Record Deleted Successfully!!")
                 self.clear()                  


        except Exception as ex:
             messagebox.showerror("error",f'error due to :{str(ex)}')


    def add(self):
       if self.var_emp_code.get()=='' or self.var_emp_netsalary.get()=='' or self.var_emp_name.get()=='':
            messagebox.showerror("Error","Employee Details are required")
       else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
            rows=cur.fetchone()
            #print(rows)
            if rows !=None:
                 messagebox.showerror("Error","This Employee ID is already available.Please try with an another id",parent=self.root),
            else:
                  cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                  (
                       
                   self.var_emp_code.get(),
                   self.var_emp_designation.get(),
                   self.var_emp_doj.get(),
                   self.var_emp_age.get(),
                   self.var_emp_gender.get(),  
                   self.var_emp_email.get(),                   
                   self.var_emp_dob.get(),
                   self.var_emp_name.get(),                   
                   self.var_emp_experience.get(),
                   self.var_emp_proof_id.get(),                         
                   self.var_emp_contact_no.get(),
                   self.var_emp_qualification.get(),
                   self.var_emp_address.get(),                           
                   self.var_emp_month.get(),
                   self.var_emp_year.get(),
                   self.var_emp_basicpay.get(),
                   self.var_emp_totaldays.get(),
                   self.var_emp_absent.get(),  
                   self.var_emp_present.get(),
                   self.var_emp_bonus.get(),
                   self.var_emp_netsalary.get(),
                   self.var_emp_code.get()+".txt"
                      ))  
            con.commit()
            con.close()
            file=open('salary_reciept/'+str(self.var_emp_code.get())+'.txt',"w")
            file.write(self.txt_salary_reciept.get('1.0',END))
            
            messagebox.showinfo("success","record added successfully")       
            self.btn_print.config(state=NORMAL)
            file.close()                  
                  
        except Exception as ex:
             messagebox.showerror("error",f'error due to :{str(ex)}')

    def update(self):
     if self.var_emp_code.get() == '' or self.var_emp_netsalary.get() == '' or self.var_emp_name.get() == '':
        messagebox.showerror("Error", "Employee Details are required")
     else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='ems')
            cur = con.cursor()
            cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_code.get(),))
            rows = cur.fetchall()

            if not rows:
                messagebox.showerror("Error", "This Employee ID is invalid. Please try with another id", parent=self.root)
            else:
                cur.execute("""
                    UPDATE emp_salary 
                    SET e_designation = %s, e_doj = %s, e_age = %s, e_gender = %s, e_email = %s, e_dob = %s, 
                    e_name = %s, e_experience = %s, e_proofid = %s, e_contact = %s, qualification = %s, 
                    address = %s, month = %s, year = %s, basic_pay = %s, total_days = %s, absents = %s, 
                    present = %s, bonus = %s, net_salary = %s, salary_reciept = %s 
                    WHERE e_id = %s
                """, (
                    self.var_emp_designation.get(),
                    self.var_emp_doj.get(),
                    self.var_emp_age.get(),
                    self.var_emp_gender.get(),
                    self.var_emp_email.get(),
                    self.var_emp_dob.get(),
                    self.var_emp_name.get(),
                    self.var_emp_experience.get(),
                    self.var_emp_proof_id.get(),
                    self.var_emp_contact_no.get(),
                    self.var_emp_qualification.get(),
                    self.var_emp_address.get(),
                    self.var_emp_month.get(),
                    self.var_emp_year.get(),
                    self.var_emp_basicpay.get(),
                    self.var_emp_totaldays.get(),
                    self.var_emp_absent.get(),
                    self.var_emp_present.get(),
                    self.var_emp_bonus.get(),
                    self.var_emp_netsalary.get(),
                    self.var_emp_code.get() + '.txt',
                    self.var_emp_code.get()
                ))

            con.commit()
            con.close()

            file = open('salary_reciept/' + str(self.var_emp_code.get()) + '.txt', "w")
            file.write(self.txt_salary_reciept.get('1.0', END))
            file.close()
            
            messagebox.showinfo("Success", "Record updated successfully")

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')

         

    def calculate(self):
       
        if self.var_emp_month.get()=='' or self.var_emp_year.get()=='' or self.var_emp_code.get()=='' or self.var_emp_basicpay.get()=='' or  self.var_emp_totaldays.get()=='' or self.var_emp_absent.get()=='' or self.var_emp_present.get()=='' or  self.var_emp_bonus.get()=='' :
             messagebox.showerror('Error','All Fields are required')
        else:
            # self.var_net_salary.set("result")
            #35000/31=1752
            #31-10=21*1752
            per_day=int(self.var_emp_basicpay.get())/int(self.var_emp_totaldays.get())
            work_day=int(self.var_emp_totaldays.get())-int(self.var_emp_absent.get())
            sal=per_day*work_day
            addition=int(self.var_emp_bonus.get())
            net_sal=sal+addition
            self.var_emp_netsalary.set(str(round(net_sal,2)))
            
            
            #=====updtae the reciept=====
            new_sample=f'''
    \tCompany Name, XYZ\n\tAddress : xyz
    ----------------------------------------
    Employee ID\t\t: {self.var_emp_code.get()} 
    Salary of\t\t: {self.var_emp_month.get()}-{self.var_emp_year.get()}
    Generated on\t\t: {str(time.strftime("%d-%m-%y"))}
    ----------------------------------------
    Total Days\t\t: {self.var_emp_totaldays.get()}
    Total Present\t\t: {self.var_emp_present.get()}
    Total Absent\t\t: {self.var_emp_absent.get()}
    Bonus\t\t:  Rs.{self.var_emp_bonus.get()}
    Basic Pay\t\t: Rs.{self.var_emp_basicpay.get()}
    Net Salary\t\t: Rs.{self.var_emp_netsalary.get()}
    ----------------------------------------
    This is computer generated slip, not required any Signature
        '''
            self.txt_salary_reciept.delete('1.0',END)
            self.txt_salary_reciept.insert(END,new_sample)
         
             
    

    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            
            # print(rows)

        except Exception as ex:
             messagebox.showerror("error",f'error due to :{str(ex)}')

    def show(self):
         try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
           # print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
              self.employee_tree.insert('',END,values=row)
            con.close()

         except Exception as ex:
             messagebox.showerror("error",f'error due to :{str(ex)}')         
           
    def employee_frame(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Employee Payroll Managemnt System")
        self.root2.geometry("1000x500+120+100")
        self.root2.configure(bg="white")
        self.root2.focus_force()
        title=Label(self.root2, text="All Employee Details",font=("times new roman",30,"bold"),bg="light blue",fg="grey",anchor="w",padx=10).pack(side=TOP,fill=X)
        
        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'e_designation', 'e_doj', 'e_age', 'e_gender', 'e_email', 'e_dob', 'e_name', 'e_experience', 'e_proofid', 'e_contact', 'qualification', 'address', 'month', 'year', 'basic_pay', 'total_days', 'absents', 'present', 'bonus', 'net_salary', 'salary_reciept'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id',text='E_ID')
        self.employee_tree.heading('e_designation',text='DESIGNATION')
        self.employee_tree.heading('e_doj',text='D.O.J')
        self.employee_tree.heading('e_age',text='AGE')
        self.employee_tree.heading('e_gender',text='GENDER')
        self.employee_tree.heading('e_email',text='E-MAIL')
        self.employee_tree.heading('e_dob',text='D.O.B')
        self.employee_tree.heading('e_name',text='NAME')
        self.employee_tree.heading('e_experience',text='EXPERIENCE')
        self.employee_tree.heading('e_proofid',text='PROOF_ID')
        self.employee_tree.heading('e_contact',text='CONTACT_NO')
        self.employee_tree.heading('qualification',text='QUALIFICATION')
        self.employee_tree.heading('address',text='ADDRESS')
        self.employee_tree.heading('month',text='MONTH')
        self.employee_tree.heading('year',text='YEAR')
        self.employee_tree.heading('basic_pay',text='BASIC_PAY')
        self.employee_tree.heading('total_days',text='TOTAL DAYS')
        self.employee_tree.heading('absents',text='ABSENTS')
        self.employee_tree.heading('present',text='PRESENTS')
        self.employee_tree.heading('bonus',text='BONUS')
        self.employee_tree.heading('net_salary',text='NET SALARY')
        self.employee_tree.heading('salary_reciept',text='SALARY_RECIEPT')
        self.employee_tree['show']='headings'
        
        self.employee_tree.column('e_id',width=100)
        self.employee_tree.column('e_designation',width=300)
        self.employee_tree.column('e_doj',width=100)
        self.employee_tree.column('e_age',width=100)
        self.employee_tree.column('e_gender',width=100)
        self.employee_tree.column('e_email',width=200)
        self.employee_tree.column('e_dob',width=100)
        self.employee_tree.column('e_name',width=200)
        self.employee_tree.column('e_experience',width=100)
        self.employee_tree.column('e_proofid',width=180)
        self.employee_tree.column('e_contact',width=180)
        self.employee_tree.column('qualification',width=200)
        self.employee_tree.column('address',width=400)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_pay',width=100)
        self.employee_tree.column('total_days',width=100)
        self.employee_tree.column('absents',width=100)
        self.employee_tree.column('present',width=100)
        self.employee_tree.column('bonus',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_reciept',width=100)

        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()
        
        
        self.root2.mainloop()

    # print command function
    def print(self):

        file=tempfile.mktemp(".txt")
        open(file,'w').write(self.txt_salary_reciept.get('1.0',END) )
        os.startfile(file,'print')   

root=Tk()
obj=EmployeeSystem(root)
root.mainloop()