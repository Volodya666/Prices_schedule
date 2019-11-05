inputed_prices = []
inputed_names = []
inputed_colors = []

while 1:
    print("If you want to finish input, write 'end' anywhere.")
    name = input("Write product's name:")
    if name == "end":
        break
    inputed_names.append(name)
    color = input("Write chart's color:")
    if color == "end":
        for i in range(len(inputed_names)):
            if i == (len(inputed_names) - 1):
                inputed_names.pop(i)
        break
    inputed_colors.append(color)
    while 1:
        inputed_word = input("Write price:")
        if inputed_word == "end":
            break
        else:
            price = inputed_word
            if price.isdigit():
                price = int(price)
                if price >= 0:
                    inputed_prices += [price]
                else:
                    print("You have written price which is less than 0! HOW IT IS POSSIBLE!?")
            else:
                print("You have written wrong type of price!")