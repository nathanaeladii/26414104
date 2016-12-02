DMIN SEARCH QUIZ BY !
class SearchUpdateQuiz(Music):
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.geometry('300x420+450+150')
        self.imagebackground = Image.open('image\gbackground.jpeg')
        self.displaybackground = ImageTk.PhotoImage(self.imagebackground)
        self.labelbackground = Label(self.root, image=self.displaybackground).place(x=-5, y=-5)
        self.Menu_bar = Menu(self.root)
        self.Menu_bar.add_command(label="Insert", command=self.insertquiz)
        self.Menu_bar.add_command(label="Logout", command=self.logoutquiz)
        self.root.config(menu=self.Menu_bar)
        self.labelspace = Label(self.root, bg='black').pack()
        self.labeljdlAdmin = Label(self.root, text='ADMIN PANEL', fg='blue', font=("Helvetica", 16), bg='black').pack()
        self.labeljdlUpdate = Label(self.root, text='UPDATE YOUR QUESTION, ANSWER AND HINT', fg='blue',font=("Helvetica", 8), bg='black').pack()
        self.labelsearchid = Label(self.root, text='Search ID Question ', bg='black', fg='white').pack()
        self.stringsearchid = StringVar()
        self.entrysearchid = Entry(self.root, textvariable=self.stringsearchid).pack()
        self.labelspace = Label(self.root, bg='black').pack()
        self.buttonsearch = Button(self.root, text='SEARCH', command=self.searchquiz, width='16').pack()

        self.imageplay = Image.open('image\gplay.png')
        self.displayplay = ImageTk.PhotoImage(self.imageplay)
        self.buttonplay = Button(self.root, command=self.play, image=self.displayplay).place(x=70, y=355)
        self.imageresume = Image.open('image\gresume.png')
        self.displayresume = ImageTk.PhotoImage(self.imageresume)
        self.buttonresume = Button(self.root, command=self.resume, image=self.displayresume).place(x=110, y=355)
        self.imagepause = Image.open('image\gpause.png')
        self.displaypause = ImageTk.PhotoImage(self.imagepause)
        self.buttonpause = Button(self.root, command=self.pause, image=self.displaypause).place(x=150, y=355)
        self.imagestop = Image.open('image\gstop.png')
        self.displaystop = ImageTk.PhotoImage(self.imagestop)
        self.buttonstop = Button(self.root, command=self.stop, image=self.displaystop).place(x=190, y=355)
    def play(self):
        Music.PlayMusicAdmin(self)
    def resume(self):
        Music.UnpauseMusic(self)
    def pause(self):
        Music.PauseMusic(self)
    def stop(self):
        Music.StopMusic(self)
    def searchquiz(self):
        tempID = self.stringsearchid.get()
        if tempID == '':
            tkMessageBox.showwarning(title="Error!", message="Empty ID")
        else:
            c.execute("SELECT * FROM quizadmin WHERE id = ?", (tempID,))
            if c.fetchall():
                self.root.destroy()
                self.suq = Tk()
                self.app = UpdateQuiz(self.suq, 'Update Quiz', tempID)
                self.suq.deiconify()
            else:
                tkMessageBox.showwarning(title="Error !", message="ID Not Found")
    def insertquiz(self):
        self.root.destroy()
        self.insquiz = Tk()
        self.app = AdminInsert(self.insquiz, 'Insert Quiz')
        self.insquiz.deiconify()
    def logoutquiz(self):
        self.root.destroy()
        self.logoutq = Tk()
        self.app = Login(self.logoutq, 'Login')
        self.logoutq.deiconify()
