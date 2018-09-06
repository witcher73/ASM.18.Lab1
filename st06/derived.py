from .base import Base

class Derived(Base):
	def __init__(self):
		super().__init__()
		self.read_field3()

	def read_field3(self):
		self.field3 = input("Field3: ")

	def edit(self):
		super().edit()
		self.read_field3()

	def __str__(self):
		return "Derived({0}, {1}, {2})".format(self.field1, self.field2, self.field3)
