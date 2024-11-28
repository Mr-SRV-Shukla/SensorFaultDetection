import logging
import os
from datetime import datetime

# Generate time stamp for the log file 
LOG_FILE=f"{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.log"

# define the logs dir
logs_dir=os.path.join(os.getcwd(),"logs")

# Ensure logs dir is there
os.makedirs(logs_dir,exist_ok=True)

# define the full log dir path

LOG_FILE_PATH=os.path.join(logs_dir,LOG_FILE)

# Configuration file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO  # Note: `logging.INFO` is uppercase
)