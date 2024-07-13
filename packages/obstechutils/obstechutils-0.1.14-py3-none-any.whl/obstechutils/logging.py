import logging
from logging import FileHandler, StreamHandler, LogRecord, Logger
import sys
import io
from types import FunctionType
from typing import Callable, Union
from functools import wraps
from pathlib import Path
from datetime import datetime

class OutputLogger(io.TextIOBase):

    def __init__(
        self, 
        logger: logging.Logger,  
        output_name: 'stdout',
        level: int = logging.INFO
    ) -> None:
        
        super().__init__()
        self.output_name = output_name
        self.logger = logger
        self.level = level

    def __enter__(self):
        self.original_stream = getattr(sys, self.output_name)
        setattr(sys, self.output_name, self)

    def __exit__(self, _x, _y, _z):
        setattr(sys, self.output_name, self.original_stream)

    def write(self, s) -> None:
        if s := s.strip():
            self.logger.log(self.level, f"logger: {s}")
    
def log_output(
    fun: Callable = None, 
    *, 
    loggername: str = __name__,
    logger: Union[logging.Logger, None] = None,
    stdout_level: int = logging.INFO, 
    stderr_level: int = logging.ERROR
):
    """

If a function uses print or yields some output, capture it and log it
using the logging module.

Optional keyword arguments:
    * logger:  logger, by default root legger logging
    * stdout:  logging level of the standard output (by default INFO)
    * stderr:  logging level of the standard error (by default ERROR)

"""
    if logger is None:
        logger = logging.getLogger(loggername)

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            with OutputLogger(logger, 'stdout', level=stdout_level):
                with OutputLogger(logger, 'stderr', level=stderr_level):
                    return f(*args, **kwargs)
        
        return wrapper

    if fun:
        return decorator(fun)

    return decorator

class PeriodicFileHandler(FileHandler):
    
    def __init__(
        self, 
        pattern: str, 
        mode: str='a', 
        encoding: str = None, 
        delay: bool = False
    ) -> None:
       
        self.pattern = pattern
        filename = datetime.now().strftime(self.pattern)

        super().__init__(filename, mode, encoding, delay)

    def emit(
        self, 
        record: LogRecord
    ) -> None:

        date = datetime.fromtimestamp(record.created)
        new_filename = datetime.now().strftime(self.pattern)

        if self.stream is None:
            self.baseFileName = new_filename
        elif self.baseFilename != new_filename:
            self.close()
            self.baseFileName = new_filename

        super().emit(record)

def getDailyLogger(
    name: str = 'root',
    basename: str = 'dailylog', 
    path: Path = Path('.'), 
    format: str = '%(asctime)s %(levelname)-5s %(message)s',
    datefmt: str = '%Y-%m%dT%I:%M:%S',
    level: int = logging.INFO,
):
    """Change logfile daily"""
    
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s", 
        datefmt="%Y-%m%dT%I:%M:%S",
        encoding='utf8',
        level=level,
    )

    logger = logging.getLogger(name)
    path.mkdir(parents=True, exist_ok=True)
    pattern = f"{path}/{basename}-%Y%m%d.log"
    filehandler = PeriodicFileHandler(pattern)
    formatter = logging.Formatter(format, datefmt)
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger

