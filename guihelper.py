from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

class GUIhelper:
    def __init__(self,f,g):
        self._root=Tk()
        self._root.title("Tinder Login")
        self._root.minsize(250,450)
        self._root.configure(background="#FC4F67")

        label1=Label(self._root, text="Tinder", bg="#FC4F67", fg="#fff")
        label1.configure(font=("Verdana",24,"bold","italic"))
        label1.pack(pady=(30,10))

        self.label2 = Label(self._root, text="Kindly login to proceed", bg="#FC4F67", fg="#fff")
        self.label2.configure(font=("Verdana", 12, "bold"))
        self.label2.pack(pady=(10, 10))

        label3 = Label(self._root, text="Email", bg="#FC4F67", fg="#fff")
        label3.configure(font=("Verdana", 10, "bold"))
        label3.pack(pady=(10, 5))

        self._emailInput=Entry(self._root)
        self._emailInput.pack(ipadx=40 , ipady=8, pady=(2,5))

        label4 = Label(self._root, text="Password", bg="#FC4F67", fg="#fff")
        label4.configure(font=("Verdana", 10, "bold"))
        label4.pack(pady=(10, 5))

        self._passwordInput = Entry(self._root,show = "*")
        self._passwordInput.pack(ipadx=40, ipady=8, pady=(2, 30))

        btn1=Button(self._root, text="Sign In", bg="#fff" ,fg="#FC4F67", command=lambda : f())
        btn1.configure(width=28,height=2)
        btn1.pack(pady=(1,10))

        label4 = Label(self._root, text="Not a member ? Sign up now! ", bg="#FC4F67", fg="#fff")
        label4.configure(font=("Verdana", 10))
        label4.pack(pady=(1, 5))

        btn2 = Button(self._root, text="Sign Up", bg="#fff", fg="#FC4F67",command=lambda : g())
        btn2.pack(pady=(2,1))

        self._root.mainloop()

    """def get_num(self):
        print(self._emailInput.get())
        print(self._passwordInput.get())"""

    def regWindow(self,f):
        self._root.destroy()

        self._root=Tk()
        self._root.title("Register for Tinder")
        self._root.minsize(300, 550)
        self._root.configure(background="#fd5068")

        label1 = Label(self._root, text="Tinder", bg="#fd5068", fg="#fff")
        label1.configure(font=("Constantia", 24, "bold", "italic", "underline"))
        label1.pack(pady=(10, 10))

        self.label2 = Label(self._root, text="Fill the form to register", bg="#fd5068", fg="#fff")
        self.label2.configure(font=("Verdana", 12, "bold"))
        self.label2.pack(pady=(5, 10))

        label3 = Label(self._root, text="Name", bg="#fd5068", fg="#fff")
        label3.configure(font=("Verdana", 12, "bold"))
        label3.pack(pady=(5, 5))

        self._nameInput = Entry(self._root)
        self._nameInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        label4 = Label(self._root, text="Email", bg="#fd5068", fg="#fff")
        label4.configure(font=("Verdana", 12, "bold"))
        label4.pack(pady=(5, 5))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        label8 = Label(self._root, text="Password", bg="#fd5068", fg="#fff")
        label8.configure(font=("Verdana", 12, "bold"))
        label8.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        label5 = Label(self._root, text="Gender", bg="#fd5068", fg="#fff")
        label5.configure(font=("Verdana", 12, "bold"))
        label5.pack(pady=(5, 5))

        self._genderInput = Entry(self._root)
        self._genderInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        label6 = Label(self._root, text="Age", bg="#fd5068", fg="#fff")
        label6.configure(font=("Verdana", 12, "bold"))
        label6.pack(pady=(5, 5))

        self._ageInput = Entry(self._root)
        self._ageInput.pack(ipadx=50, ipady=7, pady=(1, 5))

        label7 = Label(self._root, text="City", bg="#fd5068", fg="#fff")
        label7.configure(font=("Verdana", 12, "bold"))
        label7.pack(pady=(5, 5))

        self._cityInput = Entry(self._root)
        self._cityInput.pack(ipadx=50, ipady=7, pady=(1, 15))

        btn1 = Button(self._root, text="Sign Up", fg="#fd5068", bg="#fff", command=lambda: f())
        btn1.configure(width=25, height=2, font=("verdana", 10, "bold"))
        btn1.pack()

        self._root.mainloop()

    def mainWindow(self,other,data,mode,num=0):
        #self._root.destroy()
        #self._root=Tk()
        self.clean()
        self._root.title("My Profile")
        self._root.minsize(400,500)
        self._root.configure(background="#fff")

        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile", command=lambda :other.loadProfile())
        filemenu.add_command(label="Edit Profile", command=lambda :other.editProfile())
        filemenu.add_command(label="View Users", command=lambda :other.viewProfile(num))
        filemenu.add_command(label="Logout", command=lambda :other.myLogout())

        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals", command=lambda : other.propose())
        helpmenu.add_command(label="My Request")
        helpmenu.add_command(label="My Matches")
        if mode == 1 or mode ==2:
            imageUrl="img/" + data[0][-1]
            load = Image.open(imageUrl)
            load = load.resize((200,200), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)

            img = Label(image=render)
            img.image = render
            img.pack()

            name = "Name: " + data[0][1]
            label1 = Label(self._root, text=name, bg="#fff", fg="#000")
            label1.configure(font=("Verdana", 14, "bold"))
            label1.pack(pady=(10, 5))

            gender = "Not Intrested in:  " + str(data[0][4])
            label2 = Label(self._root, text=gender, bg="#fff", fg="#000")
            label2.configure(font=("Verdana", 14, "bold"))
            label2.pack(pady=(10, 5))

            age = "Age: " + str(data[0][5])
            label3 = Label(self._root, text=age, bg="#fff", fg="#000")
            label3.configure(font=("Verdana", 14, "bold"))
            label3.pack(pady=(10, 5))

            city = "From : " + data[0][6]
            label4 = Label(self._root, text=city, bg="#fff", fg="#000")
            label4.configure(font=("Verdana", 14, "bold"))
            label4.pack(pady=(10, 5))

        if mode == 2:
            frame=Frame(self._root)
            frame.pack()
            btn1 = Button(frame, text="previous", bg="#fff", fg="#FC4F67",command=lambda :other.viewProfile(num-1))
            btn1.pack(side=LEFT)

            btn2 = Button(frame, text="propose", bg="#fff", fg="#FC4F67", command=lambda : other.propose(str(data[0][0])))
            btn2.pack(side=LEFT)

            btn3 = Button(frame, text="next", bg="#fff", fg="#FC4F67",command=lambda :other.viewProfile(num+1))
            btn3.pack(side=LEFT)

        if mode == 3:
            imageUrl = "img/" + data[0][-1]
            load = Image.open(imageUrl)
            load = load.resize((200, 200), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)

            img = Label(image=render)
            img.image = render
            img.pack()

            btn1 = Button(self._root, text="Profile Picture", fg="#fd5068", bg="#fff", command=lambda :other.editProfilePic())
            btn1.configure(width=12, height=1,font=("verdana", 8, "bold"))
            btn1.pack()

            label3 = Label(self._root, text="Name", bg="#fd5068", fg="#fff")
            label3.configure(font=("Verdana", 12, "bold"))
            label3.pack(pady=(5, 5))

            self._nameInput = Entry(self._root)
            self._nameInput.pack(ipadx=50, ipady=7, pady=(1, 5))


            label8 = Label(self._root, text="Password", bg="#fd5068", fg="#fff")
            label8.configure(font=("Verdana", 12, "bold"))
            label8.pack(pady=(5, 5))

            self._passwordInput = Entry(self._root)
            self._passwordInput.pack(ipadx=50, ipady=7, pady=(1, 5))

            label5 = Label(self._root, text="Gender", bg="#fd5068", fg="#fff")
            label5.configure(font=("Verdana", 12, "bold"))
            label5.pack(pady=(5, 5))

            self._genderInput = Entry(self._root)
            self._genderInput.pack(ipadx=50, ipady=7, pady=(1, 5))

            label6 = Label(self._root, text="Age", bg="#fd5068", fg="#fff")
            label6.configure(font=("Verdana", 12, "bold"))
            label6.pack(pady=(5, 5))

            self._ageInput = Entry(self._root)
            self._ageInput.pack(ipadx=50, ipady=7, pady=(1, 5))

            label7 = Label(self._root, text="City", bg="#fd5068", fg="#fff")
            label7.configure(font=("Verdana", 12, "bold"))
            label7.pack(pady=(5, 5))

            self._cityInput = Entry(self._root)
            self._cityInput.pack(ipadx=50, ipady=7, pady=(1, 15))

            btn1 = Button(self._root, text="Save", fg="#fd5068", bg="#fff", command=lambda: other.save(data))
            btn1.configure(width=25, height=2, font=("verdana", 10, "bold"))
            btn1.pack()

        self._root.mainloop()

    def clean(self):
        for i in self._root.pack_slaves():
            i.destroy()

    def message(self,title,text):
        messagebox.showinfo(title,text)


