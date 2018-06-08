"""
This file shows basic usage of argparse.
"""

import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to image file')
ap.add_argument('-w', '--weights', default='./cnn_weights.dat',
                help='path to weights file')

args = ap.parse_args()
print args.image, args.weights
