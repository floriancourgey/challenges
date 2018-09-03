- Get PNG Signature from https://fr.wikipedia.org/wiki/Portable_Network_Graphics (89 50 4E 47 0D 0A 1A 0A)
- Open it in an hex editor, e.g. HexEdit
1. Extract 3 PNGs
- Look for the Signature (89 50 4E 47 0D 0A 1A 0A), find the 3 PNGs:
- Extract the second one:
![Step 1](./step%201.jpg)
- Check with `file`
![Step 2](./step%202.jpg)
2. Recreate base image
3. Analyze image
![Step 3](./step%203.png)
Images will always:
- have a size of 330x55 px (width x height)
- have 3 lines of text (1=words, 2=key, 3=index)
- have a monotype font, a letter = 8x10
- begin at origin = 5x8
- have a margin of 5 px between 2 lines and no margin between 2 letters
- Download a few samples to work on
3. Execute OCR
- From samples, create a dic to map each character to a 8x10 matrix, e.g for the char '2':
```
2
..&&&&..
.&....&.
.&....&.
......&.
....&&..
...&....
..&.....
.&......
.&......
.&&&&&&.
```
