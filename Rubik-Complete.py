# -*- coding: utf-8 -*-


import  copy 
import  time 
import  random 
import  numpy   as np 
import  os
import  pygame
from  simpleai.search  import SearchProblem , astar, 
from    quat           import *
from    geometry       import *
from    pygame.locals  import *
from    OpenGL.GL      import *
from    OpenGL.GLU     import *



value = 0

#1 blanco
#2 azul
#3 amarillo
#4 verde
#5 naranja
#6 rojo


Sticker11 = (
    # 0 0
    (-2.95, 1.025, 3.01),
    (-2.95, 2.95, 3.01),
    (-1.025, 2.95, 3.01),
    (-1.025, 1.025, 3.01),
)
Sticker12 = (
    # 0 1
    (-0.9625, 1.025, 3.01),
    (-0.9625, 2.95, 3.01),
    (0.9625, 2.95, 3.01),
    (0.9625, 1.025, 3.01),
)
Sticker13 = (
   # 0 2
    (1.025, 1.025, 3.01),
    (1.025, 2.95, 3.01),
    (2.95, 2.95, 3.01),
    (2.95, 1.025, 3.01),
)
Sticker21 = (
    # 1 0
    (-2.95, -0.9625, 3.01),
    (-2.95, 0.9625, 3.01),
    (-1.025, 0.9625, 3.01),
    (-1.025, -0.9625, 3.01),
)
Sticker22 = (
    # 1 1
    (-0.9625, -0.9625, 3.01),
    (-0.9625, 0.9625, 3.01),
    (0.9625, 0.9625, 3.01),
    (0.9625, -0.9625, 3.01),
)
Sticker23 = (
   # 1 2
    (1.025, -0.9625, 3.01),
    (1.025, 0.9625, 3.01),
    (2.95, 0.9625, 3.01),
    (2.95, -0.9625, 3.01),
)
Sticker31 = (
   # 2 0
    (-2.95, -2.95, 3.01),
    (-2.95, -1.025, 3.01),
    (-1.025, -1.025, 3.01),
    (-1.025, -2.95, 3.01),
)
Sticker32 = (
  # 2 1
    (-0.9625, -2.95, 3.01),
    (-0.9625, -1.025, 3.01),
    (0.9625, -1.025, 3.01),
    (0.9625, -2.95, 3.01),
)
Sticker33 = (
   # 2 2
    (1.025, -2.95, 3.01),
    (1.025, -1.025, 3.01),
    (2.95, -1.025, 3.01),
    (2.95, -2.95, 3.01)
)
cube_stickers = (
    # 0 0
    (-2.95, 1.025, 3.01),
    (-2.95, 2.95, 3.01),
    (-1.025, 2.95, 3.01),
    (-1.025, 1.025, 3.01),
    

    # 0 1
    (-0.9625, 1.025, 3.01),
    (-0.9625, 2.95, 3.01),
    (0.9625, 2.95, 3.01),
    (0.9625, 1.025, 3.01),

    # 0 2
    (1.025, 1.025, 3.01),
    (1.025, 2.95, 3.01),
    (2.95, 2.95, 3.01),
    (2.95, 1.025, 3.01),
    
    # 1 0
    (-2.95, -0.9625, 3.01),
    (-2.95, 0.9625, 3.01),
    (-1.025, 0.9625, 3.01),
    (-1.025, -0.9625, 3.01),

    # 1 1
    (-0.9625, -0.9625, 3.01),
    (-0.9625, 0.9625, 3.01),
    (0.9625, 0.9625, 3.01),
    (0.9625, -0.9625, 3.01),

    # 1 2
    (1.025, -0.9625, 3.01),
    (1.025, 0.9625, 3.01),
    (2.95, 0.9625, 3.01),
    (2.95, -0.9625, 3.01),

    # 2 0
    (-2.95, -2.95, 3.01),
    (-2.95, -1.025, 3.01),
    (-1.025, -1.025, 3.01),
    (-1.025, -2.95, 3.01),

    # 2 1
    (-0.9625, -2.95, 3.01),
    (-0.9625, -1.025, 3.01),
    (0.9625, -1.025, 3.01),
    (0.9625, -2.95, 3.01),

    # 2 2
    (1.025, -2.95, 3.01),
    (1.025, -1.025, 3.01),
    (2.95, -1.025, 3.01),
    (2.95, -2.95, 3.01)
)
cube_pieces = (
    (-2.95, -2.95, 2.95),
    (-2.95, -1.025, 2.95),
    (-1.025, -1.025, 2.95),
    (-1.025, -2.95, 2.95),
    (-2.95, -2.95, 1.025),
    (-2.95, -1.025, 1.025),
    (-1.025, -1.025, 1.025),
    (-1.025, -2.95, 1.025)
)
up_face = (

    (-3.0, 1.0, 3.0),
    (-3.0, 3.0, 3.0),       # 1
    (3.0, 3.0, 3.0),        # 2
    (3.0, 1.0, 3.0),
    (-3.0, 1.0, -3.0),
    (-3.0, 3.0, -3.0),      # 5
    (3.0, 3.0, -3.0),        # 6
    (3.0, 1.0, -3.0)

    # (0, 1, 2, 3),  # Front
    # (3, 2, 6, 7),  # Right
    # (7, 6, 5, 4),  # Back
    # (4, 5, 1, 0),  # Left
    # (1, 5, 6, 2),  # Top
    # (4, 0, 3, 7)  # Bottom
)


#def draw_face():
#    glBegin(GL_LINES)
#    glColor3fv((0.5, 0.5, 0.5))
#    for edge in cube_edges:
#        for vertex in edge:
#            glVertex3fv(up_face[vertex])
#            glEnd()

def SelectColor(num):
        if num == 1:
           glColor3fv((1.0, 1.0, 1.0))
        if num == 2:
           glColor3fv((0.0, 0.318, 0.729))
        if num == 3:
           glColor3fv((1.0, 0.835, 0.0))
        if num == 4:
           glColor3fv((0.0, 0.62, 0.376))
        if num == 5:
           glColor3fv((1.0, 0.345, 0.0))
        if num == 6:
           glColor3fv((0.8, 0.118, 0.118))  
           
def draw_stickers(matriz):
    glBegin(GL_QUADS)
    for v in range(len(Sticker11)):
      value = int(matriz[0][0])
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker11[v])
      
    for v in range(len(Sticker12)):
      value = int(matriz[0][1])
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker12[v])
      
    for v in range(len(Sticker13)):
      value = int(matriz[0][2])
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker13[v])
      
    for v in range(len(Sticker21)):
      value = int(matriz[1][0])
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker21[v])
      
    for v in range(len(Sticker22)):
      value = int(matriz[1][1])
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker22[v])
      
    for v in range(len(Sticker23)):
      value = int(matriz[1][2])
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker23[v])
      
    for v in range(len(Sticker31)):
      value = int(matriz[2][0])
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker31[v])
      
    for v in range(len(Sticker32)):
      value = int(matriz[2][1])
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker32[v])
      
    for v in range(len(Sticker33)):
      value = int(matriz[2][2])
      value = int(value/10)
      SelectColor(value)
      glVertex3fv(Sticker33[v])  
     
    glEnd()
    
    
    
    #for v in range(len(cube_stickers)):
    # glVertex3fv(cube_stickers[v])

def cube(rubik):
    # glBegin(GL_QUADS)
    # for color, surface in zip(cube_colors, cube_surfaces):
    #     glColor3fv(color)
    #     for vertex in surface:
    #         glVertex3fv(cube_verts[vertex])
    # glEnd()

    glBegin(GL_QUADS)
    for surface in cube_surfaces:
        glColor3fv((0.3,0.3, 0.3))
        for vertex in surface:
            glVertex3fv(cube_verts[vertex])
    glEnd()
    #

#1 blanco
#2 azul
#3 amarillo
#4 verde
#5 naranja
#6 rojo

    # White
    #glColor3fv((1.0, 1.0, 1.0))
    draw_stickers(rubik.face1)
    glRotate(90, 1, 0, 0)
    # Blue
    draw_stickers(rubik.face5)
    glColor3fv((0.0, 0.318, 0.729))
    #draw_stickers()
    glRotate(90, 1, 0, 0)
    # Yellow
    draw_stickers(rubik.face4)
    glColor3fv((1.0, 0.835, 0.0))
    #draw_stickers()
    glRotate(90, 1, 0, 0)
    # Green
    draw_stickers(rubik.face2)
    glColor3fv((0.0, 0.62, 0.376))
    #draw_stickers()
    glRotate(90, 0, 1, 0)
    # Orange
    draw_stickers(np.rot90(rubik.face3))
    #draw_stickers(np.rot90(rubik.face6))
    glColor3fv((1.0, 0.345, 0.0))
    #draw_stickers()
    glRotate(180, 0, 1, 0)
    # Red
    draw_stickers(np.rot90(rubik.face6,3))
    #draw_stickers(np.rot90(rubik.face1,3))
    glColor3fv((0.8,8, 0.118))
    #draw_stickers()

    glBegin(GL_LINES)
    glColor3fv((0.5, 0.5, 0.5))
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_verts[vertex])
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_pieces[vertex])
    glEnd()


class Node(object):
    def __init__(self, cube_pos, value, padre, rubik):
        self.cube_pos = cube_pos
        self.value = value
        self.rubik = rubik
        self.children = [] #Array de hijos
        self.padre = padre #Rubik padre
        
    #*     
    #Añade los hijos a la lista de hijos del padre Rubik=self
    def add_child(self, obj):
        self.children.append(obj)
        
