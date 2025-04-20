m = int(input("Enter your number : "))

def checkIfpower(m):

    if(m<=0):
        return False
    while m%8 == 0:
      m = m//8
    return m == 1 
if checkIfpower(m):
   print("Is a power of 8 ")
else:
   print("Is not a power of 8 ")