QUESTA = ~/intelFPGA/22.1std/questa_fse/bin/
SIM ?= modelsim
#SCRIPT_FILE+=./Cocotbwave.do
WAVES=1
GUI=1
TOPLEVEL_LANG=verilog

VERILOG_SOURCES+=$(PWD)/hello_world.sv
VERILOG_SOURCES+=/tools/Xilinx/Vivado/2024.1/data/verilog/src/unisims/*.v
VERILOG_SOURCES+=/home/nf/venv/taylor_maclaurin_atan_proj/cordic_0_sim_netlist.v
VERILOG_SOURCES+=/tools/Xilinx/Vivado/2024.1/data/verilog/src/glbl.v

SIM_ARGS+=glbl

TOPLEVEL=hello_world
MODULE=helloWorld
COCOTB_HDL_TIMEUNIT=1ns        
COCOTB_HDL_TIMEPRECISION=1ns

SIM_COMMAND = vsim

#include $(shell cocotb-config --makefiles)/Makefile.inc
include $(shell cocotb-config --makefiles)/Makefile.sim

