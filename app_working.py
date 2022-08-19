from tkinter import *
import time

class root(Tk):
    def __init__(self):
        super(root, self).__init__()

        self.title("Timer")
        
        self.buttonplay = Button(self, text = "Play", fg= 'green', command = self.play)
        self.buttonplay.pack()

        self.buttonpause = Button(self, text = "Pause", fg = "red", command=self.pause)
        self.buttonpause.pack()

        self.createTimers()

    def play(self):
        self.timeit=True
        self.timer1.configure(bg='#1C953D')
        self.doTimer()

    def pause(self):
        self.timeit=False
        self.timer1.configure(bg='#454545')
        
    def reset(self):
        self.timer1.destroy()
        self.createTimers()

    def createTimers(self):
        self.minute = 0
        self.second = 5
        self.ms = 0
        self.total = self.second + self.minute *60 + self.ms*0.001
        self.time1 = StringVar()
        self.time1.set(str(self.minute).rjust(2, '0') + ':' + str(self.second).rjust(2, '0') +'.'+ str(self.ms).rjust(3, '0'))
        self.timer1 = Label(self, textvariable=self.time1, bg='#454545', fg='white', font ="Gadugi 40 bold")
        self.timer1.pack()
        self.timer1.configure(bg='#454545')

    def doTimer(self):
        self.time = self.second + self.minute *60 + self.ms*0.001
        if self.time !=0: #Checks if the timer ended
            if self.timeit:
                self.timer1.configure(bg='#1C953D')
                
                self.ms = self.ms -1
                if self.ms <0:
                    self.second = self.second -1
                    self.ms = 999
                if self.second == -1:
                    self.minute = self.minute -1
                    self.second = 59

                self.time1.set(str(self.minute).rjust(2, '0') + ':' + str(self.second).rjust(2, '0') +'.'+ str(self.ms).rjust(3, '0'))
                
                if self.timeit:
                    self.after(1, self.doTimer)

        else:
            self.ended = 1
            self.timer1.configure(bg='#FF0000')
            self.after(3000, self.reset)


root = root()
root.mainloop()