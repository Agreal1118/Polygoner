import sys 
import numpy as np
import scipy.misc
from matplotlib import pyplot as plt
from random import randint
from PIL import Image, ImageDraw
import polygoner
import codecs
import math
import copy


def create_random_individual_polygon(parent):

    #max_vertex = 3
    child = False
    while type(child) == bool:
        vertex_list = []
    
        #vertex = 3

        while len(vertex_list) < 3:
            cord = [randint(0,size-1),randint(0,size-1)]
            if cord not in vertex_list:
                vertex_list.append(cord)
    
    #vertex_list.sort()
    #child = False
    #while type(child) == bool:
        #colour_vector = np.random.randint(-255,255, size = 3)
        colour_vector = np.random.randint(0,255, size = 3)
        child = polygoner.check_all_points(vertex_list,size, colour_vector, parent)
        #print type(child)
        
    #print parent
    #print score_children(child)
    #scipy.misc.imsave('end.png',child)
    #print score_children(parent)
    return child
    
def score_children(children_img):
    score = 0.0
    
    for i in xrange(len(img)):
        for j in xrange(len(img[i])):
            #print i
            #print j
            #print children_img[i][j]
            #print img[i][j]
            #score +=    ((sum(children_img[i][j])*1.0) - (sum(img[i][j]))) * ((sum(children_img[i][j])*1.0) - (sum(img[i][j])))       

            #get delta per color
            #print img[i][j][0] , children_img[i][j][0]
            deltaRed = img[i][j][0] - children_img[i][j][0]
            deltaGreen = img[i][j][1] - children_img[i][j][1]
            deltaBlue = img[i][j][2] - children_img[i][j][2]
 
            #measure the distance between the colors in 3D space
            score += (deltaRed * deltaRed) + (deltaGreen * deltaGreen) + (deltaBlue * deltaBlue) 
            
    print score
    return score

def make_child_from_two_parents(parent1,parent2,first_parent):
    child = np.zeros((size,size,3))
    height = 0
    for i1, i2, i3 in zip(parent1, parent2, first_parent):
        width = 0
        for j1, j2, j3 in zip(i1, i2, i3):
            
            if np.array_equal(j1,j3):
                child[height][width][0] = j2[0]
                child[height][width][1] = j2[1]
                child[height][width][2] = j2[2]
            elif np.array_equal(j2,j3):
                child[height][width][0] = j1[0]
                child[height][width][1] = j1[1]
                child[height][width][2] = j1[2]
            else:
                child[height][width][0] = j1[0] 
                child[height][width][1] = j1[1] 
                child[height][width][2] = j1[2] 
            width += 1
        height += 1
    return child
             

        
def main(args):

    global img,size
    img = scipy.misc.imread('imigi.jpg')
    size = len(img)
    max_generation = 100
    current_generation = 0
    family = []
    family_size = 50
    biggest_score = 0
    score = 0.0
    
    first_parent = np.zeros((size,size,3))
    score_first_parent = score_children(first_parent)
    genre = -1

    example = score_first_parent*1.0
    #for current_generation in xrange(max_generation):
    while score_first_parent >= example/20:
    #while genre < current_generation:
            #scipy.misc.imsave('end.png',first_parent)
            while len(family) <= family_size:
                
                xi = create_random_individual_polygon(copy.deepcopy(first_parent))
                print type(family)
                family.append(xi)
                
            fam_hel = []
            
            for j in family:
                fam_hel.append(make_child_from_two_parents(copy.deepcopy(j),copy.deepcopy(family[randint(0,len(family)-1)]),first_parent))
                
            family = family + fam_hel
            new_family = []
            biggest_score = score_first_parent*1
            biggest_parent = copy.deepcopy(first_parent)
            
            print len(family)
            
            for i in family:
                
                print type(i)
                score = score_children(i)*1
                print score_first_parent
                
                if score <= score_first_parent:
                    new_family.append(i)
    
                if score <= biggest_score:
                    biggest_score = score*1
                    biggest_parent = copy.deepcopy(i)
                    #scipy.misc.imsave('end.png',biggest_parent)
            #scipy.misc.imsave('end.png',biggest_parent)

            family = copy.deepcopy(new_family)
            if np.array_equal(first_parent,biggest_parent):
                pass
            else:
                first_parent = copy.deepcopy(biggest_parent)
                genre += 1
                print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                score_first_parent = biggest_score*1
                scipy.misc.imsave('endio.png',first_parent)
        #current_generation += 1
        #print first_parent
        
    #scipy.misc.imsave('end.png',first_parent)
    
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
