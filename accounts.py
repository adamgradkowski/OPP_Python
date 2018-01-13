import datetime #Adam: doczytac
import pytz # Adam: dotyczac

class Account:
	""" Simple account class with balance"""

	@staticmethod
	def _current_time():
		utc_time = datetime.datetime.utcnow()
		return pytz.utc.localize(utc_time)

	def __init__(self,n,b):
		self.__name = n # Adam: doczytac public / non public : _ / __ / bez
		self.__balance = b
		self.__transaction_list = [(Account._current_time(), b)]
		print("Account created for " + self.__name)

	def show_balance(self):
		print("Balace is {}".format(self.__balance))

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			self.__transaction_list.append((Account._current_time(), amount))
			#self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
			self.show_balance()

	def withdraw(self,amount):
		if 0 < amount <= self.__balance:
			self.__balance -= amount
			self.__transaction_list.append((Account._current_time(), -amount))
		else:
			print("The amount must be greater than 0 and no more than acount balance")
		self.show_balance()
	def show_transactions(self):
		for date, amount in self.__transaction_list:
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

	ania = Account("Ania", 800)
	ania.__balance = 200
	ania.deposit(100)
	ania._Account__balance = 404
	ania.show_balance()
