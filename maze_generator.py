# Imports
from random import shuffle, randint
import os
import numpy as np
from PIL import Image
from time import sleep


def breadth_first_generation(width=64, height=64, name='image.jpg'):
    """
    Making a maze.
    Each cell starts out with all 4 walls.
    We choose random cell and start with choosing random unvisited neighbor,
    until there are no more and then we return by the stack to the last such one,
    deleting walls along the way.

    Based on the breadth first search. Therefore the maze has a lot of long paths.
    """
    # making a matrix of visited cells
    visited = [[True]*(width+2)] + [[True] + ([False] * width) + [True] for _ in range(height)] + [[True]*(width+2)]

    # Making a pixel-like matrix of cells and walls
    # 255 is white color, 0 is black color
    matrix = [[255]*(2*width + 5)]*3
    for _ in range(height):
        matrix += [[255, 255, 255] + [0, 255] * width + [255, 255]]
        matrix += [[255]*(2*width+5)]
    matrix += [[255]*(2*width + 5)]*2

    def walk(x, y):
        # Create a stack, push the chosen cell in there, mark it visited
        stack = []
        visited[y][x] = True
        stack.append((x, y))

        while len(stack) > 0:
            # Pop the cell from the stack
            x, y = stack.pop(-1)

            # translate the coordinates into real pixel cells
            real_x, real_y = 2*x+1, 2*y+1

            # generate a random move to the neighbor cell
            d = [((x-1, y), (real_x-1, real_y)),
                 ((x, y+1), (real_x, real_y+1)),
                 ((x+1, y), (real_x+1, real_y)),
                 ((x, y-1), (real_x, real_y-1))]
            shuffle(d)

            # Go over each of the neighboring cells
            for choice in d:
                xx, yy = choice[0]
                real_xx, real_yy = choice[1]

                # If the neighboring cell was visited, go to the next one
                if visited[yy][xx]:
                    continue

                # Remove the wall between the cells, push the current cell and
                # the chosen cell to the stack. Mark it visited
                matrix[real_yy][real_xx] = 0
                stack.append((x, y))
                stack.append((xx, yy))
                visited[yy][xx] = True

        # generate a live image from the array
        npmatrix = np.array(matrix)
        print(npmatrix)
        image = Image.fromarray(npmatrix.astype('uint8'))
        image.save(name)

    walk(1, 1)


def main():
    breadth_first_generation()


if __name__ == '__main__':
    main()
