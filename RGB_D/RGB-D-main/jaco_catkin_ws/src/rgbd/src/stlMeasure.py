#!/usr/bin/python

# Python script to find STL dimensions
# Requrements: sudo pip install numpy-stl

import math
import stl
from stl import mesh
import numpy

import os
import sys
directory = "~/ryan_do_not_touch/src/rgbd/src"

# this stolen from numpy-stl documentation
# https://pypi.python.org/pypi/numpy-stl

# find the max dimensions, so we can know the bounding box, getting the height, width and length
def find_mins_maxs(stl_file_name):
    print(os.getcwd())
    prev_dir = os.getcwd()
    print(prev_dir)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.abspath(os.getcwd()))
    if not os.path.exists(stl_file_name):
        sys.exit('ERROR: file %s was not found!' % stl_file_name)
    main_body = None
    temp = sys.stdout
    sys.stdout = None 
    try:      
        main_body = mesh.Mesh.from_file(stl_file_name) #this prints a statement, since an exception is raised, but it is recoverable and does just fine
        sys.stdout = temp
    except:
        sys.stdout = temp
        print('exception')
        the_type, the_value, the_traceback = sys.exc_info()
        #print(the_type)
        #print(the_value)
        #print(the_traceback)

    sys.stdout = temp
    minx = None
    maxx = None
    miny = None
    maxy = None
    minz = None
    maxz = None
    for p in main_body.points:
        # p contains (x, y, z)
        if minx is None:
            minx = p[stl.Dimension.X]
            maxx = p[stl.Dimension.X]
            miny = p[stl.Dimension.Y]
            maxy = p[stl.Dimension.Y]
            minz = p[stl.Dimension.Z]
            maxz = p[stl.Dimension.Z]
        else:
            maxx = max(p[stl.Dimension.X], maxx)
            minx = min(p[stl.Dimension.X], minx)
            maxy = max(p[stl.Dimension.Y], maxy)
            miny = min(p[stl.Dimension.Y], miny)
            maxz = max(p[stl.Dimension.Z], maxz)
            minz = min(p[stl.Dimension.Z], minz)
    #assume that stl dimenstions are in [mm] (most common convention), this converts it to [m]
    minx = minx/1000
    maxx = maxx/1000
    miny = miny/1000
    maxy = maxy/1000
    minz = minz/1000
    maxz = maxz/1000
    #switch the order to account for different orientation
    temp = miny
    miny = minz
    minz = temp
    temp = maxy
    maxy = maxz
    maxz = temp
    print ("X: %f" % (float(maxx) - float(minx)))
    print ("Y: %f" % (float(maxy) - float(miny)))
    print ("Z: %f" % (float(maxz) - float(minz)))
    os.chdir(prev_dir)
    print(os.getcwd())

    return minx, maxx, miny, maxy, minz, maxz

#minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(sys.argv[1])

# the logic is easy from there
if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        sys.exit('Usage: %s [stl file]' % sys.argv[0])
    
    if not os.path.exists(sys.argv[1]):
        sys.exit('ERROR: file %s was not found!' % sys.argv[1])

    minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(sys.argv[1])
    print ("File: %s" % sys.argv[1])
    print ("X: %f" % (float(maxx) - float(minx)))
    print ("Y: %f" % (float(maxy) - float(miny)))
    print ("Z: %f" % (float(maxz) - float(minz)))
