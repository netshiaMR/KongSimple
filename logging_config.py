import logging
import sys

def setup_logging():
    log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(log_format))
    root_logger.addHandler(console_handler)
  
