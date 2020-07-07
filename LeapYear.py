def isleapyear(year):
  if year%400==0 and year%100==0 or year%4==0:
    return True
  else:
    return False
  
testdata=[1900,2000,2016,1987]
testresult=[False,True,True,False]
for i in range(len(testdata)):
    yr=testdata[i]
    print(yr,"=",end="")
    result=isleapyear(yr)
    if result==testresult[i]:
        print("Ok")
    else:
        print("Failed")
