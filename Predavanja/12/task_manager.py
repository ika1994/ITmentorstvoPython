import psutil
import time
i=0
print(psutil.cpu_count())
processes =list(psutil.process_iter())

for proces in processes:
    proces.cpu_percent(interval=None)

time.sleep(1)
for proces in processes:
    i+=1
    print(f"{i}\t{proces.name()}\t{proces.memory_percent():.2f}\t{proces.cpu_percent()}")
