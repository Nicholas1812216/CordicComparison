import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock

from fixedpoint import FixedPoint
from math import pi

async def run_reset_routine(dut):
    for _ in range(4):
        await RisingEdge(dut.clk)
    dut.rst.value = 0

async def angles(dut):
    dut.datai.value = 1
    dut.validi.value = 0
    for _ in range(40):
        await RisingEdge(dut.clk)
    dut.datai.value = int(FixedPoint(pi / 2.0, signed = True, m = 2, n = 46))
    dut.validi.value = 1
    await RisingEdge(dut.clk)
    dut.validi.value = 0

class TB(object):
#The init method of this class can be used to do some setup like logging etc, start the 
#toggling of the clock and also initialize the internal to their pre-reset vlaue.
    def __init__(self, dut):
        self.dut = dut
        #self.log = logging.getLogger('cocotb_tb')
        #self.log.setLevel(logging.DEBUG)
				
				#start the clock as a parallel process.
        cocotb.fork(Clock(dut.clk, 10, units="ns").start())
    

@cocotb.test()
async def test_hello_world(dut):
    tb = TB(dut)
    #cocotb.start_soon(Clock(dut.clk, 1, units="ns").start())
    
    #cocotb.start_soon(run_reset_routine(dut))
    #cocotb.start_soon(angles(dut))

    dut.rst.value = 0
    a = FixedPoint(pi / 2.0, signed = True, m = 2, n = 46)
    dut.datai.value = int(str(a),16)
    dut.validi.value = 1
    
    for _ in range(50):
        await RisingEdge(dut.clk)
    

    #dut.datai.value = FixedPoint(pi / 2.0, signed = True, m = 2, n = 46)
    dut.validi.value = 1
    await RisingEdge(dut.clk)
    dut.validi.value = 0

    for _ in range(5000):
        await RisingEdge(dut.clk)
    


    #assert dut.rst.value == 0, "Reset is incorrect! %s != %s" % (str(dut.rst.value), "0")
