# tikzIntersectionCalculator
## Description
This is a calculator which calculates the intersection of a given plane and lines. The special feature about this calculator is that it also copies the intersection point into your buffer in tikz style.
## Usage
You can use it from command line with 
'python tikz.py -p "{0:[10,-2,-2], 1:[10,2,-2], 2:[8,2,2]}" -l "{0:[10,0,0], 1:[5,5,-2]}" -o "{0:[10,0,0], 1:[0,0,0]}"'
the -p is for the plane and -l is for the line and -o is for an optional line

The coordinates are in 3D Space so it is [x, y, z]

If you are unsure about the format you can use:
'python tikz.py"
There will be a little input manager which leads you to input the coordinates step by step
