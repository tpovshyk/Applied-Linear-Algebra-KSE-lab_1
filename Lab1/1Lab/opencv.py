import numpy as np
import cv2
import matplotlib.pyplot as plt


def plot_objects(objects, titles):
    fig, axs = plt.subplots(1, len(objects), figsize=(10, 5))
    if len(objects) == 1:
        axs = [axs]
    for i, obj in enumerate(objects):
        axs[i].plot(obj[:, 0], obj[:, 1], 'o-')
        axs[i].set_title(titles[i])
        axs[i].set_xlabel('x')
        axs[i].set_ylabel('y')
        axs[i].axis('equal')
    plt.show()

# Трикутник
obj_t = np.array([[0, 0], [1, 0], [0.5, 1], [0, 0]])

# Зірочка
obj_s = np.array([[0, 0.5], [0.25, 0.2], [0.5, 0], [0.15, -0.25], [0, -0.5],
                [-0.2, -0.3], [-0.55, 0.1], [-0.3, 0.25], [0, 0.5]])


def rotate(obj, angle):
    center = tuple(np.mean(obj, axis=0))
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    transformed_obj = cv2.transform(np.array([obj]), rotation_matrix)
    return transformed_obj[0]


def scale(obj, sx, sy):
    center = tuple(np.mean(obj, axis=0))
    scaling_matrix = np.array([[sx, 0, center[0] * (1 - sx)], [0, sy, center[1] * (1 - sy)]])
    transformed_obj = cv2.transform(np.array([obj]), scaling_matrix)
    return transformed_obj[0]


def reflect(obj, axis):
    if axis == 'x':
        reflection_matrix = np.array([[1, 0], [0, -1]])
    elif axis == 'y':
        reflection_matrix = np.array([[-1, 0], [0, 1]])
    transformed_obj = cv2.transform(np.array([obj]), reflection_matrix)
    return transformed_obj[0]


def shear(obj, k, axis):
    if axis == 'x':
        shear_matrix = np.array([[1, k, 0], [0, 1, 0]])
    elif axis == 'y':
        shear_matrix = np.array([[1, 0, 0], [k, 1, 0]])
    transformed_obj = cv2.transform(np.array([obj]), shear_matrix)
    return transformed_obj[0]

rotated_triangle = rotate(obj_t, 30)
plot_objects([rotated_triangle], ['Rotated Triangle2'])

scaled_triangle = scale(obj_t, 2, 1)
plot_objects([scaled_triangle], ['Scaled Triangle2'])

reflected_triangle = reflect(obj_t, 'y')
plot_objects([reflected_triangle], ['Reflected Triangle2'])

sheared_triangle = shear(obj_t, 2, 'y')
plot_objects([sheared_triangle], ['Sheared Triangle2'])

rotated_star = rotate(obj_s, 45)
plot_objects([rotated_star], ['Rotated Star2'])

scaled_star = scale(obj_s, 2, 3)
plot_objects([scaled_star], ['Scaled Star2'])

reflected_star = reflect(obj_s, 'x')
plot_objects([reflected_star], ['Reflected Star2'])

sheared_star = shear(obj_s, 1, 'x')
plot_objects([sheared_star], ['Sheared Star2'])



