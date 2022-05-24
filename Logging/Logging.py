import logging
import datetime as dt

today = dt.datetime.today()
filename = f"{today.month:02d}-{today.day:02d}-{today.year}.log"

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

logging.log(logging.INFO, "This is our first logging message")
logging.log(logging.DEBUG, "This is our first logging message")
logging.log(logging.CRITICAL, "This is our first logging message")
logging.log(logging.WARNING, "This is our first logging message")

logging.debug("Hello")
logging.info("Hello")
logging.warning("Hello")
logging.critical("Hello")

for handler in logging.root.handlers:
    logging.root.removeHandler(handler)

logger = logging.getLogger("Magikid")

logger.info("This is some information")
logger.log()

file_handler = logging.FileHandler("logfile.log")
file_handler.setLevel(logging.Warning)

formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug("Hey I am debug")
logger.info("Hey I am info")
logger.warning("Hey I am warning")
logger.error("Hey I am error")
logger.critical("Hey I am critical")