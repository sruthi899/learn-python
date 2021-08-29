def function(mylist):
    mylist.append([1, 2, 3, 4])
mylist = [1, 2, 3, 4]
function(mylist)
print(mylist)

def me(str):
    str = 'v'
    print(str)
str = 's'
me(str)
print(str)

def fun(*arg1):
    print (arg1)
fun(10, 20, 30)

#lamda functions
s = lambda arg1, arg2 : arg1 + arg2
print ("total:" ,s(10,20))

#total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total

# Now you can call sum function
total = sum( 10, 20 )
print ("Outside the function global total : ", total) 
