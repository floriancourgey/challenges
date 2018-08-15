# G-code encoding
## 1. Info
- https://en.wikipedia.org/wiki/G-code
- http://linuxcnc.org/docs/html/gcode_fr.html
- https://www.ntnu.no/wiki43/display/digilab/Understanding+G-Code
- http://nraynaud.github.io/webgcode/ (online simulator)
## 2. Identify fixed parts
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
## 3. identify dynamic parts
```gcode
G0 # enable rapid mode (don't draw anything)
G52 X9 Y0 # set the origin to (9 0)
X2 Y6 # relatively from the last point (9,0), move last point to (2,6)
G1 # disable rapid mode (now every instruction will drwa a line)
Y5 # relatively from the last point (2,6), draw a line to (0,5)
```
