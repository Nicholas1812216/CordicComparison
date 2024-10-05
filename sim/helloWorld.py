import cocotb
import numpy as np
from cocotb.triggers import RisingEdge, Timer, FallingEdge
from cocotb.clock import Clock
from sin_chebyshev import chebyshev_sin
from cocotb.binary import BinaryValue

from fixedpoint import FixedPoint
from math import pi, sin

async def run_reset_routine(dut):
    dut.rst.value = 1
    for _ in range(4):
        await RisingEdge(dut.clk)
    dut.rst.value = 0

async def angles(tb):
    
    tb.dut.datai.value = 0 
    tb.dut.validi.value = 0
    for _ in range(40):
        await RisingEdge(tb.dut.clk)
    
    tb.dut.validi.value = 1
    for i in np.arange(-pi/2, pi/2, 0.1): #only pi/2 max to prevent overflow
        tmpVal = FixedPoint(i, signed = True, m = 3, n = 45)
        tb.dut.datai.value = int(str(tmpVal),16)
        tb.input_list.append(i)
        await RisingEdge(tb.dut.clk)
    await RisingEdge(tb.dut.clk)
    tb.dut.validi.value = 0

async def check_angles(tb, run_length):
    for i in range(run_length): #only pi/2 max to prevent overflow
      await FallingEdge(tb.dut.clk)
      if(tb.dut.valido.value == 1): 
        input_val = tb.input_list.pop(0)
        if input_val < 0:
          chebyshev_mapped_val = input_val + 2 * pi
        else:
          chebyshev_mapped_val = input_val
        theo = sin(input_val)
        python_impl = chebyshev_sin(chebyshev_mapped_val)
        vivado_impl_tmp = BinaryValue(int(tb.dut.datao.value[0:31]))
        if tb.dut.datao.value[0] == 1:
          vivado_impl = int(vivado_impl_tmp.signed_integer)/2**30
        else:
          vivado_impl = int(vivado_impl_tmp) / (2**30)
        
        print("input(radians): ", input_val, "actual: ", theo, "Python chebyshev: ", python_impl, "vivado cordic: ", vivado_impl)
        if theo != 0:
          print(" python imp percent error: ", abs((python_impl - theo) / theo * 100), "vivado Percent error: ", abs((vivado_impl - theo) / theo * 100))


class TB(object):
# The init method of this class can be used to do some setup like logging etc, start the 
# toggling of the clock and also initialize the internal to their pre-reset vlaue.
    def __init__(self, dut):
        self.dut = dut
        self.input_list = []
        # self.log = logging.getLogger('cocotb_tb')
        # self.log.setLevel(logging.DEBUG)
				
				# start the clock as a parallel process.
        cocotb.fork(Clock(dut.clk, 10, units="ns").start())
    

@cocotb.test()
async def test_hello_world(dut):
    tb = TB(dut)
    simclock_cycle_len = 250
    cocotb.start_soon(run_reset_routine(dut))
    cocotb.start_soon(angles(tb))
    cocotb.start_soon(check_angles(tb, simclock_cycle_len))
    
    for _ in range(simclock_cycle_len):
        await RisingEdge(dut.clk)
    


    assert dut.rst.value == 0, "Reset is incorrect! %s != %s" % (str(dut.rst.value), "0")
