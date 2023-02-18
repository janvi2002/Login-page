from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.config(bg="#fff")
root.resizable(False,False)

def sign_in():
    username=user.get()
    passwrd=password.get()

    if username=="admin" and passwrd=="1234":
        screen=Toplevel(root)
        screen.title("APP")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")
        label(screen,Text="Hello everyone",bg="#fff",font=("Calibri(Body",50,"bold")).pack(expand=True)
        screen.mainloop()
        
    elif username!="admin" and passwrd!="1234":
        messagebox.showerror("invalid","invalid username and password")
    
    elif password!="1234":
        messagebox.showerror("invalid","invalid password")
    elif  username!="admin":
        messagebox.showerror("invalid","invalid password")


# image on log in page
img=PhotoImage(file="D:\\miniproject\\tkinter login\\login.png")
Label(root,image=img,bg="#fff").place(x=50,y=50)

# frame /section inside which all form details come
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

# heading for the form
heading=Label(frame,text="Sign In",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",20,"bold"))
heading.place(x=100,y=5)

###############################----------------
def on_enter(e):
    user.delete(0,"end")

def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"Username")

# entry is for taking input from user
user=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11))
user.place(x=30,y=80)
user.insert(0,"Username") 
user.bind("<FocusIn>",on_enter)  
user.bind("<FocusOut>",on_leave)
# for the underline
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

######################------------------------
def on_enter(e):
    password.delete(0,"end")

def on_leave(e):
    name=password.get()
    if name=="":
        password.insert(0,"Password")

# taking password
password=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11))
password.place(x=30,y=150)
password.insert(0,"Password") 
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
password.bind("<FocusIn>",on_enter)
password.bind("<FocusOut>",on_leave)
#####################------------------------


Button(frame,width=39,pady=7,text="Sign In",bg="#57a1f8",fg="white",border=0,command=sign_in).place(x=35,y=204)

label=Label(frame,text="Don't have a account?",fg="black",bg="white",font=("Microsoft Yahei UI Light",9))
label.place(x=75,y=260)
sign_up=Button(frame,width=6,text="Sign up",border=0,bg="white",cursor="hand2",fg="#57a1f8")
sign_up.place(x=215,y=260)


root.mainloop()