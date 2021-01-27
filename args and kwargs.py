#args


def add_nums(*nums):
    result = 0
    for num in nums:
        result += num
    return result/len(nums)

list1 = [11, 12, 13]
list2 = [14, 15]
list3 = [16, 17, 18, 19]

print(add_nums(*list1, *list2, *list3))


## ** kwargs

def new_list(**words):
    result = []

    for word in words.values():
        result.append(word)
    return result

print(new_list(a="Python", b="is", c="Fun"))
