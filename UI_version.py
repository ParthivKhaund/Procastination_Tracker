from tkinter import *

m = Tk()

m.title("Procastination Check")
m.geometry("500x500")


# to get hours form user (hours)
Label(m,text="How many hours of productivity ? : ").pack()
e1 = Entry(m)
e1.pack()
def get_hours():
	global hours
	hours = int(e1.get())

b1 = Button(m,text="Enter Hours",command=get_hours)
b1.pack()

# to get every hour imput of task from user (past_hour)
Label(m,text = "what's your output for the last hour? :").pack()
e2 = Entry(m)
e2.pack()
def get_task_done():
	global past_hour
	past_hour = e2.get()

b2 = Button(m,text ="Enter Past hour work",command =get_task_done)
b2.pack()

# to check productivity and display tips 

def disp_tips():
	pop = Tk()
	pop.title("Tips")
	tips = Text(pop)
	tips.pack()
	text_tips = """
	DO Just Start
	
	DO set a hard deadline for tasks
	
	DONT think its a small task will do it later
	
	DO if cravings , breathe and be in control
	
	DO list down all tasks (DONT be intimidated)
	
	DO Pomodoro Technique
	
	DO if other stuff come to mind add to distraction list"""
	tips.insert(END,text_tips)
	b5 = Button(pop,text="Back",command=pop.destroy)
	b5.pack()
	pop.mainloop()

def popupmsg():
    popup = Tk()
    popup.title("Help")
    label = Label(popup, text="would you like to review tips?")
    label.pack()
    B0 = Button(popup,text = "YES",command= disp_tips)
    B0.pack()
    B1 = Button(popup, text="NO", command = popup.destroy)
    B1.pack()
    popup.mainloop()


Label(m,text="were you productive").pack()

def yes():
	answer = "yes"
def no():
	answer = "no"
	popupmsg()


b3 = Button(m,text="YES",command=yes)
b3.pack()
b4 = Button(m,text="NO",command=no)
b4.pack()


m.mainloop()