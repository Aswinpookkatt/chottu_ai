import logging
from logging.handlers import RotatingFileHandler

def get_logger(name=__name__):
    """
    Configures and returns a reusable logger instance.
    """
    logger = logging.getLogger(name)
    
    # Prevents duplicate logs if get_logger is called multiple times
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # 5 MB file size limit, keeps 3 backups
        handler = RotatingFileHandler(
            'app.log', 
            maxBytes=5 * 1024 * 1024, 
            backupCount=1
        )
        
        # Simple format: Timestamp - Module Name - Message
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
    return logger
