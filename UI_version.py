# improve UI
# for hours do a thing that closes window after given hours and gives a message 
# fix the every hour request thing 
# once button has been pressed see that text is wiped 


from tkinter import *
import sched
import time
import datetime
import csv


log_tasks = []
productive_hours = []


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
	log_tasks.append(past_hour)

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
    label = Label(popup, text="do you wish to review productivity tips ? ")
    label.pack()
    B0 = Button(popup,text = "YES",command= disp_tips)
    B0.pack()
    B1 = Button(popup, text="NO", command = popup.destroy)
    B1.pack()
    popup.mainloop()


Label(m,text="were you productive").pack()

def yes():
	global answer
	answer = "yes"
	productive_hours.append(answer)

def no():
	global answer
	answer = "no"
	productive_hours.append(answer)
	popupmsg()


b3 = Button(m,text="YES",command=yes)
b3.pack()
b4 = Button(m,text="NO",command=no)
b4.pack()



# remind every hour to update


def hour_pop():
	remind_pop = Tk()
	remind_pop.title("Update inputs")
	Label(remind_pop,text = "Please Update all the values").pack()

	close = Button(remind_pop,text="close",command=remind_pop.destroy)
	close.pack()
	remind_pop.mainloop()
	
# to get report in csv for further analysis 

def get_csv():
	date = datetime.date.today()
	f = open("productivity report for %s.csv"%(date),"w")
	writer = csv.writer(f,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
	writer.writerow(log_tasks)
	writer.writerow(productive_hours)

b8 = Button(m,text = "get report",command=get_csv)
b8.pack()

m.mainloop()
