import psutil

i=0
while i<20:
    i+=1
    cpu_usage=psutil.cpu_percent(interval=1)
    core=psutil.cpu_count(logical=False)
    thred=psutil.cpu_count(logical=True)
    current_process=psutil.Process()
    num_thred=current_process.num_threads()
    print(f"{cpu_usage}\t{core}\t{thred}\t{num_thred}")
    # control + c