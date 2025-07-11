# write a function that computes the distance between two points on a graph
import math
import argparse

parser = argparse.ArgumentParser(description='Provides distance between two points on a xy-plane')
parser.add_argument('x1', type= int, help='Value of X from point 1')
parser.add_argument('y1', type= int, help='Value of Y from point 1')
parser.add_argument('x2', type= int, help='Value of X from point 2')
parser.add_argument('y2', type= int, help='Value of Y from point 2')

arg = parser.parse_args()

def graph_dist(x1,y1,x2,y2):
	dist = math.sqrt(((x1+x2)**2)+((y1+y2)**2))
	print(dist)


graph_dist(arg.x1,arg.y1,arg.x2,arg.y2)
