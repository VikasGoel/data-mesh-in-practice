

def grant_access(user = "no_user", dataset = "no_dataset", access="no_access"):
	print("user: " + user + ", dataset: " + dataset + ", access: " + access)
	if user == "no_user":
		print("user name needed, try to provide user=\"user\" as argument")
		return
	if " " in user:
		print("user name should only be one word")
		return
	if not user.islower():
		print("user name should be all lowercase")
		return
	if user != "mschultze":
		if "schultze" in user:
			print("user names are constructed from the first letter of first name + the full last name")
			return
		else:
			print("please note, the function only works for the user from the exercise request \"Max Schultze\"")
			return
	if user == "mschultze":
		print("correct user name!")
		if dataset == "no_dataset":
			print("Please provide a dataset by specifying dataset=\"dataset\" as additional parameter")
			return
		if " " in dataset:
			print("dataset should only be one word")
			return
		if not dataset.islower():
			print("dataset should be all lowercase")
			return
		if dataset != "order_positions":
			if "positions" in dataset:
				print("datasets can contain \'_\' as word separator")
				return
			else:
				print("please note, the function only works for the dataset from the exercise request \"Order Positions\"")
				return
		if dataset == "order_positions":
			print("correct dataset!")
			switcher = {
				"no_access": "please provide access mode by specifying access=\"access\" as additional parameter",
				"read": "read access has been granted"
			}
			print(switcher.get(access, "invalid access method"))
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
