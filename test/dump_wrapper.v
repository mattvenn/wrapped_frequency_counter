module dump();
    initial begin
        $dumpfile ("wrapper.vcd");
        $dumpvars (0, wrapped_frequency_counter);
        #1;
    end
endmodule
