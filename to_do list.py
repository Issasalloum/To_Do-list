import time
tasks=[]
print("welcom to the to-do list app!  ")
while True:
	print("-----------------------------‐--------------------------")
	print("choose an option: ")
	print("1: Add task")
	print("2: My tasks")
	print("3: Remove task")
	print("4: Exit")	
	print("--------------------------------------------------------")
	choise=input("choose (1_4) : ")
	if choise=="1":
		value=input("enter the task: ")
		tasks.append(value)
		print("task added ! ")
		time.sleep(1)
	elif choise=="2":
		if not tasks:
			print("no tasks yet! ")	
		else:
			print("your tasks: ") 
			i=1
			for data in tasks:
				print(i,data)
				i+=1
				time.sleep(1)
	elif choise=="3":
		if not tasks:
			print("no tasks to delete! ")
		else:
			i=1
			for data in tasks:
				print(i,data)
				i+=1
			task_number=int(input("enter task number to delete: "))
			if task_number>=1 and task_number<=len(tasks):		
				tasks.pop(task_number-1)
				print(tasks)
				deleted=tasks.pop(task_number-1)
				print(f"deleted task: {deleted}")
				time.sleep(1)
			else:
				print("invalid value! ")
	elif choise=="4":
			print("goodbye!")
			break
	else:
			print("invalid choise : try again ! ")
print("_________________________________________________________________________")									
			