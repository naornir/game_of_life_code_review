
# review: module names should be lowered cased. 
# http://www.python.org/dev/peps/pep-0008/#package-and-module-names
# For example:
#   from gameoflife import GameOfLife
from GameOfLife import GameOfLife

# review: move the doc inside the class, allows for better code introspection via the Patterns.__doc__ value and follows PEP 257 (sub of PEP 8) for docstrings
# http://www.python.org/dev/peps/pep-0257/
# 
"""
Static class that returns a few special patterns of 
game of life
"""

# review: in python 3.* the object-model has been changed. For future-compatibility, it's recommended to inheirt from `object`. For example:
#   class Patterns( object ):
#       ...
#
class Patterns:

    # review: static methods are a bit use-less in python because you can achieve the same results via a module-function. Class-methods make more sense if
    # indeed they're related to the relevant class. 
    # See: http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
    #
    # Regardless, I dislike both because they're not really OOP, arguably.
    # See: http://stackoverflow.com/questions/4002201/why-arent-static-methods-considered-good-oo-practice
    # Although this discussion related to Java/Scala, I believe it also applies to other programming languages
    @staticmethod
    def blinker():
        game = GameOfLife(6)
        game.add_living_cell(3, 2)
        game.add_living_cell(3, 3)
        game.add_living_cell(3, 4)
        return game

    @staticmethod
    def toad():
        game = GameOfLife(6)

        game.add_living_cell(2, 2)
        game.add_living_cell(3, 2)
        game.add_living_cell(4, 2)
        
        game.add_living_cell(1, 3)
        game.add_living_cell(2, 3)
        game.add_living_cell(3, 3)
        return game

    @staticmethod
    def beacon():
        game = GameOfLife(6)

        game.add_living_cell(1, 1)
        game.add_living_cell(2, 1)
        game.add_living_cell(1, 2)
        
        game.add_living_cell(4, 3)
        game.add_living_cell(3, 4)
        game.add_living_cell(4, 4)
        return game
