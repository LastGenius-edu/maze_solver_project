from random import shuffle, randint
import os
import numpy as np
from PIL import Image
from time import sleep


def make_maze(width=16, height=8):
    """
    Making a maze.
    Each cell starts out with all 4 walls.
    We choose random cell and start with choosing random unvisited neighbor,
    until there are no more and then we return by the stack to the last such one,
    deleting walls along the way
    """
    visited = [[True]*(width+2)] + [[True] + ([False] * width) + [True] for _ in range(height)] + [[True]*(width+2)]
    matrix = [[255]*(2*width + 5)] + [[255]*(2*width + 5)] + [[255]*(2*width + 5)]

    print(visited)

    for _ in range(height):
        matrix += [[255, 255, 255] + [0, 255] * width + [255, 255]]
        matrix += [[255]*(2*width+5)]
    matrix += [[255]*(2*width + 5)] + [[255]*(2*width + 5)]

    # for row in matrix:
    #     row_chars = ''
    #     for col in row:
    #         if col:
    #             row_chars += "O"
    #         else:
    #             row_chars += " "
    #     print(row_chars)

    def walk(x, y):
        visited[y][x] = True
        real_x, real_y = 2*x+1, 2*y+1
        d = [((x-1, y), (real_x-1, real_y)),
             ((x, y+1), (real_x, real_y+1)),
             ((x+1, y), (real_x+1, real_y)),
             ((x, y-1), (real_x, real_y-1))]
        shuffle(d)

        for choice in d:
            xx, yy = choice[0]
            real_xx, real_yy = choice[1]

            if visited[yy][xx]:
                continue

            matrix[real_yy][real_xx] = 0

            os.system('cls')

            npmatrix = np.array(matrix)
            image = Image.fromarray(npmatrix.astype('uint8'))
            image.save('image.jpg')

            for row in matrix:
                row_chars = ''
                for col in row:
                    if col:
                        row_chars += "O"
                    else:
                        row_chars += " "
                print(row_chars)

            # sleep(0.2)
            walk(xx, yy)

    walk(randint(0, width-1), randint(0, height-1))


def main():
    # breadth_first_generation(10, 10)
    make_maze()


if __name__ == '__main__':
    main()
