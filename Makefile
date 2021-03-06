# cocotb setup
export COCOTB_REDUCED_LOG_FMT=1

test_wrapper:
	rm -rf sim_build/
	mkdir sim_build/
	iverilog -o sim_build/sim.vvp -DMPRJ_IO_PADS=38 -s wrapped_frequency_counter -s dump -g2012 wrapper.v test/dump_wrapper.v frequency_counter/src/*.v
	MODULE=test.test_wrapper vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus sim_build/sim.vvp
	! grep failure results.xml

show_wrapper:
	gtkwave wrapper.vcd wrapper.gtkw

