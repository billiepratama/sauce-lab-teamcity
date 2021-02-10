import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt="%d/%m/%y %I:%M:%S %p %A", filemode="w")
logging.critical("This is critical msg")
logging.error("This is error msg")
logging.warning("This is warning msg")
logging.info("This is info msg")
logging.debug("This is debug msg")
