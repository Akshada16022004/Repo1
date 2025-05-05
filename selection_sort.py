my_arr=[23,56,3,5,8,10]
n=len(my_arr)
for i in range(n):
  min_index=i
  for j in range(i+1,n):
    if my_arr[j]<my_arr[min_index]:
      min_index=j
  my_arr[i],my_arr[min_index]=my_arr[min_index],my_arr[i]
print("sorted array:",my_arr)
      
      
  
      
