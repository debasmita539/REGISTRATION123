import string
from cProfile import label
from tkinter import *
def TK():
    pass
root = Tk()
def getvals():
    print("Accepted")
Label(root, text=" REGISTRATION FORM", font="arial 15 bold").grid(row=0, column=3)
name=Label(root,text="NAME")
phone=Label(root,text="PHONE")
gender=Label(root,text="GENDER")
email=Label(root,text="EMAIL")
password=Label(root,text="PASSWORD")
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
email.grid(row=4,column=2)
password.grid(row=5,column=2)

namevalue =StringVar
phonevalue=StringVar
gendervalue=StringVar
emailvalue=StringVar
passwordvalue=StringVar
checkvalue=IntVar

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phone)
genderentry=Entry(root,textvariable=gender)
passwordentry=Entry(root,textvariable=passwordvalue)
emailentry=Entry(root,textvariable=emailvalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
passwordentry.grid(row=4,column=3)
emailentry.grid(row=5,column=3)

checkbtn=Checkbutton(text="remember me?",variable=checkvalue)
checkbtn.grid(row=6,column=3)
Button(text="submit",command=getvals).grid(row=7,column=3)
root.mainloop()



