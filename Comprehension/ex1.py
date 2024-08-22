integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
z=zip(integer,binary)
binary_dic={key: value for key,value in z}
print(binary_dic)