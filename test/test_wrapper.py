import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles

from frequency_counter.test.test_seven_segment import read_segments

@cocotb.test()
async def test_wrapper(dut):
    clock = Clock(dut.wb_clk_i, 10, units="ns")
    cocotb.fork(clock.start())

    # reset but project is inactive
    dut.wb_rst_i <= 1
    await ClockCycles(dut.wb_clk_i, 5)
    dut.wb_rst_i <= 0
    dut.la_data_in <= 0

    # pause
    await ClockCycles(dut.wb_clk_i, 100)

    # activate project
    dut.active <= 1

    # reset it
    dut.la_data_in <= 1 << 0
    await ClockCycles(dut.wb_clk_i, 1)
    dut.la_data_in <= 0 << 0
    await ClockCycles(dut.wb_clk_i, 1)

    await ClockCycles(dut.wb_clk_i, 100)

