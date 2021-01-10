import random
import decimal
import csv

#-------------------------------------------------------------------------------
#-------------------- section to generate article constants --------------------
#-------------------------------------------------------------------------------

#article name, article description, article group
ARTICLES = [["blue sneakers", "these are blue sneakers", "shoes"], ["green sneakers", "wow - green sneakers!", "shoes"], ["red sneakers", "amazing red sneakers", "shoes"], ["yellow sneakers", "these sneakers are yellow", "shoes"], ["orange sneakers", "sneakers of type orange", "shoes"], ["white sneakers", "beautiful white sneakers", "shoes"], ["black sneakers", "great sneakers in black", "shoes"], ["purple sneakers", "these sneakers are purple", "shoes"], ["brown sneakers", "very brown sneakers", "shoes"], ["black boots", "great black boots", "shoes"], ["brown boots", "tracking boots in brown", "shoes"], ["grey boots", "practical grey boots", "shoes"], ["green boots", "classiy green boots", "shoes"], ["blue slippers", "perfect slippers for home", "shoes"], ["black slippers", "perfect slippers for home", "shoes"], ["grey slippers", "perfect slippers for home", "shoes"], ["white slippers", "perfect slippers for home", "shoes"], ["black hiking shoes", "best for outside", "shoes"], ["grey hiking shoes", "best for outside", "shoes"], ["brown hiking shoes", "best for outside", "shoes"], ["brown sandals", "brown sandals for the summer", "shoes"], ["white sandals", "white sandals for the summer", "shoes"], ["black business shoes", "classy black business shoes", "shoes"], ["brown business shoes", "stylish brown business shoes", "shoes"], ["pink business shoes", "pink business shoes for special occasions", "shoes"], ["white business shoes", "high quality white business shoes", "shoes"], ["yellow business shoes", "special business shoes", "shoes"], ["black high heels", "high quality high heels", "shoes"], ["white high heels", "high quality high heels", "shoes"], ["red high heels", "high quality high heels", "shoes"], ["yellow high heels", "high quality high heels", "shoes"], ["pink pumps", "amazing pink pumps", "shoes"], ["blue pumps", "great blue pumps", "shoes"], ["white sport shoes", "the best shoe for your training", "shoes"], ["green sport shoes", "the best shoe for your training", "shoes"], ["yellow sport shoes", "the best shoe for your training", "shoes"], ["purple sport shoes", "the best shoe for your training", "shoes"], ["red sport shoes", "the best shoe for your training", "shoes"], ["blue sport shoes", "the best shoe for your training", "shoes"], ["grey running shoes", "the best shoe for your running", "shoes"], ["purple running shoes", "the best shoe for your running", "shoes"], ["orange running shoes", "the best shoe for your running", "shoes"], ["black slip-ons", "comfortable slip-ons", "shoes"], ["white slip-ons", "comfortable slip-ons", "shoes"], ["grey slip-ons", "comfortable slip-ons", "shoes"], ["blue pool slides", "best for the summer", "shoes"], ["red pool slides", "best for the summer", "shoes"], ["black pool slides", "best for the summer", "shoes"], ["yellow pool slides", "best for the summer", "shoes"], ["THE shoe", "the ultimate shoe", "shoes"], ["black suite", "the classic black suite", "suits"], ["white suite", "the stylish white suite", "suits"], ["yellow suite", "the crazy yellow suite", "suits"], ["pink suite", "the funny pink suite", "suits"], ["green suite", "the natural green suite", "suits"], ["purple suite", "the exciting purple suite", "suits"], ["blue suite", "the deep blue suite", "suits"], ["christmas suite", "the special occasion suit", "suits"], ["tuxedo", "the very special suit", "suits"], ["white shirt", "shirt for all occasions", "suits"], ["red shirt", "shirt for all occasions", "suits"], ["grey shirt", "shirt for all occasions", "suits"], ["black shirt", "shirt for all occasions", "suits"], ["hawaii shirt", "shirt for all occasions", "suits"], ["ugly christmas sweater", "you know you want it", "sweaters"], ["white shorts", "great summer shorts", "trousers"], ["grey shorts", "great summer shorts", "trousers"], ["brown shorts", "great summer shorts", "trousers"], ["black shorts", "great summer shorts", "trousers"], ["beige shorts", "great summer shorts", "trousers"], ["red shorts", "great summer shorts", "trousers"], ["white t-shirt", "white t-shirts are nice", "shirts"], ["black t-shirt", "black t-shirts are great", "shirts"], ["red t-shirt", "red t-shirts are amazing", "shirts"], ["blue t-shirt", "blue t-shirts are perfect", "shirts"], ["branded t-shirt", "a shirt with a brand printed on it", "shirts"], ["blue jeans", "jeans for everyone", "trousers"], ["grey jeans", "jeans for everyone", "trousers"], ["black jeans", "jeans for everyone", "trousers"], ["white skirt", "nice white skirt", "skirts"], ["green skirt", "great green skirt", "skirts"], ["blue skirt", "cool clue skirt", "skirts"], ["black skirt", "dark black skirt", "skirts"], ["black socks", "everyday socks", "socks"], ["blue socks", "everyday socks", "socks"], ["colorful socks", "everyday socks", "socks"], ["red dress", "beautiful evening dress", "dresses"], ["black dress", "beautiful evening dress", "dresses"], ["white dress", "beautiful evening dress", "dresses"], ["purple dress", "beautiful evening dress", "dresses"], ["green dress", "beautiful evening dress", "dresses"], ["blue dress", "beautiful evening dress", "dresses"], ["red hat", "a hat to top it off", "accessoirs"], ["black hat", "a hat to top it off", "accessoirs"], ["yellow tie", "perfect to the yellow suite", "accessoirs"], ["black tie", "perfect to the black suite", "accessoirs"], ["green bag", "a green bag to wear", "accessoirs"], ["black belt", "opens and closes", "accessoirs"], ["brown belt", "opens and closes", "accessoirs"], ["black sunglasses", "cool black sunglasses", "accessoirs"]]

