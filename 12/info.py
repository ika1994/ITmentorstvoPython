import psutil


memory=psutil.virtual_memory()
print(f"{memory[0]/(1024**3):.2f}GB")