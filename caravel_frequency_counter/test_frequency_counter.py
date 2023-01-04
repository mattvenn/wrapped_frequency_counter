import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles, with_timeout
from test_seven_segment import read_segments

# takes ~60 seconds on my PC
@cocotb.test()
async def test_start(dut):
    clock = Clock(dut.clk, 25, units="ns") # 40M
    cocotb.start_soon(clock.start())
    
    dut.RSTB.value = 0
    dut.power1.value = 0;
    dut.power2.value = 0;
    dut.power3.value = 0;
    dut.power4.value = 0;

    await ClockCycles(dut.clk, 8)
    dut.power1.value = 1;
    await ClockCycles(dut.clk, 8)
    dut.power2.value = 1;
    await ClockCycles(dut.clk, 8)
    dut.power3.value = 1;
    await ClockCycles(dut.clk, 8)
    dut.power4.value = 1;

    await ClockCycles(dut.clk, 80)
    dut.RSTB.value = 1

    # start the input signal
    period_us = 4 # 25kHz
    # default update period is 1200 cycles
    input_signal = cocotb.start_soon(Clock(dut.signal, period_us,  units="us").start())

    # wait for the project to become active - time out if necessary - should happen around 165us
    await with_timeout(RisingEdge(dut.active), 600, 'us')

    # let counter settle 
    await ClockCycles(dut.clk, 7000)

    # read the 7 segment display
    reading = await read_segments(dut)
    assert(reading == 25)

