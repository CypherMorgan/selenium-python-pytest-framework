from framework.utils.logger import get_logger


class BaseClass:

    def get_logger(self):
        return get_logger(self.__class__.__name__)