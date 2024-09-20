#ex.1
from array import*
arr = array("i",[12,34,56,67,78])
print(type(arr))
print(arr)
print(arr.typecode)
print(arr.tolist())
#replace
arr[arr.index(67)]=40
print(arr.tolist())
#append
arr.append(100)
print(arr.tolist())
#insert on any index
arr.insert(3,99)
print(arr.tolist())

#list of element : add in array
#arr.extend([44,55,66])
#print(arr.tolist())

arr.extend({23,45})
print(arr.tolist())

#remove any item
arr.remove(100)
print(arr.tolist())

#remove item using index
arr.pop(1)
print(arr.tolist())
# count
print("occurance(12):",arr.count(12))
#slicing of array
print("array:",arr)
print("slicing of array:",arr[0:len(arr):2])
print("reverse of array:",arr[len(arr)::-1])
arr.reverse()
print("Rev:",arr.tolist())