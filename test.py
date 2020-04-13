# Imports
from maze_generator import breadth_first_generation
from PIL import Image
import numpy


def main():
    """
    Generates a few new mazes

    :return: None
    """
    for i in range(5):
        breadth_first_generation(name=f'image{i}.jpg')


def astar_algorithm(name):
    """
    Algorithm that is based on my pain and eternal will to die

    :param name: str
    :return: None
    """
    image = Image.open(name)
    image_array = numpy.asarray(image)
    print(image_array)


if __name__ == '__main__':
    main()
    astar_algorithm('image.jpg')
