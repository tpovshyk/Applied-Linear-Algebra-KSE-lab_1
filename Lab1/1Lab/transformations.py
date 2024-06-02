import numpy as np

def rotate(points, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
    return points @ rotation_matrix.T


def scale(points, factor):
    scaling_matrix = np.array([[factor[0], 0], [0, factor[1]]])
    return points @ scaling_matrix.T


def reflect(points, axis):
    if axis == 'x':
        reflection_matrix = np.array([[1, 0], [0, -1]])
    elif axis == 'y':
        reflection_matrix = np.array([[-1, 0], [0, 1]])
    return points @ reflection_matrix.T


def shear(points, shear_factor, axis):
    if axis == 'x':
        shear_matrix = np.array([[1, shear_factor], [0, 1]])
    elif axis == 'y':
        shear_matrix = np.array([[1, 0], [shear_factor, 1]])
    return points @ shear_matrix.T


#для 3Д
def rotate_3d(points, angle, axis):
    rad = np.radians(angle)
    if axis == 'x':
        rotation_matrix = np.array([[1, 0, 0], [0, np.cos(rad), -np.sin(rad)], [0, np.sin(rad), np.cos(rad)]])
    elif axis == 'y':
        rotation_matrix = np.array([[np.cos(rad), 0, np.sin(rad)], [0, 1, 0], [-np.sin(rad), 0, np.cos(rad)]])
    elif axis == 'z':
        rotation_matrix = np.array([[np.cos(rad), -np.sin(rad), 0], [np.sin(rad), np.cos(rad), 0], [0, 0, 1]])
    return points @ rotation_matrix.T


def scale_3d(points, factor):
    scaling_matrix = np.diag(factor)
    return points @ scaling_matrix.T


def custom_transform(points, matrix):
    return points @ matrix.T