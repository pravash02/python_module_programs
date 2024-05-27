from loguru import logger
import sys

# logger.debug("Simple logging!")
message = "Simple logging!"

## If you need to output the log to a file
logger.add("s_file.log")
logger.debug("That's it, simple logging!")

## Multi-process security
logger.add("somefile.log", enqueue=True)
logger.debug("That's it, simple logging!")
logger.debug("Just simple logging!")


## Handler/Formatter/Filter
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

## backtrace support
logger.add("out.log", backtrace=True, diagnose=True)

def check_div(c):
    try:
        val = 10/c
    except ZeroDivisionError:
        logger.exception("What?!")

check_div(0)

