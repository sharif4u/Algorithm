#arraList
shopping_list = ["beef", "rice", "daal"]
print(shopping_list)

int_list = [0,1,2,3,4,5]
print(int_list[-1]) # its called slicing to find out last item on list
#print first four
print(int_list[:2]) #startIndex:endIndex-1

#find maximum, minimum, sum, averagevalue of list
maxValue = max(int_list)
minValue = min(int_list)
sumValue = sum(int_list)
print(maxValue)
print(minValue)
print(sumValue)

#find maximum value with coding or sorting code
myList = [1,4,3,5,6,45,3,34,54]
maxvalue = myList[0]
for val in myList:
  if(val > maxValue):
    maxValue = val
print(maxValue)
