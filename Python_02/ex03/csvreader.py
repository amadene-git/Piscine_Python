class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		
		try:
			self.fileobj = open(filename, "r")
		except FileNotFoundError:
			raise Exception("CsvReader error: File not found.")
		except PermissionError:
			raise Exception("CsvReader error: Permission denied.")

		self.filename		= filename
		self.sep 			= sep
		self.header 		= header
		self.skip_top 		= skip_top
		self.skip_bottom 	= skip_bottom
		self.data			= []
		
		self.text = self.fileobj.read()

		return None

	def __enter__(self):
		# ... Your code here ...
		if not hasattr(self, 'fileobj'):
			print ("Error fileobj")
			return None
		
		for i in list(filter(None, self.text.split("\n"))):
			self.data.append(i.split(self.sep))
			if len(self.data[0]) != len(self.data[self.data.index(i.split(self.sep))]):
				# raise Exception("CsvReader error: File corrupted, mistmatch between number of fields and number of records.")
				return None

		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				if not (i == 0 and self.header == True) and len(self.data[i][j]) != len(self.data[len(self.data) - 1][j]):
					# raise Exception("CsvReader error: File corrupted, records with different length.")
					return None
		
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				self.data[i][j] = list(filter(None, self.data[i][j].split(' ')))

		return self


	def __exit__(self, exc_type, exc_val, exc_tb):
		# ... Your code here ...
		if not hasattr(self, 'fileobj'):
			print ("Error fileobj")
			return None


		self.fileobj.close()

		return None
	
	
	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
		nested list (list(list, list, ...)) representing the data.
		"""
		# ... Your code here ...
		return [x for x in self.data if (self.data.index(x) >= self.skip_top + self.header\
										 and self.data.index(x) < len(self.data) - self.skip_bottom)\
										 or (self.header == True and self.data.index(x) == 0)]
	
	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
		list: representing the data (when self.header is True).
		None: (when self.header is False).
		"""
	
		if self.header:
			return self.data[0]
		else:
			return None
	# ... Your code here ...



import sys

if __name__ == "__main__":
	with CsvReader(sys.argv[1], skip_top=1, header=True, skip_bottom=0) as file:
		if file == None:
			print("File corrupted.")
		else:
			data = file.getdata()
			# for i in data:
			# 	print(i)
			header = file.getheader()
			# print(header)

