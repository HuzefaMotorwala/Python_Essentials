myList=[4,5,7,2,3,1,8,6]
swapped=True
while swapped:
  swapped = False  #swapped has not occured
  for i in range(len(myList)-1):
    if myList[i]>myList[i+1]:
      myList[i],myList[i+1]=myList[i+1],myList[i]
      swapped=True
    
print(myList)    














