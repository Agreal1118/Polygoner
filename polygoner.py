import sys 
import numpy as np
from random import randint
import main
import scipy.misc
import copy

def check_all_points(vertex_list,size,colour_vector, child):

    #print vertex_list
    
    
    x1, y1 = vertex_list[0][0], vertex_list[0][1]
    x2, y2 = vertex_list[1][0], vertex_list[1][1]
    x3, y3 = vertex_list[2][0], vertex_list[2][1]

    a_12, b_12, c_12 = (x2-x1),(y2 - y1), (y1*(x2-x1)) - (x1*(y2-y1))
    a_13, b_13, c_13 = (x3-x1),(y3 - y1), (y1*(x3-x1)) - (x1*(y3-y1))
    a_23, b_23, c_23 = (x3-x2),(y3 - y2), (y2*(x3-x2)) - (x2*(y3-y2))


    #print a_12,b_12,c_12
    #print a_13,b_13,c_13
    #print a_23,b_23,c_23

    #print a_13,y2
    #print b_13,x2
    
    ex1 = a_12*y3 - (b_12*x3 + c_12)
    ex2 = a_13*y2 - (b_13*x2 + c_13)
    ex3 = a_23*y1 - (b_23*x1 + c_23)

    #print ex1,ex2,ex3

    tru1 = 0
    tru2 = 0
    tru3 = 0
    
        
    for j in xrange(size):
        for k in xrange(size):
            tru = 0

            expe1 = a_12*j - (b_12*k + c_12)
            expe2 = a_13*j - (b_13*k + c_13)
            expe3 = a_23*j - (b_23*k + c_23)

     #       print expe1, expe2, expe3
            
            if (expe1 <= 0) & (ex1 <= 0):
                tru1 = 1
            elif (expe1 >= 0) & (ex1 >= 0):
                tru1 = 1
            else:
                tru1 = 0
                
            if (expe2 <= 0) & (ex2 <= 0):
                tru2 = 1
            elif (expe2 >= 0) & (ex2 >= 0):
                tru2 = 1
            else:
                tru2 = 0
                
            if (expe3 <= 0) & (ex3 <= 0):
                tru3 = 1
            elif (expe3 >= 0) & (ex3 >= 0):
                tru3 = 1
            else:
                tru3 = 0
                
       #     print tru1, tru2, tru3
      #      print "\n"
            tru = tru1+tru2+tru3
            
            if tru == 3:
                child = add_to_child(copy.deepcopy(child), colour_vector,j,k)
                if type(child) == bool:
                    #print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    return False
    #global img
    #img = scipy.misc.imread('image.png')
    #print main.score_children(childi)
    return child


def add_to_child(child, colour_vector,j,k):
    pixel = child[j][k] + colour_vector

    for pixel_value in pixel:
        #print pixel
        if pixel_value >= 255 or pixel_value < 0:
            return False
    
    #child[j][k] = child[j][k] + colour_vector
    child[j][k] = colour_vector
    return child



#print check_all_points([[0,0],[1,3], [4,2]], 6, [10,10,10], np.zeros(([6,6,3] )) )
