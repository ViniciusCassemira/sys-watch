import psutil
from functions import log_message

def cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    for i, cpu in enumerate(cpu_percent):
        log_message("cpu_info", f"CPU {i}: {cpu}%")