import random


def coupon_collector_problem(n):
    my_set = set()
    my_list = []
    while len(my_set) != n:
        number = random.randint(0, n-1)
        if number not in my_set:
            my_set.add(number)
        else:
            my_list.append(number)
    total_amount = len(my_set) + len(my_list)
    #print(f"The amount of integers generated to fill the set was {total_amount}")
    return total_amount


def get_average(n, size_of_set):
    my_list = []
    for i in range(n):
        amount = coupon_collector_problem(size_of_set)
        my_list.append(amount)
    average = sum(my_list) / len(my_list)
    print(f"The amount of integers to fill the set of {size_of_set} was on average {average}")
    print("The hypothesis states that with a set that has the size of 10, it should take roughly 29,29 tries")
    return average

get_average(1000, 10)