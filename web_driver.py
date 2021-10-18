import threading
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class SingletonDoubleChecked(object):

    __singleton_lock = threading.Lock()
    __singleton_instance = None

    # define the classmethod
    @classmethod
    def instance(cls):

        # check for the singleton instance
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()

        # return the singleton instance
        return cls.__singleton_instance


class Driver:
    options = None
    driver = None

    def __init__(self):
        pass

    def add_args(self):
        raise NotImplementedError

    def get_driver(self):
        raise NotImplementedError


class ChromeDriver(SingletonDoubleChecked, Driver):

    def __init__(self, arguments):
        self.options = webdriver.ChromeOptions()
        self.add_args(arguments)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)

    def add_args(self, arguments):
        for arg in arguments:
            self.options.add_argument(arg)

    def get_driver(self):
        return self.driver
