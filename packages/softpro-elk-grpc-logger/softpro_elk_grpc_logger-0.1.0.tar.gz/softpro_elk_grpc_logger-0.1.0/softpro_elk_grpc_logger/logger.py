import logging
import json
from datetime import datetime


class StructuredMessage:
    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        return json.dumps({
            'time': datetime.utcnow().isoformat(),
            'message': self.message,
            **self.kwargs
        })


def setup_logger(log_filename='structured.log'):
    logger = logging.getLogger("StructuredLogger")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger