
class StringReprMixin:

    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class A(StringReprMixin):
    def __init__(self, nome):
        self.x = 10
        self.y = 20


a = A('Ivan')
print(a)
