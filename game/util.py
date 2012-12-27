# -*- coding: utf-8 *-*

import math, random

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2
    return image



def random_pos(screensize=(800, 600)):
    """
    returns a random position between 0 and screensize[i]
    >>> random_pos((800, 600, 300))
    [571, 375, 292]
    >>> random_pos((800, 600))
    [14, 324]
    """
    pos = []
    for i, max_dim in enumerate(screensize):
        pos.append(random.randrange(0, max_dim))
    return pos


def distance(pos1, pos2=None):
    """
    Return the distance between 2 points
    or from the origin
    """
    if not pos2:
        pos2 = [0] * len(pos1)
    elif len(pos1) != len (pos2):
        raise TypeError("Different dimensions")

    squaresum = 0
    for i in range(len(pos1)):
        squaresum += (pos1[i] - pos2[i]) ** 2
    return math.sqrt(squaresum)

def angle_to_vector(rotation):
    # rotation in pyglet is negative degrees
    ang = -math.radians(rotation)
    return [math.cos(ang), math.sin(ang)]


def vector_to_angle(vector):
    return -math.degrees(math.atan2(vector[1], vector[0]))


