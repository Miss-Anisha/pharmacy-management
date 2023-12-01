from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

    #=====================Add Medicine variable===================
        self.refMed_var=StringVar()
        self.addmed_var=StringVar()

        lbltitle=Label(self.root,text="Pharamacy Management System",bd=15,relief=RIDGE,
                       bg='white',fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)
        
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("python/logo.jpg")
        img1 = img1.resize((80, 80))
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=20)
        
        #==================DataFrame=====================
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1440,height=400)

        DataFramerLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                 fg="darkgreen",font=("arial",12,"bold"))
        DataFramerLeft.place(x=0,y=5,width=900,height=350)

        

        #==================ButtonsFrame========================
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1440,height=65)

        #=================MainButton===========================
        btnAddData=Button(ButtonFrame,text="Medicine Add",font=("arial",12,"bold"),width=14,bg="darkgreen",fg="black")
        btnAddData.grid(row=0,column=0)
        
        btnUpdateMed=Button (ButtonFrame, text="Update", font=("arial",13, "bold"), width=14, bg="darkgreen", fg="black")
        btnUpdateMed .grid (row=0,column=1)

        btnDeleteData=Button(ButtonFrame,text="Delete",font=("arial",12,"bold"),width=14,bg="red",fg="black")
        btnDeleteData.grid(row=0,column=2)

        btnResetData=Button(ButtonFrame,text="Reset",font=("arial",12,"bold"),width=14, bg="darkgreen",fg="black")
        btnResetData.grid(row=0,column=3)

        btnExitData=Button(ButtonFrame,text="Exit",font=("arial",12,"bold"),width=14, bg="darkgreen",fg="black")
        btnExitData.grid(row=0,column=4)

        #================Search by============================
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search by",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)
        
        serch_combo=ttk.Combobox(ButtonFrame,width=12,font=("arial",17,"bold"),state="readonly")
        serch_combo["values"]=("Ref","Medname","Lot")
        serch_combo.grid(row=0,column=6)
        serch_combo.current(0)

        txtSerch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSerch.grid(row=0,column=7)

        serchBtn=Button(ButtonFrame,text="SEARCH",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="black")
        serchBtn.grid(row=0,column=8)
        
        showAll=Button(ButtonFrame,text="SHOW ALL",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="black")
        showAll.grid(row=0,column=9)


        #========================Lables and Entry==========================
        lblrefno=Label(DataFramerLeft, font=("arial",12, "bold"), text="Reference No", padx=2,)
        lblrefno.grid (row=0, column=0, sticky=W )
        
        ref_combo=ttk.Combobox(DataFramerLeft,width=27,font=("arial",12,"bold"),state="readonly")
        ref_combo["values"]=("Ref","Medname","Lot")
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)

        lblCmpName=Label(DataFramerLeft,font=("arial",12,"bold"),text="Company Name:",padx=2,pady=6)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFramerLeft,font=("arial",13,"bold"),bg="black",bd=2,relief=RIDGE,width=29)
        txtCmpName.grid(row=1,column=1)
        
        lblTypeofMedicine=Label(DataFramerLeft,font=("arial",12,"bold"),text="Type of Medicine:",padx=2,pady=6)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)

        comTypeofMedicine=ttk.Combobox(DataFramerLeft,state="readonly",
                                     font=("arial",12,"bold"),width=27)
        comTypeofMedicine['value']=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injections",)
        comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row=2,column=1)


        #===================Add Medicine==============================


        lblMedicineName=Label(DataFramerLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)
        
        comMedicineName=ttk.Combobox(DataFramerLeft,state="readonly",
                                     font=("arial",12,"bold"),width=27)
        comMedicineName['value']=("nice","novel")
        comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)
        
        lblLotNo=Label(DataFramerLeft,font=("arial",12,"bold"),text="Lot No:",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFramerLeft,font=("arial",13,"bold"),bg="black",bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)
        
        
        lblIssueDate=Label(DataFramerLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFramerLeft,font=("arial",13,"bold"),bg="black",bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=5,column=1)
        
        lblExDate=Label(DataFramerLeft,font=("arial",12,"bold"),text="Expiry Date:",padx=2,pady=6)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFramerLeft,font=("arial",13,"bold"),bg="black",bd=2,relief=RIDGE,width=29)
        txtExDate.grid(row=6,column=1)
        
        lblUses=Label(DataFramerLeft,font=("arial",12,"bold"),text="Uses:",padx=2,pady=6)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFramerLeft,font=("arial",13,"bold"),bg="black",bd=2,relief=RIDGE,width=29)
        txtUses.grid(row=7,column=1)
        
        
        lblSideEffect=Label(DataFramerLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFramerLeft,font=("arial",13,"bold"),bg="black",bd=2,relief=RIDGE,width=29)
        txtSideEffect.grid(row=8,column=1)
        
        lblPreWarning=Label(DataFramerLeft,font=("arial",12,"bold"),text="Prec&Warning:",padx=2,pady=6)
        lblPreWarning.grid(row=0,column=2,sticky=W)
        txtPreWarning=Entry(DataFramerLeft,font=("arial",13,"bold"),bg="black",bd=2,relief=RIDGE,width=29)
        txtPreWarning.grid(row=0,column=3)
        
        
        lblDosage=Label(DataFramerLeft,font=("arial",12,"bold"),text="Dosage:",padx=2,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFramerLeft,font=("arial",13,"bold"),bg="black",bd=2,relief=RIDGE,width=29)
        txtDosage.grid(row=1,column=3)
        
        
        lblPrice=Label(DataFramerLeft,font=("arial",12,"bold"),text="Tablets Price:",padx=2,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFramerLeft,font=("arial",13,"bold"),bg="black",bd=2,relief=RIDGE,width=29)
        txtPrice.grid(row=2,column=3)
        
        
        lblProductQt=Label(DataFramerLeft,font=("arial",12,"bold"),text="Product QT:",padx=2,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W )
        txtProductQt=Entry(DataFramerLeft,font=("arial",13,"bold"),bg="black",bd=2,relief=RIDGE,width=29)
        txtProductQt.grid(row=3,column=3,sticky=W)

        #=====================Images==========================
        lblhome=Label(DataFramerLeft,font=("arial",12,"bold"),text="Stay Home Stay Home",padx=2,pady=6,bg="black",fg="red",width=37  )
        lblhome.place(x=500,y=140)

        img2=Image.open("python/img4.jpg")
        img2 = img2.resize((150, 135))
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=770,y=330)

        img3=Image.open("python/img5.jpg")
        img3 = img3.resize((150, 135))
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=620,y=330)

        img4=Image.open("python/images.jpeg")
        img4 = img4.resize((150, 135))
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=475,y=330)

       #====================DataFrameRight=====================
       
        DataFramerRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department ",
                                   fg="darkgreen",font=("arial",12,"bold"))
        DataFramerRight.place(x=910,y=5,width=540,height=350)

        img5=Image.open("python/img2.jpg")
        img5=img5. resize((200,75))
        self. photoimg5=ImageTk. PhotoImage (img5)
        b1=Button(self.root, image=self. photoimg5, borderwidth=0)
        b1. place (x=960,y=160)


        img6=Image.open("python/img3.jpeg")
        img6=img6. resize((200,75))
        self. photoimg6=ImageTk. PhotoImage (img6)
        b1=Button(self.root, image=self. photoimg6, borderwidth=0)
        b1. place (x=1160,y=160)
        
       

        lblrefno=Label(DataFramerRight,font=("arial",12,"bold"),text="Reference No:")
        lblrefno.place(x=0,y=80)
        txtrefno=Entry(DataFramerRight,textvariable=self.refMed_var,font=("arial",15,"bold"),bd=2,relief=RIDGE,width=14)
        txtrefno.place(x=135,y=80)

        lblmedName=Label(DataFramerRight,font=("arial",12,"bold"),text="Medicine Name:")
        lblmedName.place(x=0,y=110)
        txtmedName=Entry(DataFramerRight,textvariable=self.addmed_var,font=("arial",15,"bold"),bg="black",bd=2,relief=RIDGE,width=14)
        txtmedName.place(x=135,y=110)


        #=========================side frame=========================

        side_frame=Frame(DataFramerRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)
        
        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")
        
        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname", width=100)

        #====================Medicine Add Button====================
        down_frame=Frame(DataFramerRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=150,width=135,height=160)

        btnAddmed=Button(down_frame,text="Add",font=("arial",12,"bold"),width=12,bg="lime",fg="black",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="UPDATE",font=("arial",12,"bold"),width=12,bg="purple",fg="black",pady=4)
        btnUpdatemed.grid(row=1,column=0)
        
        btnDeletemed=Button(down_frame,text="DELETE",font=("arial",12,"bold"),width=12,bg="red",fg="black",pady=4)
        btnDeletemed.grid(row=2,column=0)
        
        btnClearmed=Button(down_frame,text="CLEAR",font=("arial",12,"bold"),width=12,bg="orange",fg="black",pady=4)
        btnClearmed.grid(row=3,column=0)



        #======================Frame details=========================
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1445,height=195 )


        #===================Main Table and Scrollbar==================
        Table_frame=Frame (Framedetails, bd=15, relief=RIDGE, padx=20)
        Table_frame. place (x=0,y=1,width=1500,height=180)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("reg","companyname","type","tabletname","lotno","issuedate","expdate","uses","sideeffect","warning","dosage","price","productqt")
                                         ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"
        
        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Expiry Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product QTs")
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        
        
         
        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        
        #====================Add Medicine Functionality declaration====================

    def AddMed(self):
        conn=mysql.connector.connect(host="127.0.01:3306",username="anisha",password="Anisha*#98",database="data")
        my_cursor=conn.cursor() 
        try:
            
            my_cursor.execute("INSERT INTO pharma(Ref,MedName) VALUES(%s,%s)",(
                                                                        self.refMed_var.get(),
                                                                        self.Addmed_var.get()
                                                    ))
            
            messagebox.showinfo("success","Medicine Added")
            conn.commit()
            conn.close()
        except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

             

        
        










if __name__ == "__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()