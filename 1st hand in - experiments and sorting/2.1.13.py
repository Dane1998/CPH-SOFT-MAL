import random


#Intialising a bunch of stuff
diamond_list = []
clubs_list = []
spades_list = []
heart_list = []
sorted_cards = []
cards = [
    (1,"Heart"),
    (2, "Heart"),
    (3,"Heart"),
    (4, "Heart"),
    (5,"Heart"),
    (6, "Heart"),
    (7,"Heart"),
    (8, "Heart"),
    (9,"Heart"),
    (10, "Heart"),
    (11,"Heart"),
    (12, "Heart"),
    (13,"Heart"),
    (1, "Clubs"),
    (2,"Clubs"),
    (3, "Clubs"),
    (4,"Clubs"),
    (5, "Clubs"),
    (6,"Clubs"),
    (7, "Clubs"),
    (8,"Clubs"),
    (9, "Clubs"),
    (10,"Clubs"),
    (11, "Clubs"),
    (12,"Clubs"),
    (13, "Clubs"),
    (1,"Diamond"),
    (2, "Diamond"),
    (3,"Diamond"),
    (4, "Diamond"),
    (5,"Diamond"),
    (6, "Diamond"),
    (7,"Diamond"),
    (8, "Diamond"),
    (9,"Diamond"),
    (10, "Diamond"),
    (11,"Diamond"),
    (12, "Diamond"),
    (13,"Diamond"),
    (1, "Spades"),
    (2,"Spades"),
    (3, "Spades"),
    (4,"Spades"),
    (5, "Spades"),
    (6,"Spades"),
    (7, "Spades"),
    (8,"Spades"),
    (9, "Spades"),
    (10,"Spades"),
    (11, "Spades"),
    (12,"Spades"),
    (13, "Spades")
]

def shuffle(my_list):
    random.shuffle(my_list)
    return my_list


def sort_helper(my_list):
    for i in range(len(my_list)):
        min_idx = i
        for j in range(i+1, len(my_list)):
            if my_list[min_idx] > my_list[j]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list

def sort_cards(my_list):
    for element in my_list:
        if "Diamond" in element:
            diamond_list.append(element)
        if "Clubs" in element:
            clubs_list.append(element)
        if "Spades" in element:
            spades_list.append(element)
        if "Heart" in element:
            heart_list.append(element)

    sorted_cards.append(sort_helper(spades_list))
    sorted_cards.append(sort_helper(heart_list))
    sorted_cards.append(sort_helper(clubs_list))
    sorted_cards.append(sort_helper(diamond_list))

    return sorted_cards

print(sort_cards(shuffle(cards)))

#This is a very bad way of doing this, especially if you look at how the program is set up, but it works as intended