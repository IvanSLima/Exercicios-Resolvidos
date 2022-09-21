from sre_constants import CATEGORY_NOT_DIGIT


class Animal:
    def make_noise(self) -> None:
        raise NotImplementedError(' Voce deve implementar make_noise ')

    def move(self) -> None:
        raise NotImplementedError(' Voce deve implementar Move')


class Dog(Animal):
    def make_noise(self) -> None:
        print('Au Au')


class Cat(Animal):
    def make_noise(self) -> None:
        print(' MIAU MIAU ')


dog = Dog()
dog.make_noise()

cat = Cat()
cat.make_noise()
