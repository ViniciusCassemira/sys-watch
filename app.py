from datetime import datetime

# Filter the date and current time
current_time = datetime.now().strftime('%d/%m/%Y - %X')

# Function to log messages with the current timestamp
def log_message(message):
    with open("<your-project-path>/sys-watch/data/logs.txt", "a") as file:
        file.write(f"[{current_time}]: {message}\n")

log_message("testing")