class Problem(SearchProblem):
    
    COSTS = {    
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 1,
        8: 1,
        9: 1,
        10: 1,
        11: 1           
    }
    
    def actions(self, rubik):
                
       # if len(state) < len(GOAL):
        #    return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        #else:
       #     return []
       ''' retorna la Lista de acciones que se pueden ejecutar
       '''
       list = []
       for i in range(0, 12):
            list.append(i)
                
       return list

    def result(self, state, action):
        '''
        Aqui se le aplica la accion al estado 
        '''
        rubik_Copy = copy.deepcopy(state)
        
        if (action == 0):
            rubik_Copy.face_1(True)
        elif (action == 1):
            rubik_Copy.face_1(False)
        elif (action== 2):
            rubik_Copy.face_2(True)
        elif (action== 3):
            rubik_Copy.face_2(False)
        elif (action== 4):
            rubik_Copy.face_3(True)
        elif (action== 5):
            rubik_Copy.face_3(False)
        elif (action== 6):
            rubik_Copy.face_4(True)
        elif (action== 7):
            rubik_Copy.face_4(False)
        elif (action== 8):
            rubik_Copy.face_5(True)
        elif (action== 9):
            rubik_Copy.face_5(False)
        elif (action== 10):
            rubik_Copy.face_6(True)
        elif (action== 11):
            rubik_Copy.face_6(False)
        return rubic_Copy

    def is_goal(self, state):
        f=[]
        f.append(state.face1)
        f.append(state.face2)
        f.append(state.face3)
        f.append(state.face4)
        f.append(state.face5)
        f.append(state.face6)

        ob=[]
        ob.append(np.array(['11', '12', '13', '14', '15', '16', '17', '18', '19']).reshape((3, 3))) #Blanco
        ob.append(np.array(['21', '22', '23', '24', '25', '26', '27', '28', '29']).reshape((3, 3))) #Azul
        ob.append(np.array(['31', '32', '33', '34', '35', '36', '37', '38', '39']).reshape((3, 3))) #Amarillo
        ob.append(np.array(['41', '42', '43', '44', '45', '46', '47', '48', '49']).reshape((3, 3))) #Verde 
        ob.append(np.array(['51', '52', '53', '54', '55', '56', '57', '58', '59']).reshape((3, 3))) #Naranja
        ob.append(np.array(['61', '62', '63', '64', '65', '66', '67', '68', '69']).reshape((3, 3))) #Rojo
        
        e3=True
        for i in range(6):
            e1 = ob[i]
            e2 = f[i]
            for y in range(3):
                for x in range(3):
                    if(e1[x,y]==e2[x,y]):
                        e3=e3  
                    else:
                        e3= False 
                        return False                
        return e3 #return True


    
    def heuristic(self, state):
        '''regresa cuantas posiciones estan incorrectas 
           dentro de todas las posibles,
           Si todas estan correctas h=0
        '''
        # how far are we from the goal?
        #wrong = sum([1 if state[i] != GOAL[i] else 0
        #            for i in range(len(state))])
        #missing = len(GOAL) - len(state)
        #return wrong + missing
        f=[]
        f.append(state.face1)
        f.append(state.face2)
        f.append(state.face3)
        f.append(state.face4)
        f.append(state.face5)
        f.append(state.face6)

        ob=[]
        ob.append(np.array(['11', '12', '13', '14', '15', '16', '17', '18', '19']).reshape((3, 3))) #Blanco
        ob.append(np.array(['21', '22', '23', '24', '25', '26', '27', '28', '29']).reshape((3, 3))) #Azul
        ob.append(np.array(['31', '32', '33', '34', '35', '36', '37', '38', '39']).reshape((3, 3))) #Amarillo
        ob.append(np.array(['41', '42', '43', '44', '45', '46', '47', '48', '49']).reshape((3, 3))) #Verde 
        ob.append(np.array(['51', '52', '53', '54', '55', '56', '57', '58', '59']).reshape((3, 3))) #Naranja
        ob.append(np.array(['61', '62', '63', '64', '65', '66', '67', '68', '69']).reshape((3, 3))) #Rojo
        
        wrong=0
        for i in range(6):
            e1 = ob[i]
            e2 = f[i]
            for y in range(3):
                for x in range(3):
                    if(e1[x,y]!=e2[x,y]):
                        wrong+=1  
        return wrong
    

        
