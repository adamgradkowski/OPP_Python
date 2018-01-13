import datetime #Adam: doczytac
import pytz # Adam: dotyczac

class Account:
	""" Simple account class with balance"""

	@staticmethod
	def _current_time():
		utc_time = datetime.datetime.utcnow()
		return pytz.utc.localize(utc_time)

	def __init__(self,n,b):
		self.name = n
		self.balance = b
		self.transaction_list = []
		print("Account created for " + self.name)

	def show_balance(self):
		print("Balace is {}".format(self.balance))

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			self.transaction_list.append((Account._current_time(), amount))
			#self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
			self.show_balance()

	def withdraw(self,amount):
		if 0 < amount <= self.balance:
			self.balance -= amount
			self.transaction_list.append((Account._current_time(), -amount))
		else:
			print("The amount must be greater than 0 and no more than acount balance")
		self.show_balance()
	def show_transactions(self):
		for date, amount in self.transaction_list:
			if amount > 0:
				trans_type = 'deposited'
			else:
				trans_type = 'withdrawn'
				amount *= -1
			print("{} {} on {} (local time was {})".format(amount, trans_type, date, date.astimezone()))

if __name__ == '__main__':
	adam = Account("Adam",0)
	#adam.show_balance()
	adam.deposit(150)
	adam.withdraw(100)
	adam.withdraw(100)
	adam.show_transactions()