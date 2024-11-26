from tkinter import*
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from sales import salesClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("HEALTH + | Developed by Devashish Das")
        self.root.config(bg="white")
        #===title====
        title=Label(self.root,text="HEALTH +",font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===btn_logout===
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=30,width=150)
        #===clock=====
        self.b1_clock=Label(self.root,text="Welcome to HEALTH + Website\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.b1_clock.place(x=0,y=70,relwidth=1,height=30)
        #===Left Menu==
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        b1_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #===content===
        self.b1_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="yellow",fg="white",font=("goudy old style",20,"bold"))
        self.b1_employee.place(x=300,y=120,height=150,width=300)

        self.b1_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.b1_supplier.place(x=650,y=120,height=150,width=300)

        self.b1_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.b1_category.place(x=1000,y=120,height=150,width=300)


        
        self.b1_sale=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.b1_sale.place(x=300,y=300,height=150,width=300)



        #===footer====
        b1_footer=Label(self.root,text="Welcome to HEALTH + | Developed by Devashish in 2024\nFor any Technical Issue Contact: 9907898725",font=("times new roman",15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
#====================================================================================================================

    def employee(self):
        self.new_win= Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win= Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win= Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def sales(self):
        self.new_win= Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

if __name__ =="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
