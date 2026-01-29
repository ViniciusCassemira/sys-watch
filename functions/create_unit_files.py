from dotenv import load_dotenv
import os
from .write_log import log_message

load_dotenv()

# Environment variables
user = os.getenv("USER")
working_directory = os.getenv("WORKING_DIRECTORY")
exec_start = os.getenv("EXEC_START")
on_boot_sec = os.getenv("ON_BOOT_SEC")
on_unit_active_sec = os.getenv("ON_UNIT_ACTIVE_SEC")

# Create unit_files directory if it doesn't exist
unit_files_path = f"{working_directory}/unit_files"
if not os.path.exists(unit_files_path):
    os.makedirs(unit_files_path)
    log_message("logs", "Created unit_files directory.")

def create_service_file():
    if os.path.exists(f"{unit_files_path}/sys_watch.service"):
        log_message("logs", "service file already exists, skipping creation.")
        return

    with open(f"{unit_files_path}/sys_watch.service", "a") as file:
        file.write("[Unit]\n")
        file.write("Description=Simple service for Studies\n")
        file.write("After=local-fs.target\n\n")
        
        file.write("[Service]\n")
        file.write("Type=oneshot\n")
        file.write(f"ExecStart={exec_start} {working_directory}/app.py\n")
        file.write(f"User={user}\n")
        file.write("MemoryMax=200M\n\n")

        file.write("[Install]\n")
        file.write("WantedBy=multi-user.target\n")
    log_message("logs", "service file created successfully.")

def create_timer_file():
    if os.path.exists(f"{unit_files_path}/sys_watch.timer"):
        log_message("logs", "timer file already exists, skipping creation.")
        return

    with open(f"{unit_files_path}/sys_watch.timer", "a") as file:
        file.write("[Unit]\n")
        file.write("Description=Simple Timer for Studies\n\n")
        
        file.write("[Timer]\n")
        file.write(f"OnBootSec={on_boot_sec}\n")
        file.write(f"OnUnitActiveSec={on_unit_active_sec}\n\n")

        file.write("[Install]\n")
        file.write("WantedBy=timers.target\n")
    log_message("logs", "timer file created successfully.")

create_service_file()
create_timer_file()