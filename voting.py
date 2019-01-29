responses = {}

polling_active = True

while polling_active:
	name = input("\nWhat is your name: \n")
	response = input("Who are you going to vote for? \n")
	
	responses[name] = response
	
	repeat = input("WOuld you like to go on voting? (yes/no)")
	if repeat == 'no':
		polling_active = False
		
	print("\n....Poll Results....")
	
	for name, response in responses.items():
		print(name.title() + " would like " + response.title() + " to be the 6th President of Kenya")
