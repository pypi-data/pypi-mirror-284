# coding: utf-8
"""日志模块
"""

from log4py import Logger

Logger.set_level("DEBUG")

config = {
    "handlers": {
      "file_handler": {
        "class": "logging.FileHandler", 
        'filename': 'debug.log'
      },
      "stream_handler": {"class": "logging.StreamHandler" }
    },
    "loggers": {
      'default': {"level": "DEBUG", "handlers": ["file_handler", "stream_handler"], 'propagate': False}
    }
}
Logger.configure(**config)
log = Logger.get_logger('default')