###################################################################################
class Rubik(object):
    def __init__(self):
        self.face1 = None
        self.face2 = None
        self.face3 = None
        self.face4 = None
        self.face5 = None
        self.face6 = None
        
    
        
    def face_1(self, flag):
        if flag:
            self.face1 = np.rot90(self.face1, 3)
            temp = copy.deepcopy(self.face3[:, 0])  # This saves the first column that is being updated
            self.face3[:, 0] = self.face2[2, :]
            temp2 = copy.deepcopy(self.face5[0, :])
            self.face5[0, :] = np.flip(temp, -1)
            temp = copy.deepcopy(self.face6[:, 2])
            self.face6[:, 2] = temp2
            self.face2[2, :] = np.flip(temp, -1)
           
        else:
            self.face1 = np.rot90(self.face1)
            # Update face1 and face2
            temp = copy.deepcopy(self.face3[:, 0])  # This saves the first column that is being updated
            self.face3[:, 0] = np.flip(self.face5[0, :], -1)
            temp2 = copy.deepcopy(self.face2[2, :])
            self.face2[2, :] = temp
            temp = copy.deepcopy(self.face6[:, 2])
            self.face6[:, 2] = np.flip(temp2, -1)
            self.face5[0, :] = temp

    def face_2(self, flag):
        if flag:
            self.face2 = np.rot90(self.face2, 3)
            temp = copy.deepcopy(self.face3[0, :])  # This saves the first column that is being updated
            self.face3[0, :] = np.flip(self.face4[2, :], -1)
            temp2 = copy.deepcopy(self.face1[0, :])
            self.face1[0, :] = temp
            temp = copy.deepcopy(self.face6[0, :])
            self.face6[0, :] = temp2
            self.face4[2, :] = np.flip(temp, -1)

        else:
            self.face2 = np.rot90(self.face2)
            temp = copy.deepcopy(self.face6[0, :])  # This saves the first column that is being updated
            self.face6[0, :] = np.flip(self.face4[2, :], -1)
            temp2 = copy.deepcopy(self.face1[0, :])
            self.face1[0, :] = temp
            temp = copy.deepcopy(self.face3[0, :])
            self.face3[0, :] = temp2
            self.face4[2, :] = np.flip(temp, -1)
        # return face1, face2, face3, face4, face6
    def face_3(self, flag):
        if flag:
            self.face3 = np.rot90(self.face3, 3)
            # Update face1 and face2
            temp = copy.deepcopy(self.face4[:, 2])  # This saves the first column thatt is being updated
            self.face4[:, 2] = copy.deepcopy(self.face2[:, 2])
            temp2 = copy.deepcopy(self.face5[:, 2])
            self.face5[:, 2] = temp
            temp = copy.deepcopy(self.face1[:, 2])
            self.face2[:, 2] = temp
            self.face1[:, 2] = temp2

        else:
            self.face3 = np.rot90(self.face3)
            temp = copy.deepcopy(self.face1[:, 2])
            temp2 = copy.deepcopy(self.face2[:, 2])
            temp3 = copy.deepcopy(self.face4[:, 2])
            temp4 = copy.deepcopy(self.face5[:, 2])
            self.face4[:, 2] = temp4
            self.face5[:, 2] = temp
            self.face1[:, 2] = temp2
            self.face2[:, 2] = temp3

        # return face1, face2, face3, face4, face5
    def face_4(self, flag):
        if flag:
            self.face4 = np.rot90(self.face4, 3)
            temp = copy.deepcopy(self.face5[2, :])
            temp2 = copy.deepcopy(self.face3[:, 2])
            temp3 = copy.deepcopy(self.face2[0, :])
            temp4 = copy.deepcopy(self.face6[:, 0])
            self.face5[2, :] = temp4
            self.face3[:, 2] = np.flip(temp, -1)
            self.face2[0, :] = temp2
            self.face6[:, 0] = np.flip(temp3, -1)

        else:
            self.face4 = np.rot90(self.face4)
            temp = copy.deepcopy(self.face5[2, :])
            temp2 = copy.deepcopy(self.face3[:, 2])
            temp3 = copy.deepcopy(self.face2[0, :])
            temp4 = copy.deepcopy(self.face6[:, 0])
            self.face5[2, :] = np.flip(temp2, -1)
            self.face3[:, 2] = temp3
            self.face2[0, :] = np.flip(temp4, -1)
            self.face6[:, 0] = temp
    def face_5(self, flag):
        if flag:
            self.face5 = np.rot90(self.face5, 3)
            temp = copy.deepcopy(self.face3[2, :])  # This saves the first column that is being updated
            self.face3[2, :] = self.face1[2, :]
            temp2 = copy.deepcopy(self.face4[0, :])
            self.face4[0, :] = np.flip(temp, -1)
            temp = copy.deepcopy(self.face6[2, :])
            self.face6[2, :] = np.flip(temp2, -1)
            self.face1[2, :] = temp

        else:
            self.face5 = np.rot90(self.face5)
            # Update face1 and face2
            temp = copy.deepcopy(self.face3[2, :])  # This saves the first column that is being updated
            self.face3[2, :] = np.flip(self.face4[0, :], -1)
            temp2 = copy.deepcopy(self.face1[2, :])
            self.face1[2, :] = temp
            temp = copy.deepcopy(self.face6[2, :])
            self.face6[2, :] = temp2
            self.face4[0, :] = np.flip(temp, -1)
        # return face1, face3, face4, face5, face6
    def face_6(self, flag):
        if flag:
            self.face6 = np.rot90(self.face6, 3)
            temp = copy.deepcopy(self.face1[:, 0])  # This saves the first column that is being updated
            self.face1[:, 0] = self.face2[:, 0]
            temp2 = copy.deepcopy(self.face5[:, 0])
            self.face5[:, 0] = temp
            temp = copy.deepcopy(self.face4[:, 0])
            self.face4[:, 0] = temp2
            self.face2[:, 0] = temp
            
        else:
            self.face6 = np.rot90(self.face6)
            temp = copy.deepcopy(self.face5[:, 0])  # This saves the first column that is being updated
            self.face5[:, 0] = self.face4[:, 0]
            temp2 = copy.deepcopy(self.face1[:, 0])
            self.face1[:, 0] = temp
            temp = copy.deepcopy(self.face2[:, 0])
            self.face2[:, 0] = temp2
            self.face4[:, 0] = temp
        # return face1, face2, face4, face5, face6
    def show(self):
        print("Cara1: ")
        print(self.face1)
        print("Cara2: ")
        print(self.face2)
        print("Cara3: ")
        print(self.face3)
        print("Cara4: ")
        print(self.face4)
        print("Cara5: ")
        print(self.face5)
        print("Cara6: ")
        print(self.face6)

    def heuristic(self):
        counter = 0
        counter += (self.face1 == np.array([11, 12, 13, 14, 15, 16, 17, 18, 19]).reshape((3, 3))).sum()
        counter += (self.face2 == np.array([21, 22, 23, 24, 25, 26, 27, 28, 29]).reshape((3, 3))).sum()
        counter += (self.face3 == np.array([31, 32, 33, 34, 35, 36, 37, 38, 39]).reshape((3, 3))).sum()
        counter += (self.face4 == np.array([41, 42, 43, 44, 45, 46, 47, 48, 49]).reshape((3, 3))).sum()
        counter += (self.face5 == np.array([51, 52, 53, 54, 55, 56, 57, 58, 59]).reshape((3, 3))).sum()
        counter += (self.face6 == np.array([61, 62, 63, 64, 65, 66, 67, 68, 69]).reshape((3, 3))).sum()
        return counter
       
       # counter = 0
       # counter += (self.face1 == np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]).reshape((3, 3))).sum()
       # counter += (self.face2 == np.array([2, 2, 2, 2, 2, 2, 2, 2, 2]).reshape((3, 3))).sum()
       # counter += (self.face3 == np.array([3, 3, 3, 3, 3, 3, 3, 3, 3]).reshape((3, 3))).sum()
       # counter += (self.face4 == np.array([4, 4, 4, 4, 4, 4, 4, 4, 4]).reshape((3, 3))).sum()
       # counter += (self.face5 == np.array([5, 5, 5, 5, 5, 5, 5, 5, 5]).reshape((3, 3))).sum()
       # counter += (self.face6 == np.array([6, 6, 6, 6, 6, 6, 6, 6, 6]).reshape((3, 3))).sum()
       # return counter
       
    def heuristic2(self):
        counter = 0
        if np.count_nonzero(self.face1 == 1) == 9:
            counter += 1
        if np.count_nonzero(self.face2 == 2) == 9:
            counter += 1
        if np.count_nonzero(self.face3 == 3) == 9:
            counter += 1
        if np.count_nonzero(self.face4 == 4) == 9:
            counter += 1
        if np.count_nonzero(self.face5 == 5) == 9:
            counter += 1
        if np.count_nonzero(self.face6 == 6) == 9:
            counter += 1
        return counter
    
    def backtracking(self, sneaky):
        #sneaky.append([r, r2])
        rev_sneaky = sneaky[4:]
        rev_sneaky = rev_sneaky[::-1]
        for each in rev_sneaky:
            initT()
            r = each[0]
            r2 = each[1]
            if r2 == 1:
                print("Se giro la cara: ", r, " Hacia la derecha")
            else:
                print("Se giro la cara: ", r, " Hacia la izquierda")
            if r2 == 1:
                r2 = False
            else:
                r2 = True

            if r == 1:
                self.face_1(r2)
            if r == 2:
                self.face_2(r2)
            if r == 3:
                self.face_3(r2)
            if r == 4:
                self.face_4(r2)
            if r == 5:
                self.face_5(r2)
            if r == 6:
                self.face_6(r2)

    def initial(self):
        self.face1 = np.array(['11', '12', '13', '14', '15', '16', '17', '18', '19']).reshape((3, 3)) #Blanco
        self.face2 = np.array(['21', '22', '23', '24', '25', '26', '27', '28', '29']).reshape((3, 3)) #Azul
        self.face3 = np.array(['31', '32', '33', '34', '35', '36', '37', '38', '39']).reshape((3, 3)) #Amarillo
        self.face4 = np.array(['41', '42', '43', '44', '45', '46', '47', '48', '49']).reshape((3, 3)) #Verde 
        self.face5 = np.array(['51', '52', '53', '54', '55', '56', '57', '58', '59']).reshape((3, 3)) #Naranja
        self.face6 = np.array(['61', '62', '63', '64', '65', '66', '67', '68', '69']).reshape((3, 3)) #Rojo
        
        #self.face1 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]).reshape(3, 3)
        #self.face2 = np.array([2, 2, 2, 2, 2, 2, 2, 2, 2]).reshape(3, 3)
        #self.face3 = np.array([3, 3, 3, 3, 3, 3, 3, 3, 3]).reshape(3, 3)
        #self.face4 = np.array([4, 4, 4, 4, 4, 4, 4, 4, 4]).reshape(3, 3)
        #self.face5 = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5]).reshape(3, 3)
        #self.face6 = np.array([6, 6, 6, 6, 6, 6, 6, 6, 6]).reshape(3, 3)
        
        
        
        
