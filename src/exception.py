import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Generate detailed error message with file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback info
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file name
    line_number = exc_tb.tb_lineno  # Get the line number where the error occurred
    
    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"
    return error_message

class CustomException(Exception):
    """
    Custom exception to handle and log detailed error messages.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initialize the CustomException with a detailed error message.
        """
        # Generate the detailed error message
        self.error_message = error_message_detail(error_message, error_detail)
        
        # Log the error
        logging.error(self.error_message)
        
        # Pass the error message to the parent class
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message
