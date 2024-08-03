onerror {resume}
radix define fixed#30#decimal#signed -fixed -fraction 30 -signed -base signed -precision 6
quietly virtual signal -install /hello_world { /hello_world/datai[47:16]} datai_32
quietly virtual function -install /hello_world -env /hello_world { &{/hello_world/datao[95], /hello_world/datao[94], /hello_world/datao[93], /hello_world/datao[92], /hello_world/datao[91], /hello_world/datao[90], /hello_world/datao[89], /hello_world/datao[88], /hello_world/datao[87], /hello_world/datao[86], /hello_world/datao[85], /hello_world/datao[84], /hello_world/datao[83], /hello_world/datao[82], /hello_world/datao[81], /hello_world/datao[80], /hello_world/datao[79], /hello_world/datao[78], /hello_world/datao[77], /hello_world/datao[76], /hello_world/datao[75], /hello_world/datao[74], /hello_world/datao[73], /hello_world/datao[72], /hello_world/datao[71], /hello_world/datao[70], /hello_world/datao[69], /hello_world/datao[68], /hello_world/datao[67], /hello_world/datao[66], /hello_world/datao[65], /hello_world/datao[64] }} X_32
quietly virtual function -install /hello_world -env /hello_world { &{/hello_world/datao[47], /hello_world/datao[46], /hello_world/datao[45], /hello_world/datao[44], /hello_world/datao[43], /hello_world/datao[42], /hello_world/datao[41], /hello_world/datao[40], /hello_world/datao[39], /hello_world/datao[38], /hello_world/datao[37], /hello_world/datao[36], /hello_world/datao[35], /hello_world/datao[34], /hello_world/datao[33], /hello_world/datao[32], /hello_world/datao[31], /hello_world/datao[30], /hello_world/datao[29], /hello_world/datao[28], /hello_world/datao[27], /hello_world/datao[26], /hello_world/datao[25], /hello_world/datao[24], /hello_world/datao[23], /hello_world/datao[22], /hello_world/datao[21], /hello_world/datao[20], /hello_world/datao[19], /hello_world/datao[18], /hello_world/datao[17], /hello_world/datao[16] }} Y_32
quietly WaveActivateNextPane {} 0
add wave -noupdate /hello_world/clk
add wave -noupdate /hello_world/rst
add wave -noupdate -radix fixed#30#decimal#signed /hello_world/datai_32
add wave -noupdate /hello_world/validi
add wave -noupdate /hello_world/valido
add wave -noupdate -radix fixed#30#decimal#signed /hello_world/X_32
add wave -noupdate -radix fixed#30#decimal#signed /hello_world/Y_32
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {600100 ps} 0}
quietly wave cursor active 1
configure wave -namecolwidth 214
configure wave -valuecolwidth 100
configure wave -justifyvalue left
configure wave -signalnamewidth 1
configure wave -snapdistance 10
configure wave -datasetprefix 0
configure wave -rowmargin 4
configure wave -childrowmargin 2
configure wave -gridoffset 0
configure wave -gridperiod 1
configure wave -griddelta 40
configure wave -timeline 0
configure wave -timelineunits ps
update
WaveRestoreZoom {118579 ps} {914242 ps}
