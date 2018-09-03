#! /usr/bin/env python3
# coding: utf-8
from vigenere import Vigenere

v = Vigenere('B')
assert v.encrypt('ABCDEF') == 'BCDEFG'
assert v.decrypt('BCDEFG') == 'ABCDEF'
assert v.decrypt(v.encrypt('ABCDEF')) == 'ABCDEF'

v = Vigenere('CISAILLES')
assert v.encrypt('ANIMAUX INHUMAIN CHOSES ENDOMMAGE') == 'CVAMIFI MFJCEAQY NLGUMK EVOZQECOW'
assert v.decrypt('CVAMIFI MFJCEAQY NLGUMK EVOZQECOW') == 'ANIMAUX INHUMAIN CHOSES ENDOMMAGE'
assert v.decrypt(v.encrypt('ANIMAUX INHUMAIN CHOSES ENDOMMAGE')) == 'ANIMAUX INHUMAIN CHOSES ENDOMMAGE'
