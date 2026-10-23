import unittest
from Lab1 import Polynomial


class TestPolynomialAllMethods(unittest.TestCase):

    def test_init_and_str(self):
        p1 = Polynomial(0, 2, 0, 5)
        self.assertEqual(str(p1), "5x^3 + 2x")

        p2 = Polynomial([7, -2, 0, 1])
        self.assertEqual(str(p2), "x^3 - 2x + 7")

        p3 = Polynomial([7, -2, 0, -1])
        self.assertEqual(str(p3), "-x^3 - 2x + 7")

        p4 = Polynomial({0: -3, 2: 1, 5: 4})
        self.assertEqual(str(p4), "4x^5 + x^2 - 3")

        p5 = Polynomial(p4)
        self.assertEqual(str(p5), "4x^5 + x^2 - 3")
        self.assertIsNot(p4.coeffs, p5.coeffs)

        self.assertEqual(str(Polynomial(5)), "5")
        self.assertEqual(str(Polynomial(0)), "0")
        self.assertEqual(str(Polynomial([0, 0, 0])), "0")

    def test_repr(self):
        p = Polynomial({5: 4, 2: 1, 0: -3})
        self.assertEqual(repr(p), "Polynomial [-3, 0, 1, 0, 0, 4]")
        self.assertEqual(repr(Polynomial(0)), "Polynomial [0]")

    def test_addition(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([3, 4])

        self.assertEqual(str(p1 + p2), "3x^2 + 6x + 4")
        self.assertEqual(str(p1 + 5), "3x^2 + 2x + 6")
        self.assertEqual(str(5 + p1), "3x^2 + 2x + 6")

        p3 = Polynomial([1, -2, 3])
        p4 = Polynomial([1, 2, -3])
        self.assertEqual(str(p3 + p4), "2")

    def test_subtraction_and_negation(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([3, 4])

        self.assertEqual(str(-p1), "-3x^2 - 2x - 1")
        self.assertEqual(str(p1 - p2), "3x^2 - 2x - 2")
        self.assertEqual(str(p1 - 5), "3x^2 + 2x - 4")
        self.assertEqual(str(5 - p1), "-3x^2 - 2x + 4")

    def test_multiplication(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([3, 4])

        self.assertEqual(str(p1 * p2), "8x^2 + 10x + 3")
        self.assertEqual(str(p1 * 3), "6x + 3")
        self.assertEqual(str(3 * p1), "6x + 3")
        self.assertEqual(str(p1 * 0), "0")

    def test_equality(self):
        self.assertTrue(Polynomial([1, 2, 3]) == Polynomial({0: 1, 1: 2, 2: 3}))
        self.assertTrue(Polynomial(5) == 5)
        self.assertFalse(Polynomial([1, 2]) == 5)

    def test_call(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p(1), 6)
        self.assertEqual(p(0), 1)
        self.assertEqual(p(-2), 9)

    def test_degree(self):
        self.assertEqual(Polynomial([1, 2, 3]).degree(), 2)
        self.assertEqual(Polynomial({0: -3, 5: 4}).degree(), 5)
        self.assertEqual(Polynomial(7).degree(), 0)
        self.assertEqual(Polynomial(0).degree(), 0)

    def test_derivative(self):
        p = Polynomial([7, 5, 2, 4])
        self.assertEqual(str(p.der()), "12x^2 + 4x + 5")
        self.assertEqual(str(p.der(2)), "24x + 4")
        self.assertEqual(str(p.der(3)), "24")
        self.assertEqual(str(p.der(4)), "0")

    def test_iteration(self):
        p = Polynomial({5: 4, 2: 1, 0: -3})
        self.assertEqual(list(p), [(5, 4), (2, 1), (0, -3)])


if __name__ == "__main__":
    unittest.main()
