import cv2
import matplotlib.pyplot as plt


def plot_image(image, title):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()


def rotate_image(image, angle):
    height, width = image.shape[:2]
    center = (width, height)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image


def scale_image(image, sx, sy):
    scaled_image = cv2.resize(image, None, fx=sx, fy=sy, interpolation=cv2.INTER_LINEAR)
    return scaled_image


def reflect_image(image, axis):
    if axis == 'x':
        reflected_image = cv2.flip(image, 0)
    elif axis == 'y':
        reflected_image = cv2.flip(image, 1)
    return reflected_image

image = cv2.imread('image.jpeg')

rotated_image = rotate_image(image, 30)
plot_image(rotated_image, 'Rotated Image')

scaled_image = scale_image(image, 2, 1)
plot_image(scaled_image, 'Scaled Image')

reflected_image = reflect_image(image, 'y')
plot_image(reflected_image, 'Reflected Image')

