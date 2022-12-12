class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		print("__init__")
		
		try:
			self.fileobj = open(filename, "r")
		except FileNotFoundError:
			print("CsvReader error: File not found", file=sys.stderr)
			return None
		except PermissionError:
			print("CsvReader error: Permossion denied", file=sys.stderr)
			return None

		self.filename		= filename
		self.sep 			= sep=','
		self.header 		= header=False
		self.skip_top 		= skip_top=0
		self.skip_bottom 	= skip_bottom=0
		self.data			= []
		
		self.text = self.fileobj.read()
		
	def __enter__(self):
		# ... Your code here ...
		print("__enter__")
		if not hasattr(self, 'fileobj'):
			print ("Error fileobj")
			return None
		
		self.data = self.text.split("\n")

		for i in self.data:
			self.data = i.split(",")
		
		return self.fileobj


	def __exit__(self, exc_type, exc_val, exc_tb):
		# ... Your code here ...
		print("__exit__")
		if not hasattr(self, 'fileobj'):
			print ("Error fileobj")
			return None


		self.fileobj.close()
	
	
	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
		nested list (list(list, list, ...)) representing the data.
		"""
		# ... Your code here ...
	
	
	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
		list: representing the data (when self.header is True).
		None: (when self.header is False).
		"""
	# ... Your code here ...


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True

import sys

if __name__ == "__main__":
	with CsvReader(sys.argv[1]) as file:
		print(f"CsvReader({sys.argv[1]})")

# with File(sys.argv[1], 'r') as opened_file:
# 	print("file opened")