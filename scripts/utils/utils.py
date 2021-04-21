# Only import say_hello and say_bye when import *
__all__ = ["say_hello", "say_bye","a"]

def say_hello():
    print("hello")

def say_bye():
    print("Bye")

a=2