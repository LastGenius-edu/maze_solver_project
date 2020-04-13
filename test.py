from maze_generator import breadth_first_generation


def main():
    for i in range(5):
        breadth_first_generation(name=f'image{i}.jpg')


if __name__ == '__main__':
    main()
