import matplotlib.pyplot as plt
def plot_objects(objects, titles):
    fig, axs = plt.subplots(1, len(objects))
    if len(objects) == 1:
        axs = [axs]
    for i, obj in enumerate(objects):
        axs[i].plot(obj[:, 0], obj[:, 1], 'o-')
        axs[i].set_title(titles[i])
        axs[i].set_xlabel('x')
        axs[i].set_ylabel('y')
        axs[i].axis('equal')
    plt.show()

def plot_3d_object(points, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(points[:, 0], points[:, 1], points[:, 2], 'o-')
    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()

def print_matrix(matrix, title):
    print(f"{title}:\n{matrix}\n")