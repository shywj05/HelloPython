import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)

fh = logging.FileHandler(filename="run.log")
# fh.setLevel(logging.INFO)

logger.addHandler(ch)
logger.addHandler(fh)

logger.critical("critical.")
logger.error("error.")
logger.warning("warning.")
logger.info("info.")
logger.debug("debug.")
