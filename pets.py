def describe_pets(pet_name, pet_type="dog"):
	print("You have a " + pet_type.title() + " named " + pet_name.title() + ". Those are wonderful animals.")
#	
prompt = "\nPlease tell me about your pets."
prompt = "\nWhat "
ipet_type = ""
ipet_name = ""
active = True
while active:
	prompt = "\nWhat kind of pet do you have? "
	ipet_type = input(prompt)
	prompt = "\nWhat is your pet's name? "
	ipet_name = input(prompt)
	describe_pets(pet_name = ipet_name, pet_type = ipet_type) 
	prompt = "\nDo you have any more pets? yes/no "
	more_pets = input(prompt)
	if more_pets == "no":
		active = False