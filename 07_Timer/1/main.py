import time

t = int(input("Enter the time in seconds: "))

while (t >= 0):
    mins, secs = divmod(t, 60)
    hrs, mins = divmod(mins, 60)
    timer = '{:02d} : {:02d} : {:02d}'.format(hrs, mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1
    
print('\ntime is up')
		