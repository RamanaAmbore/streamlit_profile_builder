import logging
from logging.handlers import RotatingFileHandler


def log_setup():
    maxBytes = 40
    backupCount = 1

    log = logging.getLogger('streamlit')
    log.setLevel(logging.DEBUG)
    log.propagate = False
    format = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s", datefmt="%H:%M:%S")

    error_file_handler = RotatingFileHandler(".log/streamlit_error_log.log", maxBytes=maxBytes, backupCount=backupCount)
    error_file_handler.setLevel(logging.INFO)
    error_file_handler.setFormatter(format)
    log.addHandler(error_file_handler)

    debug_file_handler = RotatingFileHandler(".log/streamlit_debug_log.log", maxBytes=maxBytes, backupCount=backupCount)
    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(format)
    log.addHandler(debug_file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(format)
    log.addHandler(stream_handler)

