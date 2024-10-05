
# all: clean build

# clean:
	# @if [ -d "./sim_build" ]; then \
		# echo "Removing ./sim_build directory..."; \
		# rm -r ./sim_build; \

	# fi
	
	# @if [ -f "modelsim.ini" ]; then \
		# echo "Removing modelsim.ini..."; \
		# rm ./modelsim.ini; \
	# fi

# build: 
	
SIM ?= modelsim
#SCRIPT_FILE+=./Cocotbwave.do
WAVES=1
GUI=1
TOPLEVEL_LANG=verilog

VERILOG_SOURCES+=$(PWD)/hello_world.sv
# VERILOG_SOURCES+=/tools/Xilinx/Vivado/2024.1/data/verilog/src/unisims/*.v
# VERILOG_SOURCES+=$(PWD)/cordic_0_sim_netlist.v
VERILOG_SOURCES+=/tools/Xilinx/Vivado/2024.1/data/verilog/src/glbl.v

SIM_ARGS+=glbl

TOPLEVEL=hello_world
MODULE=helloWorld

# SIM_COMMAND = vsim

#include $(shell cocotb-config --makefiles)/Makefile.inc
include $(shell cocotb-config --makefiles)/Makefile.sim

RUN = vsim -c -do "source wave.do"