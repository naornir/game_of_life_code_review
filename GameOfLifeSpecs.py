import unittest
import pdb
from GameOfLife import GameOfLife


class TestInitMethod(unittest.TestCase):

    def setUp(self):
        self.game = GameOfLife(5)

    def test_that__it_initializes_board_size(self):
        self.assertEqual(self.game.size, 5)

    def test_that_it_raises_type_error_when_size_is_not_a_number(self):
        with self.assertRaises(TypeError):
            game_without_size = GameOfLife('2')

    def test_that_it_raises_value_error_when_size_is_not_a_number(self):
        with self.assertRaises(ValueError):
            game_without_size = GameOfLife(0)


class TestAddLivingCellMethod(unittest.TestCase):

    def setUp(self):
        self.game = GameOfLife(5)

    def test_that_it_raises_value_error_when_x_is_not_in_range(self):
        with self.assertRaises(ValueError):
            self.game.add_living_cell(5, 0)
    def test_that_it_raises_value_error_when_y_is_not_in_range(self):
        with self.assertRaises(ValueError):
            self.game.add_living_cell(2, 5)
    def test_that_it_raises_value_error_when_both_are_not_in_range(self):
        with self.assertRaises(ValueError):
            self.game.add_living_cell(7, 5)
    def test_that_it_returns_true_when_both_are_good(self):
            self.assertEqual(self.game.add_living_cell(2, 3), True)


class TestIsAlive(unittest.TestCase):

    def setUp(self):
        self.game = GameOfLife(5)
        self.game.add_living_cell(1, 2)
        self.game.add_living_cell(2, 2)
        self.game.add_living_cell(2, 1)

    def test_that_it_returns_false_if_cell_was_not_added(self):
            self.assertEqual(self.game.is_alive(2, 3), False)
    def test_that_it_returns_true_if_cell_was_not_added(self):
            self.assertEqual(self.game.is_alive(1, 2), True)
    def test_that_it_validates_coordinates(self):
        with self.assertRaises(ValueError):
            self.game.is_alive(- 1, 2)



class TestNeighboursCount(unittest.TestCase):

    def setUp(self):
        self.game = GameOfLife(5)
        self.game.add_living_cell(1, 2)
        self.game.add_living_cell(2, 2)
        self.game.add_living_cell(1, 2)


    def test_that_neighbours_count_is_2(self):
        self.game.add_living_cell(0, 2)
        self.assertEqual(self.game.neighbours_count(1, 2), 2)

    def test_that_neighbours_count_is_correct2(self):
        self.assertEqual(self.game.neighbours_count(0, 0), 0)
    def test_that_neighbours_count_is_8(self):
        self.game.add_living_cell(1, 1)
        self.game.add_living_cell(2, 1)
        self.game.add_living_cell(3, 1)

        self.game.add_living_cell(1, 2)
        self.game.add_living_cell(3, 2)

        self.game.add_living_cell(1, 3)
        self.game.add_living_cell(2, 3)
        self.game.add_living_cell(3, 3)
        self.assertEqual(self.game.neighbours_count(2, 2), 8)



class TestUnderPopulation(unittest.TestCase):

    def test_that_cell_with_one_neighbour_dies(self):
        game = GameOfLife(5)
        game.add_living_cell(1, 1)
        game.add_living_cell(2, 1)
        game.add_living_cell(3, 1)

        game.add_living_cell(1, 2)
        game.add_living_cell(3, 2)

        game.add_living_cell(1, 3)
        game.add_living_cell(2, 3)
        game.add_living_cell(3, 3)

        game.add_living_cell(4, 4)

        self.assertEqual(game.neighbours_count(4, 4), 1)
        game.evolve()
        self.assertEqual(game.is_alive(4, 4), False)


if __name__ == '__main__':
    unittest.main()
