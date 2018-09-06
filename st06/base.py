class Base:
	def __init__(self):
		self.input()

	def __str__(self):
		return "Base({0}, {1})".format(self.field1, self.field2)

	def input(self):
		self.read_field1()
		self.read_field2()

	def read_field1(self):
		self.field1 = input("Field1: ")

	def read_field2(self):
		self.field2 = input("Field2: ")

	def edit(self):
		print("Editing " + str(self))
		self.input()

