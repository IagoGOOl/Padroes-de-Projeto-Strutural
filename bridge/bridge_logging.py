import logging

class LoggerBridge:
    def __init__(self, handler):
        self.logger = logging.getLogger("BridgeLogger")
        self.logger.setLevel(logging.DEBUG)
    
        if self.logger.hasHandlers():
            self.logger.handlers.clear()
    
        self.logger.addHandler(handler)
    
    def log(self, message):
        self.logger.debug(message)

def get_console_handler():
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    return console_handler

def get_file_handler():
    file_handler = logging.FileHandler('bridge_log.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    return file_handler

if __name__ == "__main__":
    console_logger = LoggerBridge(get_console_handler())
    console_logger.log("Log message to console.")

    file_logger = LoggerBridge(get_file_handler())
    file_logger.log("Log message to file.")
