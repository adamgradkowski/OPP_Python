class Account:
	""" Simple account class with balance"""

	def __init__(self,n,b):
		self.name = n
		self.balance = b
		print("Account created for " + self.name)

	def show_balance(self):
		print("Balace is {}".format(self.balance))

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
		self.show_balance()
	def withdraw(self,amount):
		if 0 < amount <= self.balance:
			self.balance -= amount
		else:
			print("The amount must be greater than 0 and no more than acount balance")
		self.show_balance()

if __name__ == '__main__':
	adam = Account("Adam",0)
	#adam.show_balance()
	adam.deposit(150)
	adam.withdraw(100)
	adam.withdraw(100)