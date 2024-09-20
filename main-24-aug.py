# list in python:
#a list is a collection of items that can be of any data type
#lists are denoted by square

#ex.1
'''nums = [1,2,3,4,5,6]
print(type(nums))
# outpput: <class 'list'>

#ex.2
mylist = [23, 7.23,True,"jayrj","923"]
print(mylist)
'''
#ex.3
'''a=[23,45,56,78,89]
print("List :",a)
print(a[1])
print(a[-4])
'''
#ex.4
'''b =[33,11,77,99,88]
print("List :",b)
print("Sorted list :",b.sort())
print("List :",b)
print("Sorted list :",b.sort(reverse=True))
print("List :",b)
'''

#ex.5
# removal of element
'''mylist = [2,4,,3,6,7]
print("Original list :",mylist)
mylist[2] = 8
print("List after Modify :",mylist)
mylist.remove(6)
mylist.remove(4)
'''
#ex.6
'''mylist =[2,4,3,6,7]
print("Original list :",mylist)

mylist.append(9)
print("list after append :",mylist)

mylist.insert(2,8)
print("list after insert :",mylist)
'''
#ex.7
mylist = [2,4,3,6,7,4,7,9,2,5]
print("Index of 9 :",mylist.index(9))

#ex.8
mylist =[3,5,6,8,9,5,2,5]
print("Count of 5 ",mylist.count(5))

#ex.9

mylist = [3,4,7,8,9,10]
print("max element :",max(mylist))
print("min element :",min(mylist))

#ex.10

mylist = [3,5,6,8,9]
print("sum element:",sum(mylist))

#ex.11
# reverse:
mylist = [2, 4, 3, 6, 7, 4]
print("Original list : ", mylist)
mylist.reverse()
print("List after reverse",mylist)

