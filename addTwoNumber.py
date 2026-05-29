l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]



l1_string = "".join([str(num) for num in l1[::-1]])
l2_string = "".join([str(num) for num in l2[::-1]])

result = str(int(l1_string) + int(l2_string))[::-1]


print([int(num) for num in result])

