class MatrixLab:
    def execute(self):
        try:
            matrix_b = [
                [-10, 20, 30],
                [40, 50, 60],
                [70, -80, 90]
            ]

            print("Початкова матриця B:")
            for row in matrix_b:
                print(row)
            print("-" * 40)

            # перша дія
            rows_b = len(matrix_b)
            cols_b = len(matrix_b[0])

            matrix_c = []

            for i in range(cols_b):
                new_row = []
                for j in range(rows_b):
                    new_row.append(matrix_b[j][i])
                matrix_c.append(new_row)

            print("Матриця C (після транспонування):")
            for row in matrix_c:
                print(row)
            print("-" * 40)

            # друга дія
            final_sum = 0
            rows_c = len(matrix_c)
            cols_c = len(matrix_c[0])

            for j in range(cols_c):
                current_column = []
                for i in range(rows_c):
                    current_column.append(matrix_c[i][j])

                if j % 2 == 0:
                    smallest_number = min(current_column)
                    final_sum = final_sum + smallest_number
                    print("Стовпець", j, "(парний), найменше число:", smallest_number)
                else:
                    biggest_number = max(current_column)
                    final_sum = final_sum + biggest_number
                    print("Стовпець", j, "(непарний), найбільше число:", biggest_number)

            print("-" * 40)
            print("Фінальний результат (сума):", final_sum)

        except IndexError:
            print("Помилка: вийшли за межі матриці. Перевірте її розмір.")
        except TypeError:
            print("Помилка: неправильний тип даних.")
        except Exception as error:
            print("Сталася помилка під час виконання:", error)


if __name__ == "__main__":
    my_lab = MatrixLab()
    my_lab.execute()
