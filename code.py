import sched
import time
import datetime
import csv

# reminds people to log after every hour and give work done

log_tasks = []
productive_hours = []

def log_asker():
	try:
		past_hour = input("what's your output for the last hour? :")
		log_tasks.append(past_hour)
	except ValueError:
		print("please give a proper answer")


# asks if feel productive or not 
# integrated tips with productivity checker 

def productive_checker():
	answer = "sample"
	while (answer!= "yes" and answer!= "no"):
		answer = input("were you productivity? :")
		# tips if needed by user
		if answer == "no":
			tips = "sample"
			while (tips!= "yes" and tips!= "no"):
				tips = input("do you wish to review productivity tips ? :")
				if tips == "yes":
					print("\n")
					print("DO Just Start\n")	
					print("DO set a hard deadline for tasks\n")							
					print("DONT think its a small task will do it later\n")
					print("DO if cravings , breathe and be in control\n")
					print("DO list down all tasks (DONT be intimidated)\n")
					print("DO Pomodoro Technique\n")
					print("DO if other stuff come to mind add to distraction list\n")
	productive_hours.append(answer)


# scheduling evry hour for the user required time frame 

def running_for_hours():
	try:
		hours = int(input("How many hours of work? : "))
		counter = 1
		while counter <= hours:
			time.sleep(3600)# change to 3600 for every hour 
			log_asker()
			productive_checker()
			counter+=1
	except ValueError:
		print("please give a number")

# calling function 

running_for_hours()

print(log_tasks)
print(productive_hours)

#gives an hourly (csv) log of user inputs , used for further analysis 

date = datetime.date.today()

f = open("productivity report for %s.csv"%(date),"w")
writer = csv.writer(f,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
writer.writerow(log_tasks)
writer.writerow(productive_hours)

f.close()




