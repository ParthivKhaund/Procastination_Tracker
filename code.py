# so first lets start outline 

# a project that reminds people to log after every hour their ouptur for the past hour 


import sched
import time

# a project that reminds people to log after every hour

log_tasks = []
productive_hours = []
def log_asker():
	try:
		print("what's your output for the last hour? :")
		past_hour = input()
		log_tasks.append(past_hour)
	except ValueError:
		print("please give a proper answer")


# asks if feel productive or not 
# integrated tips with productivity checker 

def productive_checker():
	answer = "sample"
	while (answer!= "yes" and answer!= "no"):
		answer = input("were you productivity? :")
		if answer == "no":
			tips = input("do you wish to review productivity tips ? :")
			if tips == "yes":
				print("DO Just Start\n")	
				print("DO set a hard deadline for tasks\n")							
				print("DONT think its a small task will do it later\n")
				print("DO if cravings , breathe and be in control\n")
				print("DO list down all tasks (DONT be intimidated)\n")
				print("DO Pomodoro Technique\n")
				print("DO if other stuff comed to mind add to distraction list\n")
	productive_hours.append(answer)


# scheduling evry hour for the user required time frame 

def running_for_hours():
	try:
		hours = int(input("How many hours of work?"))
		counter = 1
		while counter <= hours:
			time.sleep(1)# change to 3600 for every hour 
			log_asker()
			productive_checker()
			counter+=1
	except ValueError:
		print("please give a number")

# gives them tips for productivity 



# gives an hourly (csv) log of user inputs

#outputs

running_for_hours()
print(log_tasks)
print(productive_hours)
