import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class DebugInfoFilter(logging.Filter):
    def filter(self, level):
        return level.levelno <= logging.INFO

class WarningErrorFilter(logging.Filter):
    def filter(self, level):
        return level.levelno >= logging.WARNING

debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.setFormatter(formatter)
debug_info_handler.addFilter(DebugInfoFilter())

warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)
warnings_errors_handler.setFormatter(formatter)
warnings_errors_handler.addFilter(WarningErrorFilter())

logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")