class Nodo(object):
    def __init__(self):
        self.rubik = None
        self.exists = False
        self.value = None
        self.next_nodo = None
        self.exist_nextnodo = False
    
    def _init_(self, rubik, value):
        self.rubik = rubik
        self.exists = True
        self.value = value
        self.next_nodo = None
        self.exist_nextnodo = False
        
    def _init_(self, rubik, value, next_nodo):
        self.rubik = rubik
        self.exists = True
        self.value = value
        self.next_nodo = next_nodo
        self.exist_nextnodo = True
     
    def insert(make_nodo, pTR):
        if pTR.exists:
            if pTR.value > make_nodo.value:
                make_nodo.next_nodo = pTR
                make_nodo.exist_nextnodo = True
                pTR=make_nodo
            else:
                conti = True
                anteriornodo = pTR
                nodo = pTR
                while conti:
                    conti = nodo.exist_nextnodo
                    if conti:
                        anteriornodo = nodo
                        nodo = nodo.next_nodo
                        if nodo.value > make_node.value:
                            make_node.next_nodo = nodo
                            make_node.exist_nextnodo = True
                            anteriornodo = make_node
                            conti = False
                        
                    else:
                        nodo.next_nodo = make_nodo
                        nodo.exist_nextnodo = True
                        
        else:
            pTR=make_nodo
        
    
        
def addChild(parent, depth):  # , rubik):
    #rubik_Copy = copy.deepcopy(parent.rubik)
    for i in range(0, 12):
        rubik_Copy = copy.deepcopy(parent.rubik)
        if (i == 0):
            rubik_Copy.face_1(True)
        elif (i == 1):
            rubik_Copy.face_1(False)
        elif (i == 2):
            rubik_Copy.face_2(True)
        elif (i == 3):
            rubik_Copy.face_2(False)
        elif (i == 4):
            rubik_Copy.face_3(True)
        elif (i == 5):
            rubik_Copy.face_3(False)
        elif (i == 6):
            rubik_Copy.face_4(True)
        elif (i == 7):
            rubik_Copy.face_4(False)
        elif (i == 8):
            rubik_Copy.face_5(True)
        elif (i == 9):
            rubik_Copy.face_5(False)
        elif (i == 10):
            rubik_Copy.face_6(True)
        elif (i == 11):
            rubik_Copy.face_6(False)
        # print("herustic: ",rubik_Copy.herustic())
        new_node = Node(i, rubik_Copy.heuristic(), parent, rubik_Copy)
        parent.add_child(new_node)
    depth = + 1
    return parent, depth

def path(nodo, Tree_path):
    if (nodo != None):
        print("-", nodo.cube_pos)
        Tree_path.append(nodo.cube_pos)
        path(nodo.padre, Tree_path)
    return Tree_path

def initTree(init, depth):
    # print("Numero de hijos: ", len(init.children))
    if not 0 < len(init.children):
        init.children = []
        init, depth = addChild(init, depth - 1)
    for i in range(0, 12):
        init.children[i], depth = addChild(init.children[i], depth)
    for i in range(0, 12):
        for j in range(0, 12):
            init.children[i].children[j], depth = addChild(init.children[i].children[j], depth)
    for i in range(0, 12):
        for j in range(0, 12):
            for k in range(0, 12):
                init.children[i].children[j].children[k], depth = addChild(init.children[i].children[j].children[k],
                                                                           depth)
    return init, depth

