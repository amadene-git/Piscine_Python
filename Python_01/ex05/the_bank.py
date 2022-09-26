# in the_bank.py
import random
import string


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
		if not isinstance(origin, str):
			return False
		if not isinstance(dest, str):
			return False
		if (not isinstance(amount, (int, float)) or amount < 0):
			return False

		
		# the right object,
		acc_src = None
		for i in self.accounts:
			if 'name' in i.__dict__.keys() and origin == i.name:
				acc_src = i
				break
		if acc_src is None:
			return False
		
		acc_dest = None
		for i in self.accounts:
			if 'name' in i.__dict__.keys() and dest == i.name:
				acc_dest = i
				break
		if acc_dest is None:
			return False
		
		if not isinstance(acc_src, Account) or not isinstance(acc_dest, Account):
			return False
			
		# is corrupted
		lst = acc_src.__dict__.keys()
		# • an attribute starting with b,
		if len([x for x in lst if x[0] == 'b']) > 0:
			return False
		# • no attribute starting with zip or addr,
		if len([x for x in lst if x.startswith('addr')]) == 0:
			return False
		if len([x for x in lst if x.startswith('zip')]) == 0:
			return False
		# name not being a string,
		if not 'name' in lst or not isinstance(acc_src.name, str):
			return False		
		# • id not being an int,
		if not 'id' in lst or not isinstance(acc_src.id, int):
			return False
		# • value not being an int or a float.
		if not 'value' in lst or not isinstance(acc_src.value, (int, float)):
			return False
		# • an even number of attributes,
		if len(acc_src.__dict__) % 2 == 0:
			return False

		# • an attribute starting with b,
		if len([x for x in acc_dest.__dict__.keys() if x[0] == 'b']) > 0:
			return False
		# • no attribute starting with zip or addr,
		if len([x for x in acc_dest.__dict__.keys() if x.startswith('addr')]) == 0:
			return False
		if len([x for x in acc_dest.__dict__.keys() if x.startswith('zip')]) == 0:
			return False
		# name not being a string,
		if not 'name' in acc_dest.__dict__.keys() or not isinstance(acc_dest.name, str):
			return False		
		# • id not being an int,
		if not 'id' in acc_dest.__dict__.keys() or not isinstance(acc_dest.id, int):
			return False
		# • value not being an int or a float.
		if not 'value' in acc_dest.__dict__.keys() or not isinstance(acc_dest.value, (int, float)):
			return False
		# • an even number of attributes,
		if len(acc_dest.__dict__) % 2 == 0:
			return False


		# and stores enough money to complete the transfer.
		if acc_src.value < amount:
			return False
		acc_src.value -= amount
		acc_dest.value += amount
	


	def fix_account(self, name):
		""" fix account associated to name if corrupted
		@name: str(name) of the account
		@return True if success, False if an error occured
		"""
		# ... Your code ...
		# name not being a string,
		if not isinstance(name, str):
			return False
		
		acc = None
		for i in self.accounts:
			if name == i.name:
				acc = i
				break
		if acc is None:
			return False

		if not isinstance(acc, Account):
				return False
		
		
		# # • an attribute starting with b,
		lst = list(acc.__dict__.keys())
		for i in lst:
			if i[0] == 'b':
				acc.__dict__['_'+ i] = acc.__dict__.pop(i)
		
		# • no attribute starting with zip or addr,
		if len([x for x in acc.__dict__.keys() if x.startswith('addr')]) == 0:
			randstr = ''.join(random.choice(string.ascii_letters) for i in range(10))
			acc.__dict__['addr'] = randstr
		if len([x for x in acc.__dict__.keys() if x.startswith('zip')]) == 0:
			randstr = ''.join(random.choice(string.ascii_letters) for i in range(10))
			acc.__dict__['zip'] = randstr

		# • id not being an int,
		if not 'id' in acc.__dict__.keys() or not isinstance(acc.id, int):
			acc.__dict__['id'] = Account.ID_COUNT
			Account.ID_COUNT += 1			
		
		# • value not being an int or a float.
		if not 'value' in acc.__dict__.keys() or not isinstance(acc.value, (int, float)):
			acc.__dict__['value'] = 0

		# • an even number of attributes,
		if len(acc.__dict__) % 2 == 0:
			if 'odd_attr' in acc.__dict__.keys():
				acc.__dict__.pop('odd_attr')
			else:
				acc.__dict__['odd_attr'] = 'odd'



print("test 1\n")
bank = Bank()
bank.add(Account(
    'Smith Jane',
    zip='911-745',
    value=1000.0,
    bref='1044618427ff2782f0bbece0abd05f31'
))
bank.add(Account(
    'William John',
    zip='100-064',
    value=6460.0,
    ref='58ba2b9954cd278eda8a84147ca73c87',
    info=None,
    other='This is the vice president of the corporation'
))
if bank.transfer('William John', 'Smith Jane', 545.0) is False:
    print('Failed')
else:
    print('Success')

print("\n\ntest 2\n")
# bank = Bank()
bank.add(Account(
    'Smith Jane',
    zip='911-745',
    value=1000.0,
    ref='1044618427ff2782f0bbece0abd05f31'
))
bank.add(Account(
    'William John',
    zip='100-064',
    value=6460.0,
    ref='58ba2b9954cd278eda8a84147ca73c87',
    info=None
))
if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
    print('Failed')
    bank.fix_account('William John')
    bank.fix_account('Smith Jane')
if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
    print('Failed')
else:
    print('Success')



print("\n\ntest 3\n")
# bank = Bank()
acc_valid_1 = Account('Sherlock Holmes',
                      zip='NW1 6XE',
                      addr='221B Baker street',
                      value=1000.0)
acc_valid_2 = Account('James Watson',
                      zip='NW1 6XE',
                      addr='221B Baker street',
                      value=25000.0,
                      info=None)

acc_invalid_4 = Account("Douglass",
                        zip='42',
                        addr='boulevard bessieres',
                        value=42)
acc_invalid_1 = Account("Adam",
                        value=42,
                        zip='0',
                        addr='Somewhere')
acc_invalid_2 = Account("Bender Bending RodrÃ­guez",
                        zip='1',
                        addr='Mexico',
                        value=42)
acc_invalid_3 = Account("Charlotte",
                        zip='2',
                        addr='Somewhere in the Milky Way',
                        value=42)
acc_invalid_5 = Account("Edouard",
                        zip='3',
                        addr='France',
                        value=42)

print(bank.add(acc_valid_1))
print(bank.add(acc_valid_2))
if bank.transfer('William John', 'Edourd', 1000.0) is False:
   print('Failed')
   bank.fix_account('William John')
   bank.fix_account('Smith Jane')
# ...
if bank.transfer('William John', 'Sherlock Holmes', 1000.0) is False:
   print('Failed')
else:
   print('Success')

print(acc_valid_1.value)