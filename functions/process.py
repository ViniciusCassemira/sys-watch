import psutil
from functions import log_message

def all_process_info():
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        log_message("process_info", str(proc.info))
