
my_list=[10,50,60,80] #how to print the list
for n in my_list:
    print(n)

my_list=[1,2,3,4,5] #here using lenght of the list
length=len(my_list)
print("length of the list:",len(my_list))

fruits=["apple","banana"] #here we are using append method 
fruits.append('Orange')
print(fruits)

names=["tulasi","Prabha","ramani"] #here we are using to insert the values
names.insert(2,"devi")
print(names)

student=["harini","vanaja","srujana","srivalli"] #here we are using to remove the student name 
student.remove("vanaja")
print(student)

fruits=["banana","orange"] 
if "sorange" in fruits:
    print(True)
else:
    print("False")

my_list=[10,20,30] # here we are using average method in list
total=0
for i in my_list:
    total+=n
average=total/len(my_list)
print(average)
