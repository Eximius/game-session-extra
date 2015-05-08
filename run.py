
from GameSession import GameSession

import sys

if len(sys.argv) < 2:
    print('usage: FA.exe [args...]')
    sys.exit(0)

from PyQt5.QtCore import *

app = QCoreApplication(sys.argv)

sess = GameSession()

i = 2
while i < len(sys.argv):
    assert sys.argv[i][0] == '/'
    j = i+1
    while j < len(sys.argv) and sys.argv[j][0] != '/':
        j += 1
    sess.addArg(sys.argv[i][1:], sys.argv[i+1:j+1])
sess.start(sys.argv[1])

app.exec_()