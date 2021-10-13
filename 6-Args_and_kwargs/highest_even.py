annotation = "Caculate the higest even nubmer in a list"
print(annotation)
def higest_even(*number_list):
  result_sum = sum(number_list)
  even_value = result_sum / len(number_list)
  higest_even_number = number_list[0]
  min_even_value = abs(higest_even_number - even_value)
  for item in number_list:
    differ = abs(even_value - item)
    if differ < min_even_value:
      higest_even_number = item
      min_even_value = differ
  print(f"The higest even number is {higest_even_number}, differ is {min_even_value} with even value {even_value}, and this number index is {number_list.index(higest_even_number)}")
  return higest_even_number
   
higest_even(1, 2, 3, 8)

