"""
Rozwiązania do laboratorium 1 z Obrazowania Biomedycznego.
"""
import numpy as np

"""
3 - Kwadrat
"""
def square(size, side, start): # start (x, y)
    image = np.zeros((size, size)).astype(np.uint8)
    # image[y, x]
    x, y = start
    image[y:(side+y), x:(side+x)] = 255
    return image

"""
3 - Koło
"""
def midcircle(size):
    x, y = size
    image = np.zeros((y, x)).astype(np.uint8)
    r = int(min(size)/4)
    cx = int(x/2)
    cy = int(y/2)

    for (iy,ix) in np.ndindex(image.shape):
        if (ix - cx)**2 + (iy - cy)**2 <= r**2:
            image[iy, ix] = 255

    return image


"""
3 - Szachownica.
"""
def checkerboard(size):
    rows = 8
    image = np.zeros((size, size)).astype(np.uint8)
    cellsize = size // rows

    for iy in range(rows):
        for ix in range(rows):
            if ix % 2 != iy % 2: # black
                image[iy*cellsize:(iy*cellsize+cellsize), ix*cellsize:(ix*cellsize+cellsize)] = 255
    return image

"""
4 - Interpolacja najbliższych sąsiadów.
"""
def nn_interpolation(source, new_size):
    src = source.shape
    dst = new_size

    h_src, w_src = src
    w_dst, h_dst = dst

    ratio_x = w_src / w_dst
    ratio_y = h_src / h_dst

    image = np.zeros(new_size).astype(np.uint8)

    for (iy, ix) in np.ndindex(image.shape):
        image[iy, ix] = source[int(iy*ratio_y), int(ix*ratio_x)]

    return image

"""
5 - Interpolacja dwuliniowa
"""
def bilinear_interpolation(source, new_size):
    h_src, w_src = source.shape
    w_dst, h_dst = new_size

    ratio_x = w_src / w_dst
    ratio_y = h_src / h_dst

    image = np.zeros(new_size).astype(np.uint8)

    for (iy, ix) in np.ndindex(image.shape):
        y = ratio_y * iy
        x = ratio_x * ix

        y_floor = int(np.floor(y))
        y_ceil = int(np.ceil(y))

        x_floor = int(np.floor(x))
        x_ceil = int(np.ceil(x))

        values = [
            source[y_floor, x_floor],
            source[y_ceil, x_floor],
            source[y_floor, x_ceil],
            source[y_ceil, x_ceil],
        ]

        x_fraction = x - np.floor(x)
        y_fraction = y - np.floor(y)

        a = x_fraction
        b = y_fraction

        fa0 = (1-a)*values[0] + a*values[2]
        fa1 = (1-a)*values[1] + a*values[3]

        fab = (1-b)*fa0 + b*fa1
        image[iy, ix] = int(fab)

    return image

