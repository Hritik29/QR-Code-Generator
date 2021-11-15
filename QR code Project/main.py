from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class QRgenerator():
    def __init__(self,root):

        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generrator | Developed by HRITIK and DEVIPRASAD")
        self.root.resizable(False,False)

        # logo= Image.open("qrimg.png")
        # qwe=ImageTk.PhotoImage(logo)
        
        # qwe=resizeimage.resize_cover(qwe,[1,2])
        
        # logo_lbl=Label(image=test)
        # logo_lbl.image = test
        # logo_lbl.grid(row=1,column=3)
        

        # image1 = Image.open("bgii.jpg")
        # test = ImageTk.PhotoImage(image1)
        # image1=resizeimage.resize_cover(image1,[180,180])

        # label1 =Label(self.root,image=test)
        # label1.image = test

        # Position image
        # label1.grid(columnspan=4)
        title=Label(self.root,text="Student QR Code Generator",font=("Times new roman",40),bg="#053246",fg='white').place(x=0,y=0,relwidth=1)
        
        
#----STUDENT DETAIL Window-----
# ----VARIABLE----
        self.var_student_id=StringVar()
        self.var_name=StringVar()
        self.var_sec=StringVar()
        self.var_batch=StringVar()

        studentFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        studentFrame.place(x=50,y=100,width=500,height=380)

        studentTitle=Label(studentFrame,text="STUDENT DETAILS",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)
        lbl_id=Label(studentFrame,text="Student ID",font=("times new roman",16,'bold'),bg='white').place(x=20,y=60)
        lbl_name=Label(studentFrame,text="Name",font=("times new roman",16,'bold'),bg='white').place(x=20,y=100)
        lbl_sec=Label(studentFrame,text="Section",font=("times new roman",16,'bold'),bg='white').place(x=20,y=140)
        lbl_Year=Label(studentFrame,text="Batch Year",font=("times new roman",16,'bold'),bg='white').place(x=20,y=180)

        txt_id=Entry(studentFrame,font=("times new roman",20),textvariable=self.var_student_id,bg='white').place(x=200,y=60)
        txt_name=Entry(studentFrame,font=("times new roman",20),textvariable=self.var_name,bg='white').place(x=200,y=100)
        txt_sec=Entry(studentFrame,font=("times new roman",20),textvariable=self.var_sec,bg='white').place(x=200,y=140)
        txt_Year=Entry(studentFrame,font=("times new roman",20),textvariable=self.var_batch,bg='white').place(x=200,y=180)

        btn_generate=Button(studentFrame,text="QR Generate",command=self.generate,font=('times new roman',18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=200,height=30) 
        btn_clear=Button(studentFrame,text="Clear",command=self.clear,font=('times new roman',18,'bold'),bg='#607d8b',fg='white').place(x=310,y=250,width=120,height=30)

        self.msg='' 
        self.lbl_msg=Label(studentFrame,text=self.msg,font=("times new roman",15,'bold'),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=320,relwidth=1)

        # self.msg2='' 
        # self.lbl_msg2=Label(studentFrame,text=self.msg2,font=("times new roman",15,'bold'),bg='white',fg='red')
        # self.lbl_msg2.place(x=0,y=320,relwidth=1)

#----QR code Windoww------
        QRFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        QRFrame.place(x=600,y=100,width=250,height=380)

        QRtitle=Label(QRFrame,text="QR CODE",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        self.QRcode=Label(QRFrame,text="No QR \nAvailable",font=('times new roman',15,'italic'),fg='black',bd=1,relief=RIDGE)
        self.QRcode.place(x=35,y=100,width=180,height=180)

        self.QRcode_msg=''
        self.QRcode_lbl=Label(QRFrame,text=self.QRcode_msg,font=("times new roman",15,'bold'),bg='white',fg='black')
        self.QRcode_lbl.place(x=58,y=320)

    def clear(self):
        self.var_student_id.set('')
        self.var_name.set('')
        self.var_sec.set('')
        self.var_batch.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.QRcode.config(image='')
        self.QRcode_msg=''
        self.QRcode_lbl.config(text=self.QRcode_msg)

    def generate(self):
        if self.var_batch.get()=='' or self.var_name.get()=='' or self.var_sec.get()=='' or self.var_student_id.get()=='':
            self.msg='All fields are required !'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qrdata=(f"Student ID: {self.var_student_id.get()}\nStudent Name:{self.var_name.get()}\nSection:{self.var_sec.get()}\nBatch: {self.var_batch.get()}")
            qr_code=qrcode.make(qrdata)
            # print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("qr_img/std_"+str(self.var_student_id.get())+'.png')

            # -----QR Code Image Update -----
            self.im=ImageTk.PhotoImage(file="qr_img/std_"+str(self.var_student_id.get())+'.png')
            self.QRcode.config(image=self.im)
             # -----Updating Notification----
            self.msg='QR Generated Successfully'
            self.lbl_msg.config(text=self.msg,fg='green')
            self.QRcode_msg='Scan your QR'
            self.QRcode_lbl.config(text=self.QRcode_msg,fg='black')

root=Tk()
obj = QRgenerator(root)
root.mainloop()