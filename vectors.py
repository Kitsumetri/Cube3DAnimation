from math import cos, sin, sqrt, pi
import numpy as np


RTX = tuple(" .:!/)(l1Z4H9W8$@")


def vec_len(vector):
    return sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)


def get_color(vector):
    color = round(vec_len(vector) / 2)
    if color < 0:
        color = 0
    if color > len(RTX):
        color = len(RTX)
    return color


def rotation(vector, t):
    t *= 0.2
    matrix_rotate = np.array([[cos(t), sin(t),  0, 0],
                              [-sin(t), cos(t), 0, 0],
                              [0,         0,    1, 0],
                              [0,         0,    0, 1]])
    return vector.dot(matrix_rotate)


def scale(vector, t):
    t *= 0.1
    matrix = np.array([[sin(t), 0,  0, 0],
                       [0, sin(t), 0,  0],
                       [0, 0, sin(t),  0],
                       [0, 0,      0,  1]])
    return vector.dot(matrix)


def x(vector, t):
    t *= 0.25
    matrix = np.array([[1, 0, 0, 20 * sin(t)],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    return vector.dot(matrix)


def y(vector, t):
    t *= 0.1
    matrix = np.array([[],
                       [],
                       [],
                       []])
    return vector.dot(matrix)


def z(vector, t):
    t *= 0.1
    matrix = np.array([[],
                       [],
                       [],
                       []])
    return vector.dot(matrix)
