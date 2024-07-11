from ctypes import cdll, c_double, c_bool, c_void_p
from os import path, name
from sys import version_info

if name == "nt":    
  #window specific issue, cannot directly load with absolute path
  if version_info.major==3: 
    lib = cdll.LoadLibrary(path.join(path.dirname(__file__),"./libhupf.dll"))
  else: #nt and py2 specific issue, cannot directly load dll with absolute path
    from os import environ
    dir = path.abspath(path.dirname(__file__))
    if dir not in environ['PATH']:
      environ['PATH'] = dir + ';' + environ['PATH']
    lib = cdll.LoadLibrary("libhupf.dll")
else:
  dir = path.abspath(path.dirname(__file__))  
  if version_info.major==2: 
    lib = cdll.LoadLibrary(dir+"/libhupf.so")
  else: #gcc gives platform suffix in Python 3.x
    from os import listdir
    for file in listdir(dir):
      if file.endswith(".so"): break  
    lib = cdll.LoadLibrary(dir+"/"+file)

lib.create_ik_solver.restype = c_void_p
    
class iksolver(object):
  def __init__(self, a,d,theta, alpha, rots):
    global lib
    ct_a = (c_double * 6)(*a)
    ct_d = (c_double * 6)(*d)
    ct_theta = (c_double * 6)(*theta)
    ct_alpha = (c_double * 6)(*alpha)
    ct_rots = (c_bool * 6)(*rots)
    self.iks = lib.create_ik_solver(ct_a,ct_d,ct_theta, ct_alpha, ct_rots)
  def solve(self,ee):
    global lib
    ct_ee = (c_double * 16)(*ee)
    sols = [0]*(6*16)
    c_sols = (c_double * (len(sols)))(*sols)
    nsol = lib.solve_ik(c_void_p(self.iks),ct_ee, c_sols)
    out0 = list(c_sols)
    out = []
    k = 0
    for i in range(nsol):
      sol = []
      for j in range(6):
        sol.append(out0[k])
        k= k+1
      out.append(sol)
    return out
