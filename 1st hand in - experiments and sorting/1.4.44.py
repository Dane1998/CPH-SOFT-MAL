import random

def birthday_problem(n):
    my_list = []
    for i in range(n):
        real_number = random.randint(0, n-1)
        my_list.append(real_number)
    return my_list




def validate_hypothesis(list):
    oc_set = set()
    res = []
    for idx, val in enumerate(list):
        if val not in oc_set:
            oc_set.add(val)
        else:
            res.append(idx)
    return res[0]  



def test_hypothesis(n):
    idx_list = []
    for i in range(n):
        idx = validate_hypothesis(birthday_problem(365))
        idx_list.append(idx)
    average_idx = sum(idx_list) / len(idx_list)
    return f"The average number of generated integers until duplicate is found is : {average_idx}. Compared to the hypothesis of 23,93"

print(test_hypothesis(100))
