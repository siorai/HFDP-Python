from abc import ABC, abstractmethod


class Duck(ABC):
    flyBehavior = None
    quackBehavior = None


### Behaviors ###

# Flying #
class FlyBehavior(ABC):
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly():
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):
    def fly():
        print("I can't fly")


# Quacking #
class QuackBehavior(ABC):
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack():
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack():
        print("<< Silence >>")


class Squeak(QuackBehavior):
    def quack():
        print("Squeak")
