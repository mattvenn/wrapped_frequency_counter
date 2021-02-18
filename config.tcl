# User config
set ::env(DESIGN_NAME) wrapped_frequency_counter

# Change if needed
set ::env(VERILOG_FILES) "$::env(DESIGN_DIR)/wrapper.v \
    $::env(DESIGN_DIR)/frequency_counter/src/edge_detect.v \
    $::env(DESIGN_DIR)/frequency_counter/src/frequency_counter.v \
    $::env(DESIGN_DIR)/frequency_counter/src/seven_segment.v"

set ::env(PL_TARGET_DENSITY) 0.4
set ::env(DIE_AREA) "0 0 300 300"
set ::env(FP_SIZING) absolute

set ::env(SYNTH_DEFINES) "MPRJ_IO_PADS=38"

# Fill this
set ::env(CLOCK_PERIOD) "10"
set ::env(CLOCK_PORT) "wb_clk_i"

set ::env(DESIGN_IS_CORE) 0
set ::env(GLB_RT_MAXLAYER) 5


set filename $::env(DESIGN_DIR)/$::env(PDK)_$::env(STD_CELL_LIBRARY)_config.tcl
if { [file exists $filename] == 1} {
	source $filename
}