#add random weights to the frequency each article is bought
def generate_weighted_article_ids():
	weighted_article_ids = []
	for article_id in range(100): #0 to 99
		weight = random.randint(1,5)
		weighted_article_ids += [article_id]*weight
	return weighted_article_ids

WEIGHTED_ARTICLE_IDS = generate_weighted_article_ids()

#random original prices between 5.00 and 50.00
def generate_article_original_prices():
	article_original_prices = []
	for article_number in range (100):
		article_original_prices += [random.randrange(500, 5000)/100]
	return article_original_prices

ARTICLE_ORIGINAL_PRICES = generate_article_original_prices()

# add random weights to the number of items bought per order
LINE_NUMBER_COUNT_WEIGHTS = [0]*1 + [1]*30 + [2]*30 + [3]*20 + [4]*15 + [5]*4

# add random discounts between 0 and 50% to each ordered item
DISCOUNT_WEIGHTS = [1]*50 + [0.95]*20 + [0.90]*15 + [0.80]*10 + [0.50]*5


#-------------------------------------------------------------------------------
#-------------------- section for generating order positions -------------------
#-------------------------------------------------------------------------------

#article groups can be randomly empty in 5% of the cases
def add_article_group(article_id):
	empty_group_weight = [0]*1 + [1]*19
	if (random.choice(empty_group_weight) == 0):
		return "null"
	else:
		return ARTICLES[article_id][2]


#non-empty order line
def generate_order_line(order_id, line_number):
	article_id = random.choice(WEIGHTED_ARTICLE_IDS) #each bought article is a random choice factoring in the previously added weights
	article_name = ARTICLES[article_id][0] #reference article name from the input dataset
	article_description = ARTICLES[article_id][1] #reference article description from the input dataset
	article_group = add_article_group(article_id) #reference article group from the input dataset, can be randomly empty in 5% of cases
	original_price = ARTICLE_ORIGINAL_PRICES[article_id] #reference article original price, as previously generated
	discounted_price = round(original_price*random.choice(DISCOUNT_WEIGHTS),2) #actual price factoring in a random discount
	earnings_after_taxes = round(discounted_price*0.81, 2) #earnings after deducting 19% taxes
	order_line = [[
		str(order_id),
		str(line_number),
		str(article_id),
		article_name,
		article_description,
		article_group,
		str(original_price),
		str(discounted_price),
		str(earnings_after_taxes)]]
	return order_line

def generate_orders(number_of_orders):
	order_positions = []
	for order_id in range(1, number_of_orders+1):
		line_numbers = random.choice(LINE_NUMBER_COUNT_WEIGHTS) #randomly select between 0 and 5 items per order. Orders can be empty!
		if line_numbers == 0: #handling of empty orders
			order_positions += [[str(order_id), "", "", "null", "null", "null", "0.00", "0.00", "0.00"]]
		else:
			for line_number in range(1, line_numbers+1):
				order_positions += generate_order_line(order_id, line_number)
	return order_positions

#-------------------------------------------------------------------------------
#------------- section for executing data generation and persisting ------------
#-------------------------------------------------------------------------------
number_of_orders = 10000
records = generate_orders(number_of_orders)
#print(records)

with open('generated_data.csv', 'w', newline='\n') as csvfile:
 	csvwriter = csv.writer(csvfile, delimiter=',',
 							quotechar='\\', quoting=csv.QUOTE_MINIMAL)
 	for record in records:
 		csvwriter.writerow(record)