def BuscarMayor(init, nodomayor):
    mayor = 0
    for i in range(0, 12):
        for j in range(0, 12):
            for k in range(0, 12):
                for l in range(0, 12):
                    nodo = init.children[i].children[j].children[k].children[l]
                    # print("value: ", nodo.value," pos: ", nodo.cube_pos)
                    # print("Esto es el valor del nodo: ", nodo.value)
                    if mayor < nodo.value:
                        mayor = nodo.value
                        nodomayor = nodo
    return init, nodomayor

"""MAIN"""
def add_face_move(var, cube_moves):
    cube_moves.append(var)

def rotate_face2(var, rubik):
    if(str(var) == "rf1"):   
        rubik.face_1(True)
    if(str(var) == "rf2"):   
        rubik.face_2(True)
    if(str(var) == "rf3"):   
        rubik.face_3(True)
    if(str(var) == "rf4"):   
        rubik.face_4(True)
    if(str(var) == "rf5"):   
        rubik.face_5(True)
    if(str(var) == "rf6"):   
        rubik.face_6(True)

    if(str(var) == "lf1"):   
        rubik.face_1(False)
    if(str(var) == "lf2"):   
        rubik.face_2(False)
    if(str(var) == "lf3"):   
        rubik.face_3(False)
    if(str(var) == "lf4"):   
        rubik.face_4(False)
    if(str(var) == "lf5"):   
        rubik.face_5(False)
    if(str(var) == "lf6"):   
        rubik.face_6(False)

def rotate_face(event, rubik, cube_moves):

    if event.key == pygame.K_t:   
        rotate_face2("rf1", rubik)
        add_face_move("rf1",cube_moves)
    if event.key == pygame.K_f:   
        rotate_face2("rf2", rubik)
        add_face_move("rf2",cube_moves)
    if event.key == pygame.K_o:
        rotate_face2("rf3", rubik)
        add_face_move("rf3",cube_moves)
    if event.key == pygame.K_h:   
        rotate_face2("rf4", rubik)
        add_face_move("rf4",cube_moves)
    if event.key == pygame.K_k:
        rotate_face2("rf5", rubik)
        add_face_move("rf5",cube_moves)
    if event.key == pygame.K_u:   
        rotate_face2("rf6", rubik)
        add_face_move("rf6",cube_moves)

    if event.key == pygame.K_y:  
        rotate_face2("lf1", rubik)
        add_face_move("lf1",cube_moves)
    if event.key == pygame.K_g:   
        rotate_face2("lf2", rubik)
        add_face_move("lf2",cube_moves)
    if event.key == pygame.K_p:   
        rotate_face2("lf3", rubik)
        add_face_move("lf3",cube_moves)
    if event.key == pygame.K_j:
        rotate_face2("lf4", rubik)
        add_face_move("lf4",cube_moves)
    if event.key == pygame.K_l:  
        rotate_face2("lf5", rubik)
        add_face_move("lf5",cube_moves)
    if event.key == pygame.K_i:   
        rotate_face2("lf6", rubik)
        add_face_move("lf6",cube_moves)

def random_cube(event, rubik, cube_moves ,num):
    if event.key == pygame.K_r: # Random Cube
        #rubik.random_cube(num)
        num_steps=1#numero de movimientos random que se realizaran...
        for i in range(0, num_steps):
            print(i)
            r = random.randint(1, 6)
            r2 = random.choice([True, False])
            if r == 1:
                if r2:
                    add_face_move("rf1",cube_moves)
                else:
                    add_face_move("lf1",cube_moves)
                rubik.face_1(r2)
            if r == 2:
                if r2:
                    add_face_move("rf2",cube_moves)
                else:
                    add_face_move("lf2",cube_moves)
                rubik.face_2(r2)
            if r == 3:
                if r2:
                    add_face_move("rf3",cube_moves)
                else:
                    add_face_move("lf3",cube_moves)
                rubik.face_3(r2)
            if r == 4:
                if r2:
                    add_face_move("rf4",cube_moves)
                else:
                    add_face_move("lf4",cube_moves)
                rubik.face_4(r2)
            if r == 5:
                if r2:
                    add_face_move("rf5",cube_moves)
                else:
                    add_face_move("lf5",cube_moves)
                rubik.face_5(r2)
            if r == 6:
                if r2:
                    add_face_move("rf6",cube_moves)
                else:
                    add_face_move("lf6",cube_moves)
                rubik.face_6(r2)

def get_inverse_cube_move(move):
    if(move == "rf1"):
        return "lf1"       
    if(move == "rf2"):
        return "lf2"       
    if(move == "rf3"):
        return "lf3"       
    if(move == "rf4"):
        return "lf4"       
    if(move == "rf5"):
        return "lf5"       
    if(move == "rf6"):
        return "lf6"   
    if(move == "lf1"):
        return "rf1"   
    if(move == "lf2"):
        return "rf2"   
    if(move == "lf3"):
        return "rf3"   
    if(move == "lf4"):
        return "rf4"   
    if(move == "lf5"):
        return "rf5"   
    if(move == "lf6"):
        return "rf6"
    return ""  

def solve(event, rubik, cube_moves):
    if event.key == pygame.K_e:
        #while True:
        print("el cubo se resolvera")
        longitud = len(cube_moves)
        vec = []
        #if longitud > 5:
        cube_moves1 = np.flip(cube_moves, -1)
        for move in cube_moves1:
            vec.append(get_inverse_cube_move(move))
            rotate_face2(get_inverse_cube_move(move) ,rubik)
            time.sleep(1)
            os.system('cls')
            rubik.show()
            #if longitud == 5:
            #    break
            #longitud = longitud - 1
        """
        depth = 0
        nodomayor = None
        start_time = time.time()
        Tree_path = []
        
        init = Node("initial", rubik.heuristic, None, rubik)

        init, depth = addChild(init, depth) 
        #print(rubik.heuristic())
        #rubik.random_cube()
        rubik.show()
        while (init.value != 54):
            init, depth = initTree(init, depth)
            init, nodomayor = BuscarMayor(init, nodomayor)
            init = copy.deepcopy(nodomayor);
            print("mayor: ", nodomayor.value, " posicion Mayor: ", nodomayor.cube_pos, " padre: ", nodomayor.padre.cube_pos)
            Tree_path = path(nodomayor, Tree_path)
            print(Tree_path[::-1])  # voltea el vector
        """
        #print("--- {} seconds ---".format(time.time() - start_time))

