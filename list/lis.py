#can contain multiple type of objects 
#delcare by using []
lista=['Radha',20,10.34] 
print(lista)

#list allow us to change value
lista[0]="MI Radha"
print(lista)

#list concatination
list2=["Krishna",90.10,20]
list3=lista+list2
print(list3)

#add new element in list
list3.append("another")
print(list3)

#insert at specific position
list3.insert(1,"insert at 1")
print(list3)

#access specfic element
print(list3[5])

#remove last element
list3.pop()
print(list3)

#remove specfic element
list3.pop(1)
print(list3)

#similier to string we have start, stop, step in list
print(list3[1:3])
print(list3[0:6:2])

#reverse list
list4=list3[::-1]
print(list4)