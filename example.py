#!/usr/bin/python
import sys
from scipy import misc

import matplotlib.pyplot as plt

# http://www.scipy-lectures.org/advanced/image_processing/


if __name__ == "__main__":
    if len(sys.argv) > 1:
        pic_path = sys.argv[1]
        picarray = misc.imread(pic_path)
    else:
        picarray = misc.face()

    print len(picarray)
    print len(picarray[0])
    print len(picarray[0][1])

    # This is a bad slow example
    for y in range(len(picarray)):
        for x in range(len(picarray[0])):
            r = picarray[y][x][0]
            # g = picarray[y][x][1]
            # b = picarray[y][x][2]
            picarray[y][x] = [r, 0, 0]

    plt.imshow(picarray)
    plt.show()
