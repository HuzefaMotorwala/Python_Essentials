hour = int(input("starting time (hours)" ) )
mins = int(input("starting time (minutes)" ) )
dura = int(input("event duration (minutes)" ) )

endhour=hour+(dura//60)
endminute=mins+(dura%60)
endhour=endhour+(endminute//60)
endminute=endminute%60
endhour=endhour%24

print(endhour,endminute,sep=":")





