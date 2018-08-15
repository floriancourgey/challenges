# G-code encoding
1. Info
- https://en.wikipedia.org/wiki/G-code
- http://linuxcnc.org/docs/html/gcode_fr.html
2. Identify fixed parts
- header, it's basically positioning initialisation
```gcode
%
O1234(GRAVURE)
G28G91Z0.Y0. ; G28=goto(0,0), G91=use relative coordinates
M6T1 ; M6=select, T1=tool 1
G0G90G54X0.Y0.M3S7500F250. ; G0=max speed, G90=use abs coord, G54=?,  M3=use clockwise rotation, 
G43H1Z2.M8 ; G43=?, H1=of height 1, Z2=?, M8=start cutting fluid (coolant on)
```
- footer
```gcode
G91G28Y0.Z0.M9 ; M9=stop cutting fluid (coolant off)
M30 ; end of program
%
```
