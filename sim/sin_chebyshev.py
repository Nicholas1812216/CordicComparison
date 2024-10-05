import numpy as np
from fixedpoint import FixedPoint
from math import pi

def arctan_func(x):
  y = 0.8284 * x - .0475 * (4*x**3 - 3*x) + 0.0055* (16*x**5 - 20*x**3 + 5 * x) #'Digitial Signal Processing with Field Programmable Gate Arrays' p.145

  return y
  
def chebyshev_sin(x): #taken from: http://dalrym.pl/notes/chebyshev-approximation.html
  #domain: x in [0,2*pi]
  y = -1.66451778959003 * ((x-pi)/pi)**5 + 4.74829052566064 * ((x-pi)/pi)**3 - 3.09012486790893*((x - pi)/pi)
  return y
  
  
def fixed_point_test():
  qformat = {'signed': True, 'm': 2, 'n': 46}

# A single instance
  # x = FixedPoint(0, **qformat)
  float_val = float(3226589708/(2**46))
  test = (FixedPoint(float_val, signed = True, m = 2, n = 46))
   # FixedPoint(int(tb.dut.datao.value[48:95]), signed = True, m = 2, n = 46)
  return test

if __name__ == "__main__":
  # x_values = np.arange(2*pi,0,-0.1)
  # chebyshev_results = chebyshev_sin(x_values)
  # sin_results = np.sin(x_values)
  # for x,result, sin_res in zip(x_values, chebyshev_results, sin_results):
    # error = (sin_res - result) / result * 100
    # print(f"f({x}) = {result}, actual: {sin_res}")
  print(fixed_point_test())


