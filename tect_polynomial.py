import unittest
from Lab1 import Polynomial


class TestPolynomialInitAndStr(unittest.TestCase):

    # --- ТЕСТЫ ДЛЯ __init__ ---

    def test_init_positional_args(self):
        """Polynomial(0, 2, 0, 5)"""
        p = Polynomial(0, 2, 0, 5)
        self.assertEqual(p.coeffs, {3: 5, 1: 2})

    def test_init_list(self):
        """Polynomial([7, -2, 0, 1])"""
        p = Polynomial([7, -2, 0, 1])
        self.assertEqual(p.coeffs, {3: 1, 1: -2, 0: 7})

    def test_init_dict(self):
        """Polynomial({0: -3, 2: 1, 5: 4})"""
        p = Polynomial({0: -3, 2: 1, 5: 4})
        self.assertEqual(p.coeffs, {5: 4, 2: 1, 0: -3})

    def test_init_copy_polynomial(self):
        """Создание копии из другого многочлена"""
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial(p1)
        self.assertEqual(p2.coeffs, {2: 3, 1: 2, 0: 1})
        self.assertIsNot(p1.coeffs, p2.coeffs)

    def test_init_single_number(self):
        """Создание из одного числа"""
        p = Polynomial(5)
        self.assertEqual(p.coeffs, {0: 5})

    def test_init_zeros_cleaning(self):
        """Проверка очистки от лишних нулей"""
        p = Polynomial([0, 0, 0])
        self.assertEqual(p.coeffs, {})

        p2 = Polynomial(1, 0, 0, 0)
        self.assertEqual(p2.coeffs, {0: 1})

    # --- ТЕСТЫ ДЛЯ __str__ ---

    def test_str_subject_examples(self):
        """Примеры прямо из условия задачи"""
        self.assertEqual(str(Polynomial([1, 2, 3])), "3x^2 + 2x + 1")
        self.assertEqual(str(Polynomial({0: -3, 2: 1, 5: 4})), "4x^5 + x^2 - 3")
        self.assertEqual(str(Polynomial(0, 2, 0, 5)), "5x^3 + 2x")
        self.assertEqual(str(Polynomial([7, -2, 0, 1])), "x^3 - 2x + 7")
        self.assertEqual(str(Polynomial([7, -2, 0, -1])), "-x^3 - 2x + 7")

    def test_str_edge_cases(self):
        """Краевые случаи"""
        self.assertEqual(str(Polynomial(0)), "0")
        self.assertEqual(str(Polynomial([0, 0])), "0")

        # Позиционные аргументы (a0, a1, a2)
        self.assertEqual(str(Polynomial(-1, 0, 2)), "2x^2 - 1")
        self.assertEqual(str(Polynomial(1, -1, 1)), "x^2 - x + 1")
        self.assertEqual(str(Polynomial(1, 1)), "x + 1")
        self.assertEqual(str(Polynomial(-1, 1)), "x - 1")
        self.assertEqual(str(Polynomial(0, 1)), "x")
        self.assertEqual(str(Polynomial(0, -1)), "-x")

        # Передача списком [a0, a1, a2]
        self.assertEqual(str(Polynomial([1, -1, 1])), "x^2 - x + 1")

    def test_repr(self):
        self.assertEqual(repr(Polynomial(1, 2, 3)), "Polynomial [1, 2, 3]")
        self.assertEqual(repr(Polynomial(0, 2, 0, 5)), "Polynomial [0, 2, 0, 5]")
        self.assertEqual(repr(Polynomial(0)), "Polynomial [0]")

    def test_eq(self):
        # Сравнение одинаковых многочленов
        self.assertEqual(Polynomial(1, 2, 3), Polynomial(1, 2, 3))

        # Сравнение с учетом очистки нулей
        self.assertEqual(Polynomial(1, 2, 0, 0), Polynomial(1, 2))

        # Разные многочлены
        self.assertNotEqual(Polynomial(1, 2), Polynomial(1, 3))

        # Сравнение с числами
        self.assertEqual(Polynomial(5), 5)
        self.assertEqual(Polynomial(0), 0)
        self.assertNotEqual(Polynomial(1, 2), 5)

    def test_add(self):
        p1 = Polynomial([1, 2, 3])  # 3x^2 + 2x + 1
        p2 = Polynomial([3, 4])  # 4x + 3

        # Сложение двух многочленов
        self.assertEqual(str(p1 + p2), "3x^2 + 6x + 4")

        # Сложение с числом справа и слева
        self.assertEqual(str(p1 + 5), "3x^2 + 2x + 6")
        self.assertEqual(str(5 + p1), "3x^2 + 2x + 6")

        # Сокращение противоположных членов
        p3 = Polynomial([1, -2, 3])
        p4 = Polynomial([1, 2, -3])
        self.assertEqual(str(p3 + p4), "2")

    def test_neg(self):
        """Унарный минус (-p)"""
        p = Polynomial([7, -2, 0, 1])  # x^3 - 2x + 7
        self.assertEqual(str(-p), "-x^3 + 2x - 7")

    def test_sub(self):
        """Бинарное вычитание (p1 - p2)"""
        p1 = Polynomial([1, 2, 3])  # 3x^2 + 2x + 1
        p2 = Polynomial([3, 4])  # 4x + 3

        self.assertEqual(str(p1 - p2), "3x^2 - 2x - 2")

    def test_sub_with_numbers(self):
        """Вычитание с числами справа и слева"""
        p = Polynomial([1, 2, 3])  # 3x^2 + 2x + 1

        # Вычитание числа СПРАВА (p - 5) -> 3x^2 + 2x - 4
        self.assertEqual(str(p - 5), "3x^2 + 2x - 4")

        # Вычитание из числа СЛЕВА (5 - p) -> -3x^2 - 2x + 4
        self.assertEqual(str(5 - p), "-3x^2 - 2x + 4")

    def test_call(self):
        """Вычисление значения многочлена в точке (p(x))"""
        p = Polynomial([1, 2, 3])
        self.assertEqual(p(1), 6)
        self.assertEqual(p(0), 1)
        self.assertEqual(p(-2), 9)
        p_const = Polynomial(5)
        self.assertEqual(p_const(10), 5)

    def test_degree(self):
        """Проверка определения степени многочлена"""
        p1 = Polynomial(1, 2, 3)  # 3x^2 + 2x + 1
        self.assertEqual(p1.degree(), 2)

        p2 = Polynomial({0: -3, 5: 4})  # 4x^5 - 3
        self.assertEqual(p2.degree(), 5)

        p3 = Polynomial(7)  # Константа
        self.assertEqual(p3.degree(), 0)

        p0 = Polynomial(0)  # Нулевой многочлен
        self.assertEqual(p0.degree(), 0)

    def test_der(self):
        """Проверка взятия производной"""
        # P(x) = 4x^3 + 2x^2 + 5x + 7
        p = Polynomial([7, 5, 2, 4])

        # 1-я производная: P'(x) = 12x^2 + 4x + 5
        self.assertEqual(str(p.der()), "12x^2 + 4x + 5")

        # 2-я производная: P''(x) = 24x + 4
        self.assertEqual(str(p.der(2)), "24x + 4")

        # 3-я производная: P'''(x) = 24
        self.assertEqual(str(p.der(3)), "24")

        # 4-я производная: 0 (превышает степень)
        self.assertEqual(str(p.der(4)), "0")

    def test_mul(self):
        """Проверка умножения"""
        p1 = Polynomial([1, 2])  # 2x + 1
        p2 = Polynomial([3, 4])  # 4x + 3

        # (2x + 1)(4x + 3) = 8x^2 + 10x + 3
        self.assertEqual(str(p1 * p2), "8x^2 + 10x + 3")

        # Умножение на число справа и слева
        self.assertEqual(str(p1 * 3), "6x + 3")
        self.assertEqual(str(3 * p1), "6x + 3")

        # Умножение на 0
        self.assertEqual(str(p1 * 0), "0")

    def test_mul(self):
        """Проверка умножения"""
        p1 = Polynomial([1, 2])  # 2x + 1
        p2 = Polynomial([3, 4])  # 4x + 3

        # (2x + 1)(4x + 3) = 8x^2 + 10x + 3
        self.assertEqual(str(p1 * p2), "8x^2 + 10x + 3")

        # Умножение на число справа и слева
        self.assertEqual(str(p1 * 3), "6x + 3")
        self.assertEqual(str(3 * p1), "6x + 3")

        # Умножение на 0
        self.assertEqual(str(p1 * 0), "0")

    def test_iter(self):
        """Проверка итерации по коэффициентам"""
        p = Polynomial({5: 4, 2: 1, 0: -3})
        pairs = list(p)
        self.assertEqual(pairs, [(5, 4), (2, 1), (0, -3)])



if __name__ == "__main__":
    unittest.main()
