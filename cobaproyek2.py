DMIN UPDATE QUIZ !
class UpdateQuiz():
    def __init__(self, root, title, sID):
        self.root = root
        self.root.title(title)
        self.root.geometry('300x420+450+150')
        self.tempID = sID
        self.imagebackground = Image.open('image\gbackground.jpeg')
        self.displaybackground = ImageTk.PhotoImage(self.imagebackground)
        self.labelbackground = Label(self.root, image=self.displaybackground).place(x=-5, y=-5)
        self.labelspace = Label(self.root, bg='black').pack()
        self.Menu_bar = Menu(self.root)
        self.Menu_bar.add_command(label="Insert", command=self.insertquiz)
        self.Menu_bar.add_command(label="Logout", command=self.logoutquiz)
        self.root.config(menu=self.Menu_bar)
        self.labelspace = Label(self.root, bg='black').pack()
        self.labeljdladmin = Label(self.root, text='ADMIN PANEL', fg='blue', font=("Helvetica", 16), bg='black').pack()
        self.labeljdlupdate = Label(self.root, text='UPDATE YOUR QUESTION, ANSWER AND HINT', fg='blue',font=("Helvetica", 8), bg='black').pack()
        self.imageback = Image.open('image\gback.png')
        self.displayback = ImageTk.PhotoImage(self.imageback)
        self.buttonback = Button(self.root, command=self.backsearchupdate, image=self.displayback).place(x=250, y=10)
        self.labelspace = Label(self.root, bg='black').pack()
        c.execute('''SELECT question FROM quizadmin WHERE id = ?''', (sID,))
        for row in c.fetchone():
            self.tempquestion = str(row)
        self.labelquestion = Label(self.root, text='Question: ', bg='black', fg='white').pack()
        self.stringquestion = StringVar()
        self.stringquestion.set(self.tempquestion)
        self.entryquestion = Entry(self.root, textvariable=self.stringquestion).pack()

        c.execute('''SELECT answer FROM quizadmin WHERE id = ?''', (sID,))
        for row in c.fetchone():
            self.tempanswer = str(row)
        self.labelasnwer = Label(self.root, text='Answer ', bg='black', fg='white').pack()
        self.stringanswer = StringVar()
        self.stringanswer.set(self.tempanswer)
        self.entryanswer = Entry(self.root, textvariable=self.stringanswer).pack()

        c.execute('''SELECT hint FROM quizadmin WHERE id = ?''', (sID,))
        for row in c.fetchone():
            self.temphint = str(row)
        self.labelhint = Label(self.root, text='Hint ', bg='black', fg='white').pack()
        self.stringhint = StringVar()
        self.stringhint.set(self.temphint)
        self.entryhint = Entry(self.root, textvariable=self.stringhint).pack()

        self.labelspace = Label(self.root, bg='black').pack()
        self.button1 = Button(self.root, text='UPDATE', command=self.updatequiz, width='16').pack()

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
    def updatequiz(self):
        uid = self.tempID
        question_e = self.stringquestion.get()
        answer_e = self.stringanswer.get()
        hint_e = self.stringhint.get()

        if question_e == '' or answer_e == '' or hint_e == '':
            tkMessageBox.showwarning(title="Error !", message="Empty Question/Answer/Hint")
        else:
            c.execute("UPDATE quizadmin SET question = ?, answer = ?, hint = ? WHERE id = ?",
                      (question_e, answer_e, hint_e, uid))
            conn.commit()
            tkMessageBox.showwarning(title="SUCCESS", message="Update Success")
    def backsearchupdate(self):
        self.root.destroy()
        self.upq = Tk()
        self.app = SearchUpdateQuiz(self.upq, 'Update Quiz')
        self.upq.deiconify()
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
