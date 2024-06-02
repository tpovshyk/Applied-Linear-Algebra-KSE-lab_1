import numpy as np
from transformations import rotate, scale, reflect, shear, custom_transform, rotate_3d, scale_3d
from visualization import plot_objects, plot_3d_object, print_matrix


def program_p1():
    while True:
        print(" Об'єкт для трансформації:")
        print("")
        print("1. Трикутник")
        print("2. Зірка")
        print("3. Піраміда")
        print("")
        choice = input("Введіть номер об'єкта (1/2/3): ")

        if choice == '1':
            obj = np.array([[0, 0], [1, 0], [0.5, 1], [0, 0]])
        elif choice == '2':
            obj = np.array([[0, 0.5], [0.25, 0.2], [0.5, 0], [0.15, -0.25], [0, -0.5],
                            [-0.2, -0.3], [-0.55, 0.1], [-0.3, 0.25], [0, 0.5]])
        else:
            obj = np.array([[0, 0, 0], [1, 0, 0], [0.5, 1, 0], [0.5, 0.5, 1], [0, 0, 0]])

        if choice == '1' or choice == '2':
            print("")
            print("Трансформації:")
            print("1. Обертання (кут у градусах)")
            print("2. Масштабування (коефіцієнт: додатнє дійсне число)")
            print("3. Віддзеркалення (вісь: x або y для 2D)")
            print("4. Нахил (коефіцієнт: дійсне число, вісь: x або y для 2D)")
            print("5. Кастомна матриця трансформації (матриця 2x2)")
            print("")
            transform_choice = input("Введіть першу літеру трансформації (O/M/B/H/K): ")
        else:
            print("")
            print("Трансформації для 3D:")
            print("1. Обертання (кут у градусах)")
            print("2. Масштабування (коефіцієнт: додатнє дійсне число)")
            print("3. Кастомна матриця трансформації (матриця 3x3)")
            print("")
            transform_choice = input("Введіть першу літеру трансформації (O/M/K): ")

        if transform_choice == 'O':
            angle = float(input("Введіть кут обертання: "))
            if choice == '1' or choice == '2':
                transformed_obj = rotate(obj, angle)
                print_matrix(transformed_obj, 'Rotated Object Matrix')
                plot_objects([transformed_obj], ['Rotated Object'])
            else:
                axis = input("Введіть вісь обертання (x/y/z): ")
                transformed_obj = rotate_3d(obj, angle, axis)
                print_matrix(transformed_obj, 'Rotated Object Matrix')
                plot_3d_object(transformed_obj, 'Rotated Object')

        elif transform_choice == 'M':
            if choice == '1' or choice == '2':
                factor = float(input("Введіть коефіцієнт масштабування: "))
                transformed_obj = scale(obj, factor)
                print_matrix(transformed_obj, 'Scaled Object Matrix')
                plot_objects([transformed_obj], ['Scaled Object'])
            else:
                factors = list(
                    map(float, input("Введіть коефіцієнти масштабування для осей x, y, z через пробіл: ").split()))
                transformed_obj = scale_3d(obj, factors)
                print_matrix(transformed_obj, 'Scaled Object Matrix')
                plot_3d_object(transformed_obj, 'Scaled Object')

        elif transform_choice == 'B':
                axis = input("Введіть вісь віддзеркалення (x/y): ")
                transformed_obj = reflect(obj, axis)
                print_matrix(transformed_obj, 'Reflected Object Matrix')
                plot_objects([transformed_obj], ['Reflected Object'])

        elif transform_choice == 'H':
                shear_factor = float(input("Введіть коефіцієнт нахилу: "))
                axis = input("Введіть вісь нахилу x/y): ")
                transformed_obj = shear(obj, shear_factor, axis)
                print_matrix(transformed_obj, 'Sheared Object Matrix')
                plot_objects([transformed_obj], ['Sheared Object'])

        else:
            if choice == '1' or choice == '2':
                matrix = []
                for i in range(2):
                    row = list(map(float, input(f"Введіть рядок {i + 1} матриці (2 елементи через пробіл): ").split()))
                    matrix.append(row)
                matrix = np.array(matrix)
                transformed_obj = custom_transform(obj, matrix)
                print_matrix(transformed_obj, 'Custom Transformed Object Matrix')
                plot_objects([transformed_obj], ['Custom Transformed Object'])
            else:
                matrix = []
                for i in range(3):
                    row = list(map(float, input(f"Введіть рядок {i + 1} матриці (3 елементи через пробіл): ").split()))
                    matrix.append(row)
                matrix = np.array(matrix)
                transformed_obj = custom_transform(obj, matrix)
                print_matrix(transformed_obj, 'Custom Transformed Object Matrix')
                plot_3d_object(transformed_obj, 'Custom Transformed Object')

        cont = input("Бажаєте продовжити? (y/n): ")
        if cont != 'y':
            break
program_p1()