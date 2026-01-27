from datetime import datetime

# Filter the date and current time
current_time = datetime.now().strftime('%Y-%m-%d %X')

# Function to log messages in .txt files with the current timestamp
def log_message(file_name,message):
    with open(f"/home/vinicius/Dev/sys-watch/data/{file_name}.txt", "a") as file:
        file.write(f"{current_time} {message}\n")