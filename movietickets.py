prompt = "\nWelcome to the Theatre"
prompt += "\nHow old are you?: "
#active = True
age = ""
#while active:
age = input(prompt)
age = int(age)
if age < 3:
	print("Your ticket is free.")
#	break
else:
	if age < 13:
		print("Your ticket is $10.")
#		break
	else:
		print("Your ticket is $15.")
		