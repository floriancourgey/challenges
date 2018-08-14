# python3
from urllib.request import urlopen

content = urlopen("https://www.newbiecontest.org/epreuves/prog/prog11/imgcrypted.png")
bin_data = content.read()
# write whole file
file = open("file.png", "wb")
file.write(bin_data)
file.close()
# write 3 files
chunks = bin_data.split(b'\x89\x50\x4E\x47')
for i,chunk in chunks:
  file = open("file"+str(i)+".png")
  file.write(chunk)
  file.close()
