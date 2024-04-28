# usage:
# blender -b -P texture_to_vertexcolor.py -- INPUT_PLY OUTPUT_OBJ

#import bpy
import argparse
import sys
import os

index = sys.argv.index('--')
parser = argparse.ArgumentParser(description='Bake texture image to vertex colors')
parser.add_argument('INPUT_PLY', type=str, help='Input PLY File')
parser.add_argument('OUTPUT_OBJ', type=str, help='Output OBJ File')
args = parser.parse_args(sys.argv[index:])















