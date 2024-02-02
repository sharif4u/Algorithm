#Buuble sort using python
def bubbleSort(array):
  for i in range(len(array)):
    for j in range(0,len(array)-i-1):
      if array[j] > array[j+1]:
        array[j] += array[j+1]
        array[j+1] = array[j] - array[j+1]
        array[j] = array[j] - array[j+1]
arrayData = [1,43,56,45,56,5,3,4,5,23,65,75]

bubbleSort(arrayData)
print("Sorted arrray in achending order: ")
print(arrayData)

#another for time complexity
#Buuble sort using python
def bubbleSort(array):
  for i in range(len(array)):
    swapped = False
    for j in range(0,len(array)-i-1):
      if array[j] > array[j+1]:
        array[j] += array[j+1]
        array[j+1] = array[j] - array[j+1]
        array[j] = array[j] - array[j+1]
        swapped = True
    if not swapped:
      break
arrayData = [1,43,56,45,56,5,3,4,5,11,65,75]

bubbleSort(arrayData)
print("Sorted arrray in achending order: ")
print(arrayData)
