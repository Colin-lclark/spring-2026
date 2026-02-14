import segregation
import unittest
from segregation import grid


class TestGrid(unittest.TestCase):

    def test_grid_dimensions(self):
        g = grid(0.4, 0.4, 10, (500, 500))
        self.assertEqual(len(g), 10)
        self.assertEqual(len(g[0]), 10)

    def test_correct_counts(self):
        g = grid(0.4, 0.4, 10, (500, 500))

        red = 0
        blue = 0
        empty = 0

        for row in g:
            for cell in row:
                if cell == "red":
                    red += 1
                elif cell == "blue":
                    blue += 1
                elif cell == "empty":
                    empty += 1

        self.assertEqual(red, 40)
        self.assertEqual(blue, 40)
        self.assertEqual(empty, 20)

def test_percent_of_colors_in_graph():
    return 0


def test_segregation_check():
    return 0

if __name__ == "__main__":
    unittest.main()
    