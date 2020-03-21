import logging
class Logsetup:
    @staticmethod
    def getlogreg():
        logging.basicConfig(filename=".\\Logs folder\\registration.log",format='%(asctime)s: %(levelname)s: %(message)s %(funcName)s %(lineno)d',datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
    @staticmethod
    def getlogaddlogin():
        logging.basicConfig(filename=".\\Logs folder\\login.log",format='%(asctime)s: %(levelname)s: %(message)s %(funcName)s %(lineno)d',datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
    @staticmethod
    def getlogshop():
        logging.basicConfig(filename=".\\Logs folder\\shopping.log",format='%(asctime)s: %(levelname)s: %(message)s %(funcName)s %(lineno)d',datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger