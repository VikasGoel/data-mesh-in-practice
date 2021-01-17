

def grant_access(user = "no_user", dataset = "no_dataset", access="no_access"):
	if user == "no_user":
		print("User name needed, try to provide user=\"user\" as argument.")
		return
	if " " in user:
		print("User name should only be one word.")
		return
	if not user.islower():
		print("User name should be all lowercase.")
		return
	if user != "mschultze":
		if "schultze" in user:
			print("User names are constructed from the first letter of first name + the full last name.")
			return
		else:
			print("Please note, the function only works for the user from the exercise request \"Max Schultze\".")
			return
	if user == "mschultze":
		print("Correct user name!")
		if dataset == "no_dataset":
			print("Please provide a dataset by specifying dataset=\"dataset\" as additional parameter.")
			return
		if " " in dataset:
			print("Dataset should not contain any spaces.")
			return
		if not dataset.islower():
			print("Dataset should be all lowercase.")
			return
		if dataset != "order_positions":
			if "order" in dataset and "positions" in dataset:
				print("Datasets can contain \'_\' as word separator.")
				return
			else:
				print("Please note, the function only works for the dataset from the exercise request \"Order Positions\".")
				return
		if dataset == "order_positions":
			print("Correct dataset!")
			switcher = {
				"no_access": "Please provide access mode by specifying access=\"access\" as additional parameter.",
				"read": "Read access has been granted.",
				"write": "Are you sure the user needs write permissions? Maybe \"read\" is enough.",
				"full": "Are you sure the user needs full permissions? Maybe \"read\" is enough."
			}
			print(switcher.get(access, "Invalid access method. Available options: full, write, read"))
			return




if __name__ == '__main__':
	#grant_access()
	#grant_access(user="Max Schultze")
	#grant_access(user="MaxSchultze")
	#grant_access(user="maxschultze")
	#grant_access(user="awider")
	#grant_access(user="mschultze")
	#grant_access(user="mschultze", dataset="Order Positions")
	#grant_access(user="mschultze", dataset="OrderPositions")
	#grant_access(user="mschultze", dataset="orderpositions")
	#grant_access(user="mschultze", dataset="articles")
	#grant_access(user="mschultze", dataset="order_positions")
	#grant_access(user="mschultze", dataset="order_positions", access="test123")
	grant_access(user="mschultze", dataset="order_positions", access="read")
