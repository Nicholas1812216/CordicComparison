module hello_world(
           input logic	       clk,
	   input logic	       rst,
	   input logic [47:0]  datai,
	   input logic	       validi,
	   output logic [95:0] datao,
           output logic	       valido);


   cordic_0 DUT(
    .aclk(clk),
    .s_axis_phase_tvalid(validi),  // input wire s_axis_phase_tvalid
    .s_axis_phase_tdata(datai),    // input wire [47 : 0] s_axis_phase_tdata
    .m_axis_dout_tvalid(valido),    // output wire m_axis_dout_tvalid
    .m_axis_dout_tdata(datao) 
    );
   
   
   initial begin
      $dumpfile("wave.vcd");
      $dumpvars;
      
   end
   
endmodule
