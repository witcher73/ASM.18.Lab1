import pickle

from .base import Base
from .derived import Derived

class Container:
	__items = []
	PKL_FILENAME = 'st06/dump.pkl'
	def add_base(self):
		base = Base()
		self.__items.append(base)

	def add_derived(self):
		der = Derived()
		self.__items.append(der)

	def edit_item(self):
		if not self.__items:
			print("No items")
			return
		
		self.print_all()
		try:
			index = int(input("Index of item to be edited (0 to cancel): "))
			if index == 0:
				return
			self.__items[index - 1].edit()
			print("Done!")
		except ValueError:
			print("That doesn't look like a number")
		except IndexError:
			print("Index is incorrect")

	def print_all(self):
		if not self.__items:
			print("No items")
			return
		for i, item in enumerate(self.__items, start=1):
			print("{0}. {1}".format(i, item))

	def delete_item(self):
		if not self.__items:
			print("No items")
			return
		
		self.print_all()
		try:
			index = int(input("Index of item to be deleted (0 to cancel): "))
			if index == 0:
				return
			self.__items.pop(index - 1)
			print("Done!")
		except ValueError:
			print("That doesn't look like a number")
		except IndexError:
			print("Index is incorrect")

	def save_to_file(self):
		with open(self.PKL_FILENAME, 'wb') as f:
			pickle.dump(self.__items, f, -1)
			print("Succesfully saved")

	def load_from_file(self):
		try:
			with open(self.PKL_FILENAME, 'rb') as f:
				self.__items = pickle.load(f)
				print("Succesfully loaded {0} items".format(len(self.__items)))
				if len(self.__items):
					self.print_all()
		except FileNotFoundError:
			print("No saved data found")

	def clear(self):
		self.__items.clear()
		print("It's all gone :(")