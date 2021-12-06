#you live 4 miles from university.
#the bus drives at 25 mph but spends 2 minutes at each of the 10 stops on the way. how long will the bus journey take?
#Alternatively, you could run to university. you jog the first mile at 7mph: then run the next two at 15mph; 
#before jogging the last at 7mph again. will this be quicker or slowerthan the bus?

distance=4
velocity=25
time1=(distance/velocity)*60
#the bus spend two minutes in each ten steps so 2+10
time2=20
total=time1+time2 #total time taken by bus to reach university
print(f"total time by bus is {total}")

#When jogging
j1=((1/7)*60)
j2=((2/15)*60)
j3=((1/7)*60)
total2=j1+j2+j3  #total time taken by jogging to reah university
print(f"total time taken by run or jog is {total2}")
if total>total2:
    print("going by bud is slower than running")
else:
    print("going on foot is quicker than by going by bus")

