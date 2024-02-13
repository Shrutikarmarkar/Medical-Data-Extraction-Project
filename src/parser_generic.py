import abc
class Medical_Parser(metaclass=abc.ABCMeta):
    def __init__(self, text):
        self.text = text

    @abc.abstractmethod
    def parser(self):
        pass
