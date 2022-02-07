####
# Let's make a Money management app
###

#Project : https://github.com/fuzzyray/budget-app
# If help needed : https://www.youtube.com/watch?v=zOYqy8botO8

# Make the class
class Category(object):

	def __init__(self, name):

		self.name = name
		self.balance = 0
		self.ledger = list()

	def __repr__(self):
		s = str(self.name).center(30, "*")
		for i in self.ledger :
			s += str("\n{}".format(i["description"][0:22])).ljust(23," ")
			s += str("{:.2f}".format(float(i["amount"]))).rjust(7," ")
		s += f"\nTotal : {self.balance}"
		return s


	def get_balance(self):
		print("Current balance : {0} EUR".format(self.balance))

	def check_funds(self, amount):
		self.amount = float(amount)
		if self.balance >= self.amount :
			return True
		else :
			return False

	def deposit(self, amount, description=""):
		self.amount =  float(amount)
		self.description = str(description)
		self.balance += float(self.amount)
		self.ledger.append({"amount": self.amount , "description": self.description })


	def withdraw(self, amount, description=""):
		self.amount =  float(amount)
		self.description = str(description)

		if self.check_funds(self.amount) is True :
			self.balance -= float(self.amount)
			self.ledger.append({"amount": -self.amount , "description": self.description })
			return True
		else :
			return False

	def transfer(self, amount, instance):
		self.amount = amount
		if self.check_funds(self.amount) is True :

			self.withdraw(amount, "Transfer to {0}".format(instance.name))
			instance.deposit(amount, "Transfer from {0}".format(self.name))
			return True
		else : return False

	def print(self) : print(self.ledger)

# Output the class



a = Category("Food")
b = Category("Clothing")

a.deposit(1000, "Initial deposit")
a.withdraw(55.64, "Groceries")
a.withdraw(15.69, "Lunch at Cafeteria")
a.transfer(50, b)

print(a)
print(b)
