#Find the non repeated character from the given string...
input_str="iiinnsso"
for char in input_str:
  print(char)
  if input_str.count(char)==1:
    print("char is", char)
    break