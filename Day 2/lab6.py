#You have 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way. How long will the bus journey take? Alternatively, you could run to uniersity. You jog the first mile at 7mph: then run the next two at 15mph: before jogging teh last at 7mph 
#again. Will this be quicker or slower than the bus?

distance=4
x=25
#bus stops at 10 places and spent 2 minutes
stop_time =10*2
e=1/x
t=e*60
total_time=t + stop_time
print(f"The total time to reach university by bus{total_time}")

#the runs with the speed of 7 mph
y=7
f=1/y
time_1=f*60
z=15
g=2/z
time_2=g*60
a=7
h=1/a
time_3=h*60
total_time2=time_1+time_2+time_3
print(f"the total time for walking is {total_time2}")

if total_time2>total_time:
    print("Walking is faster to reach the university")