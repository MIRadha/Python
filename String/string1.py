a="Radha"
print(a)
print(a)
# String will not allow us to change value
#a[0]='r' # <= you will get error here  TypeError: 'str' object does not support item assignment

#Concatination

a=a+" is good"
print(a)

#lenght
print(len(a))

#Extact charcter from string
print(a[0])
print(a[len(a)-1])
print(a[-1])

#print Index
print(a.find("a")) # will return first index of character
print(a.find("ha")) # will return first index of string
print(a.find("mm")) # no string found it will return -1

a=a+"\n is very cool"
print(a)
print("is",a.find("\n"))  # it will retrun index oc "is" after \n 
#print("Radha is good and very good".find("d","good",len("Radha is good and very good")))

# a[Start:End:Step] Sicing
print(a[0:])
print(a[0:a.find("\n")])
print(a[0:a.find("\n"):2])
print("Revers "+a[::-1])

#formating with place holder
print('{} is very good '.format("Krishna"))

#formating using variables
x='{} new string'
print(x.format("Result"))

#formating with multiple placeholder
x='{} {} {}'
print(x.format('1','Two','-3'))

#formating with multiple index

x="{1} {0}"
print(x.format("One is now in second place","Two is on first place"))

#formating with multiple placehoder with variables
x="{x2} {x1}"
print(x.format(x1="Rad",x2="ha"))


