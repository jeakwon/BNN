class Base:
    def __init__(self):
        self.ID = None

    def __str__(self):
        return f'{self.__class__.__name__}({self.ID})'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.ID})'