# Assignmen 2
# Question 4

max_=0
print ("u have to enter three numbers\n")
for i in range (3):
  print (f"enter {i+1}st number\n")
  x=input()
  max_=max(max_,int(x))
print (f"maximum of the three numbers = {max_}")