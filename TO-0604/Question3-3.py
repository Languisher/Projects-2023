"""
Complémentaire du projet, pour plus de détail, voir le fichier TO-0604/topo projet.ipynb

Auteurs :
- Simon
- Brenton
- Edward
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import random

def create_points_random(number_of_points=10, radius_maximum=10):
    """
    Créer des points aléatoires dans un espace 3D
    """
    
    List_x = [random.uniform(0, radius_maximum) for k in range(number_of_points)]
    List_y = [random.uniform(0, radius_maximum) for k in range(number_of_points)]
    List_z = [random.uniform(0, radius_maximum) for k in range(number_of_points)]

    return List_x, List_y, List_z
    
def plot_the_points(points_coor):
    """
    Plot les points dans un espace 3D
    """
    
    plt.plot(points_coor[0], points_coor[1], points_coor[2], 'yo')

def produit_vectoriel_3D(a, b):    # Produict vectoriel dans 3D
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

def produit_scalaire_3D(a, b):    # Produict scalaire dans 3D
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def enveloppe_3D(points_coors):
    """
    Trouver l'enveloppe convexe des points dans un espace 3D
    """
    
    triangles = []
    
    x_coors = points_coors[0]; y_coors = points_coors[1]; z_coors = points_coors[2]
    assert len(x_coors) == len(y_coors) == len(z_coors), "Les points ne sont pas dans le même espace"
    
    point_num = len(x_coors)

    # print(f"Les points sont: {len(points_coors)}")
    for index1 in range(point_num):
        for index2 in range(point_num):
            if not index1 == index2:
                for index3 in range(point_num):
                    if not index1 == index3 and not index2 == index3:
                        status_1 = True; status_2 = True 
                        
                        difference_1 = [x_coors[index2] - x_coors[index1],
                                        y_coors[index2] - y_coors[index1],
                                        z_coors[index2] - z_coors[index1]]
                        
                        difference_2 = [x_coors[index3] - x_coors[index1],
                                        y_coors[index3] - y_coors[index1],
                                        z_coors[index3] - z_coors[index1]]
                        
                        pro_vec = produit_vectoriel_3D(difference_1, difference_2)
                        
                        for index4 in range(point_num):
                            if not index4 == index1 and not index4 == index2 and not index4 == index3:
                                difference_3 = [x_coors[index4] - x_coors[index1],
                                                y_coors[index4] - y_coors[index1],
                                                z_coors[index4] - z_coors[index1]]
                                
                                pro_scal = produit_scalaire_3D(pro_vec, difference_3)
                                
                                if pro_scal < 0:
                                    status_1 = False
                                elif pro_scal > 0:
                                    status_2 = False
                                    
                        if (status_1 or status_2) and pro_vec:
                            triangles.append([[x_coors[index1], y_coors[index1], z_coors[index1]],
                                              [x_coors[index2], y_coors[index2], z_coors[index2]],
                                              [x_coors[index3], y_coors[index3], z_coors[index3]]])
                        
    return triangles
    
def draw_lines(triangles):
    for triangle in triangles:
        point1, point2, point3 = triangle

        plt.plot([point1[0], point2[0], point3[0], point1[0]],
                 [point1[1], point2[1], point3[1], point1[1]],
                 [point1[2], point2[2], point3[2], point1[2]], "b", linewidth=1)

def question3(points=None):
    if not points:
        points_coors = create_points_random(10, 10)
        

        
    plot_the_points(points_coors)
    triangles = enveloppe_3D(points_coors)

    draw_lines(triangles)
    plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
question3()