def heuristics(var, rubik):
    if str(var) == "heuristic":
        print("heuristica:", rubik.heuristic())
        try:
            input("Press enter to continue")
        except SyntaxError:
            pass
        
        
        
        
##################     CONVERSIONES    ##############
def matrix_to_string(matrix_):
    '''Convert matrix to string.
       Returns a string'''
    return '\n'.join([' '.join(row) for row in matrix_])
   
def string_to_matrix(string_):
    '''Convert puzzle string to list.
       Returns a list'''
    string_ = [row.split(' ') for row in string_.split('\n')]
    return np.array(string_).reshape((3, 3)) 
###Prueva1
#e1 = np.array(['11', '12', '13', '14', '15', '16', '17', '18', '19']).reshape((3, 3))
#e2=string_to_matrix(matrix_to_string(e1))
#e3=True
#for y in range(3):
#    for x in range(3):
#        if(e1[x,y]==e2[x,y]):
#            e3=e3  
#        else: e3=False        
#if(e3):
#    print('ok')
###Prueva2
#   e1='11 12 13\n14 15 16\n17 18 19'
#    e2=matrix_to_string(string_to_matrix(e1))
#    if(e1 == e2 ):
#        print('ok')
    

###Calcula cuantos movimientos le falta para estar en el objetivo  
def hPrimeraCruz(rubik):
    f1 = rubik.face1
    f2 = rubik.face2
    f3 = rubik.face3
    f4 = rubik.face4
    f5 = rubik.face5
    f6 = rubik.face6
    
    o1 = np.array(['11', '12', '13', '14', '15', '16', '17', '18', '19']).reshape((3, 3)) #Blanco
    o2 = np.array(['21', '22', '23', '24', '25', '26', '27', '28', '29']).reshape((3, 3)) #Azul
    o3 = np.array(['31', '32', '33', '34', '35', '36', '37', '38', '39']).reshape((3, 3)) #Amarillo
    o4 = np.array(['41', '42', '43', '44', '45', '46', '47', '48', '49']).reshape((3, 3)) #Verde 
    o5 = np.array(['51', '52', '53', '54', '55', '56', '57', '58', '59']).reshape((3, 3)) #Naranja
    o6 = np.array(['61', '62', '63', '64', '65', '66', '67', '68', '69']).reshape((3, 3)) #Rojo
    
    
    
    h=0
    if '12' == f1[0, 1] and '16' == f1[1, 2] and '18' == f1[2, 1] and '14' == f1[1, 0]:
        h = 0#print("Estan en el lugar indicado")
    else:
      #####################Para Distancia 1  
        if('12' == f1[1, 0] or '12' == f1[1, 2] or '12' == f3[0, 1] or '12' == f6[0, 1]):
            h += 1    
            #print("Distancia 1")
        if('16' == f1[0, 1] or '16' == f1[2, 1] or '16' == f2[1, 2] or '16' == f5[1, 2]):
            h += 1    
            #print("Distancia 1")
        if('18' == f1[1, 0] or '18' == f1[1, 2] or '18' == f3[2, 1] or '18' == f6[2, 1]):
            h += 1    
            #print("Distancia 1")
        if('14' == f1[0, 1] or '14' == f1[2, 1] or '14' == f2[1, 0] or '14' == f5[1, 0]):
            h += 1    
            #print("Distancia 1")

      #####################Para Distancia 2
        if('12' == f1[2, 1] or '12' == f2[1, 0] or '12' == f2[1, 2] or '12' == f3[1, 0] or '12' == f3[1, 2] or '12' == f4[0, 1] or '12' == f5[1, 0] or '12' == f5[1, 2] or '12' == f6[1, 0] or '12' == f6[1, 2]):
            h += 2    
            #print("Distancia 2")
        if('16' == f1[1, 0] or '16' == f2[0, 1] or '16' == f2[2, 1] or '16' == f3[0, 1] or '16' == f3[2, 1] or '16' == f4[1, 0] or '16' == f5[0, 1] or '16' == f5[2, 1] or '16' == f6[0, 1] or '16' == f6[2, 1]):
            h += 2    
            #print("Distancia 2")
        if('18' == f1[0, 1] or '18' == f2[1, 0] or '18' == f2[1, 2] or '18' == f3[1, 0] or '18' == f3[1, 2] or '18' == f4[2, 1] or '18' == f5[1, 0] or '18' == f5[1, 2] or '18' == f6[1, 0] or '18' == f6[1, 2]):
            h += 2    
            #print("Distancia 2")
        if('14' == f1[1, 2] or '14' == f2[0, 1] or '14' == f2[2, 1] or '14' == f3[0, 1] or '14' == f3[2, 1] or '14' == f4[1, 2] or '14' == f5[0, 1] or '14' == f5[2, 1] or '14' == f6[0, 1] or '14' == f6[2, 1]):
            h += 2    
            #print("Distancia 2")

        #####################Para Distancia 3
        if( '12' == f2[0, 1] or '12' == f2[2, 1] or '12' == f3[2, 1] or '12' == f4[1, 0] or '12' == f4[1, 2] or '12' == f5[0, 1] or '12' == f5[2, 1] or '12' == f6[2, 1]):
            h += 3
            #print("Distancia 3")
        if( '16' == f2[1, 0] or '16' == f3[1, 0] or '16' == f3[1, 2] or '16' == f4[0, 1] or '16' == f4[2, 1] or '16' == f5[1, 0] or '16' == f6[1, 0] or '16' == f6[1, 2]):
            h += 3
            #print("Distancia 3")
        if( '18' == f2[0, 1] or '18' == f2[2, 1] or '18' == f3[0, 1] or '18' == f4[1, 0] or '18' == f4[1, 2] or '18' == f5[0, 1] or '18' == f5[2, 1] or '18' == f6[0, 1]):
            h += 3
            #print("Distancia 3")
        if( '14' == f2[1, 2] or '14' == f3[1, 0] or '14' == f3[1, 2] or '14' == f4[0, 1] or '14' == f4[2, 1] or '14' == f5[1, 2] or '14' == f6[1, 0] or '14' == f6[1, 2]):
            h += 3
            #print("Distancia 3")      

      #####################Para Distancia 4
        if('12' == f4[2, 1]):
            h += 4   
            #print("Distancia 4")
        if('16' == f4[1, 2]):
            h += 4   
            #print("Distancia 4")
        if('18' == f4[0, 1]): 
            h += 4   
            #print("Distancia 4")
        if('14' == f4[1, 0]):
            h += 4   
            #print("Distancia 4")
            
        #print("No esta en el lugar indicado")
        print("Distancia", h)
    
