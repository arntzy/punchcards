#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image


def get_pixel_2d_array(image, rows, cols):
    pixels = list(image.getdata())
    #  print(len(pixels))
    pixels_list = []
    for row in range(rows):
        pixel_row = []
        for column in range(cols):
            coord = row * cols + column
            # print(coord)
            pixel_row.append(pixels[coord])
        pixels_list.append(pixel_row)
    return pixels_list


def row_to_string(row):
    return "".join(map(convert_to_binary, row))


def convert_to_binary(pixel):
    #  print(pixel)
    if pixel[0] < 128:
        return "1"
    else:
        return "0"


if __name__ == "__main__":
    im = Image.open("./get_an_a.jpeg")

    # convert to black and white
    #  im = im.convert("1")

    #  im.save("./hello_bw.jpg")
    # resize to the grid size of the graph paper
    im = im.resize((8, 8))
    im.save("./hello_resize.jpg")

    pixlist = get_pixel_2d_array(im, 8, 8)
    #  print(pixlist[5][2])
    #  print(row_to_string(pixlist[1]))

    for row in pixlist:
        binary_string = row_to_string(row)
        #  print(binary_string)
        value = int(binary_string, 2)
        #  print(value)
        print(chr(value))
