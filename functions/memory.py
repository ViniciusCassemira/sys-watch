import psutil
from functions import log_message

# Log memory information
mem = psutil.virtual_memory()

def memory_info():
    total_mb = mem.total / (1024 ** 2)
    used_mb = mem.used / (1024 ** 2)
    available_mb = mem.available / (1024 ** 2)

    log_message("memory", f"Total: {total_mb:.2f} MB - Used: {used_mb:.2f} MB - Available: {available_mb:.2f} MB - Memory use: {mem.percent}%")