PWDD := $(shell pwd)
BLOCKS := $(shell basename $(PWDD))

# ---- Include Partitioned Makefiles ----

CONFIG = caravel_user_project

export COCOTB_REDUCED_LOG_FMT=1
export PYTHONPATH := $(DESIGNS)/verilog/rtl/wrapped_frequency_counter/frequency_counter/test
export LIBPYTHON_LOC=$(shell cocotb-config --libpython)


include $(MCW_ROOT)/verilog/dv/make/env.makefile
include $(MCW_ROOT)/verilog/dv/make/var.makefile
include $(MCW_ROOT)/verilog/dv/make/cpu.makefile
include $(MCW_ROOT)/verilog/dv/make/sim.makefile

coco_test: frequency_counter.hex
	rm -rf sim_build/
	mkdir sim_build/

	iverilog -Ttyp -DFUNCTIONAL -DSIM -DUSE_POWER_PINS -DUNIT_DELAY=#1 \
	-f$(VERILOG_PATH)/includes/includes.rtl.caravel \
	-f$(USER_PROJECT_VERILOG)/includes/includes.rtl.$(CONFIG) -o sim_build/sim.vvp frequency_counter_tb.v

	TESTCASE=test_start MODULE=test_frequency_counter vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus sim_build/sim.vvp
	! grep failure results.xml
