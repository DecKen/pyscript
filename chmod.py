#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'DecKen'
__date__ = '2014-10-04 16:51'

import os
import sys


def chmod(path, dirmod=775, filemod=644):
    if not os.path.exists(path):
        print "A wrong path"
        exit()
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for d in dirs:
                os.system("chmod %s %s" % (dirmod, os.path.join(root, d)))
            for f in files:
                os.system("chmod %s %s" % (filemod, os.path.join(root, f)))
        print "Done"
    else:
        print "Path must be a direction"


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        chmod(args[1])
    elif len(args) == 4:
        chmod(args[3], args[1], args[2])
    else:
        print "Right order: Command [dirmod filemod] Path"
