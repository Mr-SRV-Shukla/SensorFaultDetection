import logging
import os
from datetime import datetime

# Generate a timestamp for the log file
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# Assuming the project root is two levels up from the current directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', ))

# Define the logs directory in the project root
logs_dir = os.path.join(project_root, "logs")
print(f"Logs directory: {logs_dir}")


# Ensure logs dir is there
os.makedirs(logs_dir, exist_ok=True)

# Define the full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

print(f"Log file path: {LOG_FILE_PATH}")
# Log configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO  # Note: `logging.INFO` is uppercase
)

# Test log entry
logging.info("Logger initialized successfully.")
