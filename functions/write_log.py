from datetime import datetime
from dotenv import load_dotenv
import os

# Filter the date and current time
current_time = datetime.now().strftime('%Y-%m-%d %X')

load_dotenv()
working_directory = os.getenv("WORKING_DIRECTORY")

# Function to log messages in .txt files with the current timestamp
def log_message(file_name,message):
    with open(f"{working_directory}/data/{file_name}.txt", "a") as file:
        file.write(f"{current_time} {message}\n")