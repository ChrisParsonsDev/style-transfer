#!/usr/bin/env python
# coding: utf-8

import os
import sys
import torch

content_image_file = ""
style_image_file = ""


#Main method for allowing parameter Updating
def main(argv):

    if len(argv) < 6:
        sys.exit("Not enough arguments provided.")

    global content_image_file, style_image_file, training_iters

    i = 1
    while i <= 3:
        arg = str(argv[i])
        if arg == "--contentImageFile":
            content_image_file = str(argv[i+1])
        elif arg == "--styleImageFile":
            style_image_file = str(argv[i+1])
        elif arg =="--trainingIters":
            training_iters = int(argv[i+1])
        i += 2

if __name__ == "__main__":
    main(sys.argv)
