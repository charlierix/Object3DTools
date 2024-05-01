# "tester2.py" -s 1 -m True -f "D:\models\!research\texture to vertex\violin.glb"

import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sub_count", help="Number of subdivisions (making extra triangles)", type=int, default=0)
parser.add_argument("-m", "--multi_obj", help="True: each object becomes its own .obj file.  False: a single .obj is created (argparse with bool is counterintuitive.  Don't pass -m for false, pass -m True for true.  Passing -m False will still be True)", type=bool, default=False)
parser.add_argument("-f", "--file", help="The 3D object file to process (that is texture mapped)", required=True)
args = parser.parse_args()

print("sub_count: " + str(args.sub_count))
print("multi_obj: " + str(args.multi_obj))
print("file: " + args.file)