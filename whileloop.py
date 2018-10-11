prompt = "\nTell me pizza toppings you wish to add:"
prompt += "\nEnter 'end' to end the program. "
topping_list = []
active = True
topping = ""
while active:
	topping = input(prompt)
	if topping == 'end':
		active = False
		print("Here is your list of toppings")
		print(topping_list)
	else:
		topping_list.append(topping)
