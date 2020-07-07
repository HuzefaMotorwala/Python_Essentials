def isleapyear(year):
  if year%400==0 and year%100==0 or year%4==0:
    return True
  else:
    return False
  
testdata=[1900,2000,2016,1987]
testresult=[False,True,True,False]
yr=testdata[i]
print(yr,"=",end="")
result=isleapyear(yr)
if result==testresult[i]:
  print("ok")
else:
  print("Failed")
