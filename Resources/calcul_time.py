from datetime import datetime
import time

t1 = datetime.now()
time.sleep(10)
t2 = datetime.now()

timediff = (t2-t1).seconds

print(timediff)
