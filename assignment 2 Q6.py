# Assignment 2
# Question 6

arr=[]
sum_=0
print ("u have to enter the length of three sides\n")
for i in range (3):
  print (f" enter {i+1}th side\n")
  arr. append (input ()) 
  sum_+=int(arr[i])
count=1
for j in arr:
   if int(j)>=(sum_ -int(j)):
    count=0
if count==1:
  print ("Yes")
else :
  print ("No")