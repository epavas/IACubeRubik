import numpy as np



GOAL = '''11 12 13 14 15 16 17 18 19
21 22 23 24 25 26 27 28 29
31 32 33 34 35 36 37 38 39
41 42 43 44 45 46 47 48 49
51 52 53 54 55 56 57 58 59
61 62 63 64 65 66 67 68 69'''

def m_t_s(matrix_):
    '''Convert matrix to string.
       Returns a string'''
    return '\n'.join([' '.join(row) for row in matrix_])
   
def s_t_m(string_):
    '''Convert puzzle string to list.
       Returns a list'''
    string_ = [row.split(' ') for row in string_.split('\n')]
    return np.array(string_).reshape((3, 3)) 


INITIAL = '''4-1-2
7-e-3
8-5-6'''

def s_t_r(string_):
  list_ = [row.split(' ') for row in string_.split('\n')]
  rubik = Rubik()
  rubik.face1 = np.array(list_[0]).reshape((3,3))
  rubik.face2 = np.array(list_[1]).reshape((3,3))
  rubik.face3 = np.array(list_[2]).reshape((3,3))
  rubik.face4 = np.array(list_[3]).reshape((3,3))
  rubik.face5 = np.array(list_[4]).reshape((3,3))
  rubik.face6 = np.array(list_[5]).reshape((3,3))
  return rubik

def r_t_s(rubik):
    string_ = ' '.join([' '.join(row) for row in rubik.face1])
    string_ += '\n' + ' '.join([' '.join(row) for row in rubik.face2])
    string_ += '\n' + ' '.join([' '.join(row) for row in rubik.face3])
    string_ += '\n' + ' '.join([' '.join(row) for row in rubik.face4])
    string_ += '\n' + ' '.join([' '.join(row) for row in rubik.face5])
    string_ += '\n' + ' '.join([' '.join(row) for row in rubik.face6])
    
    return string_

def l_t_g(list_):
    return '\n'.join([' '.join(row) for row in list_])


def s_t_l(string_):
    return [row.split(' ') for row in string_.split('\n')]


class Rubik(object):
  def __init__(self):
    self.face1 = None
    self.face2 = None
    self.face3 = None
    self.face4 = None
    self.face5 = None
    self.face6 = None
        
#################PRUEVA1###################
print("Prueva 1")

e1 = np.array(['11', '12', '13', '14', '15', '16', '17', '18', '19']).reshape((3, 3))
e2=s_t_m(m_t_s(e1))
e3=True
for y in range(3):
  for x in range(3):
    if(e1[x,y]==e2[x,y]):
      e3=e3  
    else: e3=False        
if(e3):
  print('ok')

###########PRUEVA 2###########  
print("Prueva2")
e1='11 12 13\n14 15 16\n17 18 19'
e2=m_t_s(s_t_m(e1))
if(e1 == e2 ):
  print('ok')


###########Pruva 3 ####################
print("prueva 3")
if(GOAL == r_t_s(s_t_r(GOAL))):
  print('ok')

    