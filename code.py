# so first lets start outline 

# a project that reminds people to log after every hour their ouptur for the past hour 


import sched
import time

# a project that reminds people to log after every hour
log_tasks = []
def log_asker():
	try:
		print("what's your output for the last hour?")
		past_hour = input()
		log_tasks.append(past_hour)
	except ValueError:
		print("please give a proper answer")

# scheduling evry hour for the user required time frame 
def running_for_hours():
	try:
		hours = int(input("How many hours of work?"))
		counter = 0
		while counter <= hours:
			time.sleep(10)# change to 3600 for every hour 
			log_asker()
			counter+=1
	except ValueError:
		print("please give a number")

# asks if feel productive or not 

#def productive_checker():


# gives them tips for productivity 
# gives an hourly (csv) log of user inputs

#outputs

running_for_hours()
print(log_tasks)



