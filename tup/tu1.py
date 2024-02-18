#in Tuple we can have any  type of data
#list and tuple like same but the difference is immutable, we can't change value 
#tuple startwith (  only
#Tuple will not allow to insert, append or add anything

#Smple tuple
my_tuple=(1,20.2,"Chand")
print(my_tuple[0])

#Differnce between list and tuple , sets

my_list=[1,20.2,"Chand"]

my_set={1,20.2,"Chand"}

print(my_tuple)
print(my_list)
print(my_set)


#my_tuple[0]=1.0 #<= Tuple will not allow  (immutable)
#my_set[0]=1.0 #<= Set Element can't be directly accessable
#my_list[0] =1.0 # This will allow

print(my_list)


#Count of value occurance
print(my_tuple.count("Chand"))

#Get of index of value
print(my_tuple.index("Chand"))