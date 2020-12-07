import csv

dataset = []
with open('generated_data.csv', newline='\n') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='\\')
	for row in csvreader:
		dataset += [row]
	

#print(dataset)


#average basket value
#sum price after discount for each order_id
#average all basket sizes

from decimal import Decimal

basket_values = {}
for record in dataset:
	key = record[0]
	vals = record[7]
	if(vals != "0.00"):
		if(key in basket_values):
			basket_values[key] += Decimal(vals)
		else:
			basket_values[key] = Decimal(vals)

valid_basket_count = len(basket_values)
total_basket_value = Decimal(0)
for key in basket_values:
	total_basket_value += basket_values[key]

print("sum of all sales (after discount): " + str(total_basket_value))
print("valid basket count: " + str(valid_basket_count))

average_basket_value = round(total_basket_value / valid_basket_count,2)

print("average basket value: " + str(average_basket_value))


#total sales per article group (count + value)

article_group_values = {}
article_group_counts = {}
for record in dataset:
	key = record[5]
	val = record[7]
	if key in article_group_values:
		article_group_values[key] += Decimal(val)
		article_group_counts[key] += 1
	else:
		article_group_values[key] = Decimal(val)
		article_group_counts[key] = 1

print("---------article group values---------")
for key in article_group_values:
	print(key + ": " + str(article_group_values[key]))
print("---------article group counts---------")
for key in article_group_counts:
	print(key + ": " + str(article_group_counts[key]))

