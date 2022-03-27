array=[1,2,3,4,5,6,7]
array_len=len(array)
rotate_num = 100%array_len
left_array = array[0:rotate_num]
right_array = array[rotate_num:array_len]
array=right_array+left_array
print(array)
