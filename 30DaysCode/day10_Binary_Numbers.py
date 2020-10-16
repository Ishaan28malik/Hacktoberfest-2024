count_dict, count, Last_item = {}, 0, None
binario = str(bin(int(input())))

binary_list = [n for n in binario]
for item in binary_list:
    if Last_item != item:
        Last_item = item
        count = 1
    else:
        count += 1

    if count > count_dict.get(item, 0):
        count_dict[item] = count

print(count_dict.get('1'))
