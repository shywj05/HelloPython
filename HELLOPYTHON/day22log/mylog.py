import logging

class MyLog:
    def __init__(self):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
        self.logger = logging.getLogger('MyLog')
        self.logger.setLevel(logging.DEBUG)
        
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        
        fh = logging.FileHandler(filename="MyLog.log")
        fh.setFormatter(formatter)
        
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)