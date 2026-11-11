import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debug message")
logging.info("Application started")
logging.warning("Something might be wrong")
logging.error("Login failed")
logging.critical("Application crashed")