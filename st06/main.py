from .container import Container

container = Container()

menu = [
	("Add base", container.add_base),
	("Add derived", container.add_derived),
	("Edit item", container.edit_item),
	("Delete item", container.delete_item),
	("Print all", container.print_all),
	("Clear all data", container.clear),
	("Save to file", container.save_to_file),
	("Load from file", container.load_from_file),
]

def print_menu():
	print("\n===========================")
	for i, pair in enumerate(menu, start=1):
		print("{0}: {1}".format(i, pair[0]))
	print("0: Exit")
	print("===========================")

def main():
	while True:
		print_menu()
		try:
			choice = input(">> ")
			if choice == "0":
				return
			print("")
			menu[int(choice) - 1][1]()
		except ValueError:
			print("Incorrect input")
		except Exception as e:
			print(e)

if __name__ == '__main__':
	main()
