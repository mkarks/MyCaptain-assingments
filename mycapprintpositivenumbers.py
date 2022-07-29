list1 = [12,-7,5,64,-14]
pos_nos = list(filter(lambda x: (x >= 0), list1))
print("Positive numbers in the list: ", *pos_nos) 