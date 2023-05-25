dict_1 = {
  "key1": 1,
  "key2": 2,
  "key3": 3,
  "key4": 4,
  "key5": 5
}
new_dict = {int(i[-1]): i for i in dict_1}
print(new_dict)
