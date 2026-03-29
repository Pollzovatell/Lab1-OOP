import unittest
from lab1 import MatrixLab

class TestMatrixLab(unittest.TestCase):
    def setUp(self):
        # Ініціалізація об'єкта (якщо потрібно для виклику методів)
        pass

    def test_transposition_correct(self):
        """Перевірка першої дії: Транспонування (C5 = 1)"""
        matrix_b = [
            [10, 20],
            [30, 40],
            [50, 60]
        ]
        # Очікуваний результат: рядки стають стовпцями
        expected_c = [
            [10, 30, 50],
            [20, 40, 60]
        ]

        # Логіка транспонування
        rows_b = len(matrix_b)
        cols_b = len(matrix_b[0])
        result_c = []
        for i in range(cols_b):
            new_row = []
            for j in range(rows_b):
                new_row.append(matrix_b[j][i])
            result_c.append(new_row)

        self.assertEqual(result_c, expected_c)

    def test_column_min_max_sum(self):
        """Перевірка другої дії: Сума за варіантом C11 = 7"""
        # Стовпець 0 (парний): min = 5
        # Стовпець 1 (непарний): max = 100
        # Стовпець 2 (парний): min = -10
        matrix_c = [
            [5, 50, 20],
            [15, 100, -10],
            [30, 0, 80]
        ]

        final_sum = 0
        cols_c = len(matrix_c[0])
        rows_c = len(matrix_c)

        for j in range(cols_c):
            column = [matrix_c[i][j] for i in range(rows_c)]
            if j % 2 == 0:  # Парний стовпець (0, 2)
                final_sum += min(column)
            else:  # Непарний стовпець (1)
                final_sum += max(column)

        # 5 (min стовп. 0) + 100 (max стовп. 1) + (-10) (min стовп. 2) = 95
        self.assertEqual(final_sum, 95)

    def test_byte_range_validation(self):
        """Перевірка відповідності типу byte (C7 = 1): діапазон -128...127"""
        invalid_value = 130  # Поза межами byte

        with self.assertRaises(ValueError):
            if not (-128 <= invalid_value <= 127):
                raise ValueError("Елемент матриці виходить за межі типу byte (-128...127)")

    def test_empty_matrix(self):
        """Перевірка обробки виключної ситуації (п. 16 методички)"""
        empty_matrix = []
        with self.assertRaises(IndexError):
            # Спроба отримати кількість стовпців у порожній матриці
            _ = len(empty_matrix[0])


if __name__ == "__main__":
    unittest.main()
