#This function greets the user given their name

class Greeter:
	
	def greet(name):
		if not name:
			return "Please provide a name."

		return "Hello " + name + ". Have a great day!"