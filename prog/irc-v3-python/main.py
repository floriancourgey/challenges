#! /usr/bin/env python3
# coding: utf-8
import sys
sys.path.insert(0, '../..')
from functions import IrcSolver
import base64
import os
from PIL import Image
import pytesseract
from datetime import datetime
from prog.ocr_v3_python.OcrMonotype import OcrMonotype

ocr = OcrMonotype(8, 10, 1, 4, 0, 0, os.path.abspath('dico_8_10.txt'), True)
# ocr.loadFile("results/2019-01-22T234125.310124file.png")
# result = ocr.compute()
# print(result)
# exit()

# 1. base64decode
# 2. find xor key with 8 first chars
# 3. recreate image
# 4. get image text with OCR
def solve(text):
    # text = '2xMXIWF9UEBSQ1lrJT8OGFJDWXRsd0ooVkBZZmzYiNT3Q1lmeScGHhdDWWZsiLW1UrymmWyISkpSvFlmbIjuNv7XWWZssAMOExdx9+Hli0fWY0kjbfb5PDLvmQJ3lwpLDPsqxJNlPFIzH5Dqh3Suy1FyoEyplSsu5p8PmaDgGHgtWrk0JnAQN+hUL/uMx3uMgUHvCDpDUY+ZaYphtCY9/+V+tfTFKYUr5C1y0lvBH669kIG3CkUH7DRxFMB6hnAV/EdqBZK9ff0ucEf0JBqeoyLbemKFTwHtEx5mp38f+MkTu2i65hmMesMS48qNGArxXVsRDYH8n5pkpjCg4LoZ9kd+gTTNAjFxrZVQGm2IaVf9p1hjh3dKSlIKHCgo2Qgq0A=='
    # text = '/TkcCzpNeG10aVJBfg8mNXRpUl43R2IFcGpSTDfooPnRaVJMIhcuMzFpUkw3uJ2YdJatsze4Ymd0llJMN7jGG9j9Ukw3+SsjNT163ZrVU3XwSV4JtEXXHHevQXT0Qkpf9GTv2cB4oCXgRjrQ7iXdBSoXQNZ/Ywiss1uLf9QnrdXZf4MSVNYePuIge+F7ogkZ1AIQGru2Ymo/S1i8B2YLkwrQQBzC+8Xg89c8uuOnCslMqScDdfL7d9CRN9Z3TSZ0POi6v0nYv5CZIxKZXBCbj58PXXmcdcvWcSWlck6KWGH6SG22onPKm2Qo6ATnP0E4sN1amQB+5oYyGsSnrX3wk7uULE2BA3h0CjcDYjdHYmc9LBwImQUC5Q=='
    # 1.
    bytes = base64.b64decode(text)
    #  2. find the key

    PNG_SIG = b'\x89\x50\x4E\x47\x0d\x0a\x1a\x0a'
    # step 1. Find the key from the PNG signature (8 bytes long)
    # with a XOR
    key = ''
    for i, byte in enumerate(PNG_SIG):
        b = byte ^ bytes[i] # XOR the PNG signature with the string bytes
        key += chr(b)
    print('key', key)

    # return key, 'lovelovelove', None

    # 3. create image
    final = bytearray()
    iPng=0
    for byte in bytes:
        ascii = ord(key[iPng]) ^ byte
        final.append(ascii)
        iPng = (iPng+1) % len(PNG_SIG)
    print('final', final)

    filename = 'results/'+datetime.now().isoformat().replace(':', '')+'file.png'
    out_file = open(filename, 'wb') # [w]riting as [b]inary
    out_file.write(final)
    out_file.close()
    # rotate 270
    im = Image.open(filename).transpose(Image.ROTATE_270)
    # convert to gray scale
    gray = im.convert('L')
    # convert to black and white
    bw = gray.point(lambda x: 0 if x<1 else 255, '1')
    bw.save(filename)
    im = bw

    config = ''
    config += ' -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    config += ' --psm 13'
    # config += ' --oem 1'

    # solution = pytesseract.image_to_string(im, config=config)
    ocr.loadFile(filename)
    solution = ocr.compute()[0]
    # print(result)

    return key, solution, im

import irc.client
irc.client.ServerConnection.buffer_class.encoding = 'latin-1' # because of bad non-ascii char

class Solver(IrcSolver):
    key = ''
    solution = ''
    im = None
    def on_join(self, connection, event):
        if self.STEP == 1:
            self.connection.privmsg(self.target, '.challenge_xor_ocr start')
        elif self.STEP == 2:
            print('self.connection.privmsg')
            self.connection.privmsg('#'+self.key, '.challenge_xor_ocr '+self.solution)
            self.im.show()
    def on_privmsg(self, connection, event):
        if self.STEP == 1:
            self.key, self.solution, self.im = solve(event.arguments[0])
            print('key', self.key)
            print('solution', self.solution)
            if len(self.solution) != 12:
                exit('Solution must be 12 char long')
            self.STEP = 2
            self.connection.join('#'+self.key)
            return
        elif self.STEP == 2:
            exit()
    def on_pubmsg(self, connection, event):
        if event.arguments[0] == 'Vous avez mal lu le texte.':
            exit('Vous avez mal lu le texte.')

c = Solver()
c.debug_all_events=True
c.connect_and_start()
