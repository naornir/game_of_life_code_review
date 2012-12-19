import pdb  # review: you can use Eclipse' PyDev IDE for debugging if you prefer
import os
import time

"""
Represents a cell on the board of game of life. It's only uses 
are to determine the if and why a cell should live or die 
"""
class Cell:

    # review: it's good practice (although rarely-implemented in our code) is to define the object members with default values at the top 
    # of the class definition for readability. It's also good for a more clean understanding of the datatype of each member. For example:
    #   
    #   class Cell( object ):
    #       neighbours_count = 0    # implies integer
    #       value = False               # implies boolean
    #


    def __init__(self, value, neighbours_count):
        self.neighbours_count = neighbours_count
        self.value = value

    # review: the choice of using @property is a bit unclear to me. Logically, is it a property, or a method? things that starts with "is_" implies
    # it's a method that determines a boolean result, and not part of the state of the object
    @property
    def is_alive_and_should_die_from_under_population(self):
        return self.value == 1 and self.neighbours_count < 2
    
    @property
    def is_alive_and_should_die_by_over_crowding(self):
        return self.value == 1 and self.neighbours_count > 3

    @property
    def is_alive_and_should_stay_alive(self):
        return self.value == 1 and ( self.neighbours_count == 2 or
                                     self.neighbours_count == 3)

    @property
    def is_dead_and_shoule_be_revived_by_reproduction(self):
        return self.value == 0 and self.neighbours_count == 3


"""
Holds the entire logic of Game of life. 
Has functionallity for adding new cells, and evolving due to the rules
of the game
"""
class GameOfLife:


    def __init__(self, size):

        # review: you can use assertions for input validation. For example:
        #   assert isinstance( size, int ) == True, "Size of board should be an Int"
        
        # review: False is an immutable singleton, thus following PEP-8 you can use the `is` comparator. For example:
        #   assert isinstance( size, int ) is True, " ... "

        if isinstance(size, int) == False:
            raise TypeError("size of board should be an integer") # review: great use of specific erros, instead of generic Exception() instance
        elif size < 1:
            raise ValueError("board size should be at least 1")
        else:

            # review: PEP-20, "flat is better than nested".
            # here it's pretty clear that this `else` block will only be executed if the input validation is successful, you can unindent it 
            # out of the if-block.
            self.size = size
            self._build_matrix()

    def _build_matrix(self):
        # Cell that is dead is assigned to value of 0

        # review: a classic place to apply python's amazing list comprehensions for minimalism. For example:
        #   self.board = [ [0] * self.size for i in range( self.size ) ]

        self.board = []
        for i in range(self.size):
            self.board.append([0] * self.size)

    def add_living_cell(self, x, y):
        self._validate_that_coordinate_is_in_range(x)
        self._validate_that_coordinate_is_in_range(y)
        self.board[x][y] = 1 # Cell that is alive is assigned to value of 1
        return True

    def is_alive(self, x, y):
        self._validate_that_coordinate_is_in_range(x)
        self._validate_that_coordinate_is_in_range(y)
        return self.board[x][y] == 1

    def evolve(self):
        cells_to_revive = []
        cells_to_kill = []

        for x_axis in range(self.size):
            for y_axis in range(self.size):

                # review: each call to ._get_cell() creates a new Cell instance. This is hardly good practice or high-performance (and it generates a
                # ton of zombie instances for the GC to clean up. I suggest storing the Cell instances on the game state, instead of the actual values.
                # For exmaple:
                #   self.board[x_axis, y_axis] = Cell( 0 )

                cell = self._get_cell(x_axis, y_axis)

                if cell.is_alive_and_should_die_from_under_population:

                        # review: this is a convention thing: use lists for lists of items, not separate values. Instead, use tuples when you need
                        # separate values. For example:
                        #   cells_to_kill.append( ( x_axis, y_axis ) )
                        # you can then read the values like so:
                        #   for x_axis, y_axis in cells_to_kill
                        #


                        cells_to_kill.append([x_axis, y_axis])
                elif cell.is_alive_and_should_die_by_over_crowding:
                        cells_to_kill.append([x_axis, y_axis])
                elif cell.is_dead_and_shoule_be_revived_by_reproduction:
                        cells_to_revive.append([x_axis, y_axis])

        self._set_these_cells_to(1, cells_to_revive)
        self._set_these_cells_to(0, cells_to_kill)

    def _get_cell(self, x_axis, y_axis):
        return Cell(self.board[x_axis][y_axis],
                    self.neighbours_count(x_axis, y_axis))

    def _set_these_cells_to(self, value_to_set, cells_to_change):

        # review: see my note above (in .evolve()) in regard to using tuples instead of lists. You would be able to minimize the code, and keep it
        # more readable with:
        #   for x, y in cells_to_change:
        #       self.board[ x ][ y ] = value_to_set

        for each_cell in cells_to_change:
            x = each_cell[0]
            y = each_cell[1] 
            self.board[x][y] = value_to_set

    def _validate_that_coordinate_is_in_range(self, coordinate):
        if (coordinate < 0 or coordinate > self.size - 1):
            raise ValueError("board size is " + str(self.size)  + 
                    " and given coordinate is " + str(coordinate))

    def neighbours_count(self, x, y):
        neighbours_count = 0

        # one row above
        neighbours_count += self._get_value_safely(x - 1, y- 1)
        neighbours_count += self._get_value_safely(x, y- 1)
        neighbours_count += self._get_value_safely(x + 1, y- 1)

        # same row
        neighbours_count += self._get_value_safely(x - 1, y)
        neighbours_count += self._get_value_safely(x + 1, y)

        # one row below
        neighbours_count += self._get_value_safely(x - 1, y + 1)
        neighbours_count += self._get_value_safely(x, y + 1)
        neighbours_count += self._get_value_safely(x + 1, y + 1)

        return neighbours_count

    def _get_value_safely(self, x, y):
        try:
            return self.board[x][y]
        except IndexError as err:
            # review: why do you capture `err` if you don't need to use it? You can simple catch the exception type only:
            #   except IndexError:
            #       ...

            return 0 # review: do we want to silently return 0? Don't you prefer to violently raise an error in case a non-standard cell is requested? 

    def _draw_matrix(self):
        for x_axis in range(self.size):
            s = ""
            for y_axis in range(self.size):
                s += str(self.board[x_axis][y_axis]) # review: why do you sometimes use `._get_value_safely()` but not here also? What's the difference between the two?
            print(s)

    def draw_matrix_forever(self):
        while True:
            os.system('clear') # review: +1 :)
            self._draw_matrix()
            self.evolve()
            time.sleep(1)

