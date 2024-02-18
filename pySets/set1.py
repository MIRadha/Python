#Sets will keep unique values only
#Sets will autoatically to elements in assending order only
#WE can't directly access the value from sets sets{0}
set1={1,2,2,3,3,3,4}
print("This will print unique value only",set1)

#Create a set without values
set1=set()
print(set1)


#Create a set with values

set1={8,10}
print(set1)


#Adding new element
set1.add(-1)
set1.add(2)
print(set1)

#Remove first element
set1.pop()
#set1.add(2)
print(set1)

#Remove value
set1.remove(-1)
#set1.add(2)
print(set1)

#Union Operator

Set_a={"mon","tue","wed","thu","fri"}

Set_b={"wed","thu","sun","sat","mon"}

Set_Union=Set_a | Set_b
print(Set_Union)


#Intersection

Set_Inter=Set_a & Set_b

print(Set_Inter)