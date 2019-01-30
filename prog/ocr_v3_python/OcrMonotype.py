#! /usr/bin/env python3
# coding: utf-8
from PIL import Image

class OcrMonotype:
    DIC = {} # {A:[bits..], B:[bits..]}
    DIC_1 = '&' # char used in dic to indicate a bit=1
    DIC_0 = '.' # char used in dic to indicate a bit=0 (empty)
    EMPTY = [] # matrix for empty letter

    def __init__(self, X_LTR, Y_LTR, X_ORIGIN, Y_ORIGIN, X_MARGIN, Y_MARGIN, dicPath, addUnknownToDic):
        self.X_LTR = X_LTR # a letter is 8 pixels large
        self.Y_LTR = Y_LTR # a letter is 10 pixels high
        self.X_ORIGIN = X_ORIGIN # the first letter is at (6,8)
        self.Y_ORIGIN = Y_ORIGIN
        self.X_MARGIN = X_MARGIN # no horizontal margin between letters
        self.Y_MARGIN = Y_MARGIN # vertical margin of 5 px (newline)
        for y in range(0, self.Y_LTR):
            self.EMPTY.append([])
            for x in range(0, self.X_LTR):
                self.EMPTY[y].append(False)
        self.dicPath = dicPath
        self.addUnknownToDic = addUnknownToDic
        self.initDic()

    def loadFile(self, filename):
        self.filename = filename
        self.im = Image.open(filename).convert('L')
        print('Loading image', filename, '-', self.im.format, self.im.size, self.im.mode)
        self.X_IMG = self.im.size[0]
        self.Y_IMG = self.im.size[1]
        # get the number of letters to read
        self.Y_NB_LETTERS = int( (self.Y_IMG-self.Y_ORIGIN) / (self.Y_LTR+self.Y_MARGIN) )
        self.X_NB_LETTERS = int( (self.X_IMG-self.X_ORIGIN) / self.X_LTR )
        print('# of lines: '+str(self.Y_NB_LETTERS))
        print('# of letters: '+str(self.X_NB_LETTERS))

    def getMatricesFromImage(self):
        self.linesOfMatrices = [] # each line will be an array of matrices
        # for each line
        for yLetter in range(0, self.Y_NB_LETTERS):
            self.linesOfMatrices.append([])
            y = self.Y_ORIGIN+ yLetter*(self.Y_LTR+self.Y_MARGIN)
            print('* New line n°'+str(yLetter)+' found with y origin: '+str(y))
            # for each letter
            for xLetter in range(0, self.X_NB_LETTERS):
                x = self.X_ORIGIN+ xLetter*self.X_LTR
                matrix = self.letterOrigintoMatrix(x, y)
                self.linesOfMatrices[yLetter].append(matrix)
                # if we have 2 spaces in a row, break
                if xLetter > 1 and self.linesOfMatrices[yLetter][xLetter]==self.EMPTY and self.linesOfMatrices[yLetter][xLetter-1]==self.EMPTY:
                    self.linesOfMatrices[yLetter] = self.linesOfMatrices[yLetter][:-2]
                    break

    def getLettersFromImage(self):
        self.lines = [] # each line will be an array string
        for y,lineOfMatrices in enumerate(self.linesOfMatrices):
            self.lines.append('')
            for x,matrix in enumerate(lineOfMatrices):
                self.lines[y] += self.matrixToLetter(matrix, x, y)
        return self.lines

    def compute(self):
        self.getMatricesFromImage()
        self.getLettersFromImage()
        return self.lines

    def matrixToLetter(self, matrix, x, y):
        ''' convert a matrix to a letter '''
        if matrix == self.EMPTY:
            return ' '
        for letter in self.DIC:
            m = self.DIC[letter]
            if m == matrix:
                return letter
        # if the letter is unknown, write it to the dic
        if self.addUnknownToDic:
            f = open('dico_'+str(self.X_LTR)+'_'+str(self.Y_LTR)+'.txt', 'a')
            f.write('* '+self.filename+', letter ('+str(x)+', '+str(y)+')\n')
            for j in range(0, self.Y_LTR):
                for i in range(0, self.X_LTR):
                    if matrix[j][i]:
                        f.write(self.DIC_1)
                    else:
                        f.write(self.DIC_0)

                f.write('\n')
        # then return '*'
        return '*'

    def letterOrigintoMatrix(self, origX, origY):
        ''' converts the origin of a letter to a matrix '''
        matrix = []

        for y in range(0, self.Y_LTR):
            matrix.append([])
            for x in range(0, self.X_LTR):
                matrix[y].append( self.getBitFromPixel(origX+x,origY+y) )

        return matrix

    def getBitFromPixel(self, x, y):
        ''' return true if pixel(x,y).red>127 '''
        # return self.im.getpixel( (x, y) )[0] > 127 # for "RGB"
        return self.im.getpixel( (x, y) ) > 127 # for "L" luminance (grey scale)

    def initDic(self):
        print('Loading dic', self.dicPath)
        f = open(self.dicPath, 'r')
        i = 0
        lines = f.read().split('\n')
        # for each line (without the last one)
        for i in range(0, len(lines)-1):
            # get the character
            if i % (self.Y_LTR+1) == 0:
                line = lines[i]
                letter = line.strip()[0]
                # print('letter found: '+letter)
                # and add it to the dic, via a matrix of bits
                if letter not in self.DIC:
                    matrix = []
                    for y in range(0, self.Y_LTR):
                        matrix.append([])
                        for x in range(0, self.X_LTR):
                            matrix[y].append( lines[i+1+y][x] == self.DIC_1 )
                    self.DIC[letter] = matrix
        print('OCR dic initialized with '+str(len(self.DIC))+' characters')

# X_LTR, Y_LTR, X_ORIGIN, Y_ORIGIN, X_MARGIN, Y_MARGIN, dicoPath, addUnknownToDic
# ocr = OcrMonotype(8, 10, 5, 8, 0, 5, 'dico_8_10.txt', True)
# ocr.loadFile("samples/2018-09-03T18:05:48.658980file.pngfinal.png")
# ocr.loadFile("samples/2018-09-03T18:06:16.772015file.pngfinal.png")
# ocr.loadFile("samples/2018-09-03T18:06:32.311478file.pngfinal.png")
# ocr.loadFile("samples/2018-09-03T18:06:34.184826file.pngfinal.png")
# ocr.loadFile("samples/2018-09-03T18:06:36.096125file.pngfinal.png")
# result = ocr.compute()
# print(result)
