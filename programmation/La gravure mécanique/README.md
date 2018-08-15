# G-code encoding
1. Info
- https://en.wikipedia.org/wiki/G-code
- http://linuxcnc.org/docs/html/gcode_fr.html
2. Identify fixed parts
- header
```
%
O1234(GRAVURE)
G28G91Z0.Y0.
M6T1
G0G90G54X0.Y0.M3S7500F250.
G43H1Z2.M8
```
- footer
```
G91G28Y0.Z0.M9
M30
%
```
