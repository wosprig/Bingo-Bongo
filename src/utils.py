import numpy as np


def random_from_file(filename):
    file = open(filename, 'r')
    images = file.read().split('\n')
    index = np.random.randint(low=0, high=len(images))
    return images[index]