def aSearch(rubik):
    pTR= Nodo(rubik)
        
def Asearch():
    g = 0
    h = 0
    f = g + h
    new_h = 0
    if new_h < h:
        print("este es el camino a tomar")
        h= new_h
    if h == 0:
        print("Este es el estado objetivo")
        
#def cruz():
    

def main():
    pygame.init()
    display = (1024, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('PyCube')
    
    rubik = Rubik()
    rubik.initial()

    rubik_initial = copy.deepcopy(rubik)
    var = ""

    # Using depth test to make sure closer colors are shown over further ones
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    # Default view
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.5, 40)
    glTranslatef(0.0, 0.0, -17.5)
    # set initial rotation

    inc_x = -0.006981317007977318
    inc_y = 0.013962634015954637
    accum = (1, 0, 0, 0)
    zoom = 1
    cube_moves = []
    rubik.show()
    solve_RubikCube = False
    vec = []
    cube_moves1 = []
    file = None

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                # Rotating about the x axis
                os.system('cls')
                random_cube(event, rubik,cube_moves, 10) # press R to move random the cube
                rotate_face(event, rubik, cube_moves)
                #instructions(var)

                #solve(event,rubik,cube_moves)
                if event.key == pygame.K_e:
                    solve_RubikCube = True
                    cube_moves1 = np.flip(cube_moves, -1)
                    file = open("RubikCube_solve.txt","w")


                #rubik.show()

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    inc_x = pi / 500
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    inc_x = -pi / 500
                    # Rotating about the y axis
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    inc_y = pi / 500
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    inc_y = -pi / 500
                    
                if event.key == pygame.K_m:
                    hPrimeraCruz(rubik)

                if event.key == pygame.K_u:
                    print('up')
                    
    
                    # Reset to default view
                if event.key == pygame.K_SPACE:
                    inc_x = 0
                    inc_y = 0
                    accum = (1, 0, 0, 0)
                    zoom = 1
    
                if event.type == pygame.KEYUP:
                    # Stoping rotation
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or \
                                    event.key == pygame.K_w or event.key == pygame.K_s:
                        inc_x = 0.0
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or \
                                    event.key == pygame.K_a or event.key == pygame.K_d or \
                                    event.key == pygame.K_u:
                        inc_y = 0.0

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Increase scale (zoom) value
                if event.button == 4:
                    if zoom < 1.6:
                        zoom += 0.05
                    # print('scroll up', zoom)
            if event.type == pygame.MOUSEBUTTONUP:
                # Increase scale (zoom) value
                
                if event.button == 5:
                    if zoom > 0.2:
                        zoom -= 0.05
                    # print('scroll down', zoom)
        
        if solve_RubikCube:
            if len(vec) < len(cube_moves1):
                os.system('cls')
                vecpos = len(vec)
                file.write(get_inverse_cube_move(cube_moves1[vecpos]))
                file.write("\n")
                vec.append(get_inverse_cube_move(cube_moves1[vecpos]))
                rotate_face2(get_inverse_cube_move(cube_moves1[vecpos]) ,rubik)
                
                print(vec)
                print(cube_moves1)
                time.sleep(1)
                rubik.show()
            else:
                solve_RubikCube = False
                vec = []
                cube_moves1 = []
                cube_moves = []
                file.close()

        # Get relative movement of mouse coordinates and update x and y incs
        if pygame.mouse.get_pressed()[0] == 1:
            (tmp_x, tmp_y) = pygame.mouse.get_rel()
            #print(tmp_x, tmp_y)
            inc_x = -tmp_y * pi / 450
            inc_y = -tmp_x * pi / 450

        #print(inc_x, inc_y)
        pygame.mouse.get_rel()  # prevents the cube from instantly rotating to a newly clicked mouse coordinate
        rot_x = normalize(axisangle_to_q((1.0, 0.0, 0.0), inc_x))
        rot_y = normalize(axisangle_to_q((0.0, 1.0, 0.0), inc_y))
        accum = q_mult(accum, rot_x)
        accum = q_mult(accum, rot_y)
        glMatrixMode(GL_MODELVIEW)
        glLoadMatrixf(q_to_mat4(accum))
        glScalef(zoom, zoom, zoom)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)\

        cube(rubik)
        
        pygame.display.flip()

main()