# in the_bank.py
from operator import ne



class Account(object):
	
	ID_COUNT = 1
	
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)
		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0
		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")
	
	def transfer(self, amount):
		self.value += amount

# in the_bank.py
class Bank(object):
	"""The bank"""
	
	def __init__(self):
		self.accounts = []
	
	def add(self, new_account):
		""" Add new_account in the Bank
		@new_account: Account() new account to append
		@return True if success, False if an error occured
		"""
		# test if new_account is an Account() instance and if
		# it can be appended to the attribute accounts
		# ... Your code ...
		if not isinstance(new_account, Account):
			return False
		try:
			new_account.name
			if not isinstance(new_account.name, str):
				return False
			if len([x for x in self.accounts if new_account.name == x.name]) > 0:
				return False
		except AttributeError:
			return False

		self.accounts.append(new_account)
		return True
	
	def transfer(self, origin, dest, amount):
		"""" Perform the fund transfer
		@origin: str(name) of the first account
		@dest: str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		"""
		# ... Your code ...


		try:
			if (not isinstance(amount, (int, float)) or amount < 0):
				return False
		
			# the right object,
			acc_src = None
			for i in self.accounts:
				if origin == i.name:
					acc_src = i
					break
			if acc_src is None:
				return False

			acc_dest = None
			for i in self.accounts:
				if dest == i.name:
					acc_dest = i
					break
			if acc_dest is None:
				return False
			if not isinstance(acc_src, Account) or not isinstance(acc_dest, Account):
				return False
			
			# no attribute name, id and value,
			# name not being a string,
			# id not being an int,
			# value not being an int or a float.
			if not isinstance(acc_src.name, str) or not isinstance(acc_dest.name, str): 
				return False
			if not isinstance(acc_src.id, int) or not isinstance(acc_dest.id, int):
				return False
			if not isinstance(acc_src.value, (int, float)) or not isinstance(acc_dest.value, (int, float)):
				return False
		
		
		except (AttributeError, TypeError):
			return False

		
		#an even number of attributes,
		attrlen = len(acc_src.__dict__)
		for i in acc_src.__dict__.values():
			if i is None:
				attrlen -= 1
		if attrlen % 2 == 0:
			return False
		
		attrlen = len(acc_src.__dict__)
		for i in acc_dest.__dict__.values():
			if i is None:
				attrlen -= 1
		if attrlen % 2 == 0:
			return False

		# an attribute starting with b,
		for i in acc_src.__dict__.keys():
			if i[0] == 'b':
				return False
		for i in acc_dest.__dict__.keys():
			if i[0] == 'b':
				return False


		# no attribute starting with zip or addr,
		if len([x for x in acc_src.__dict__.keys() if x.startswith('addr')]) == 0:
			return False
		if len([x for x in acc_src.__dict__.keys() if x.startswith('zip')]) == 0:
			return False		
		if len([x for x in acc_dest.__dict__.keys() if x.startswith('addr')]) == 0:
			return False
		if len([x for x in acc_dest.__dict__.keys() if x.startswith('zip')]) == 0:
			return False
	
	
		# and stores enough money to complete the transfer.
		if acc_src.value < amount:
			return False
		acc_src -= amount
		acc_dest += amount
	


	def fix_account(self, name):
		""" fix account associated to name if corrupted
		@name: str(name) of the account
		@return True if success, False if an error occured
		"""
		# ... Your code ...

		acc = None
		for i in self.accounts:
			if name == i.name:
				acc = i
				break
		if acc is None:
			return False

			
		if not isinstance(acc.name, str): 
			return False
		if not isinstance(acc.id, int):
			return False
		if not isinstance(acc.value, (int, float)) or not isinstance(acc_dest.value, (int, float)):
			return False

		if not isinstance(acc_src, Account):
				return False




bnp = Bank()


acc_valid_1 = Account('Sherlock Holmes',
						zip='NW1 6XE',
						addr='221B Baker street',
						value=1000.0)
acc_valid_2 = Account('James Watson',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=25000.0,
                          info=None)

acc_invalid_1 = Account("Adam",
                        value=42,
                        zip='0',
                        addr='Somewhere',
						hello = 12,)
acc_invalid_2 = Account(name = 'lolilol',
                        zip='1',
                        addr='Mexico',
                        value=0)
acc_invalid_2.value = "g du bif"
acc_invalid_4 = Account("Douglass",
                            zip='42',
                            addr='boulevard bessieres',
                            value=42,
							bref='yes')
acc_invalid_3 = Account('Wjeden',
                        addr='Somewhere in the Milky Way',
                        value=42)
acc_invalid_5 = Account("Jul",
                        zip='3',
                        value=42)
    


print(bnp.add(acc_valid_1))
print(bnp.add(acc_valid_2))
print()
print(bnp.add(acc_invalid_1))
print(bnp.add(acc_invalid_2))
print(bnp.add(acc_invalid_3))
print(bnp.add(acc_invalid_4))
print(bnp.add(acc_invalid_5))


print(bnp.accounts[1].__dict__)

# print(bnp.add(Account('Smith Jane',
#         zip='911-745',
#         value=1000.0,
#         ref='1044618427ff2782f0bbece0abd05f31'))
# )
# bnp.add(Account(
#         'William John',
#         zip='100-064',
#         value=6460.0,
#         ref='58ba2b9954cd278eda8a84147ca73c87',
#         info=None,
#         other='This is the vice president of the corporation'
#     ))


nb = 12

