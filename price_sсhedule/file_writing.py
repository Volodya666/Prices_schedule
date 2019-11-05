from input_file import inputed_prices, inputed_names, inputed_colors


prices = open("prices.txt", "a")
for price in inputed_prices:
    prices.write(str(price) + "\n")
prices.close()
prices = open("prices.txt", "r")
all_prices = []
for line in prices:
    all_prices += [line.replace("\n", "")]
prices.close()


names = open("names.txt", "a")
for curr_name in inputed_names:
    names.write(curr_name + "\n")
names.close()
names = open("names.txt", "r")
all_names = []
for curr_name2 in names:
    all_names.append(curr_name2.replace("\n", ""))
names.close()


colors = open("colors.txt", "a")
for curr_col in inputed_colors:
    colors.write(curr_col + "\n")
colors.close()
colors = open("colors.txt", "r")
all_colors = []
for curr_col2 in colors:
    all_colors.append(curr_col2.replace("\n", ""))
colors.close()