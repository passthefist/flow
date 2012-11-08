from os import listdir
from os.path import isfile, join, dirname
import inspect

import re

p = dirname(inspect.getfile(inspect.currentframe()))

files = [ f for f in listdir(p) if isfile(join(p,f)) ]

mods = list()

for f in files:
    m = re.match("^(\w+).py$", f)
    if m:
        mod = m.group(1)
        if mod != "__init__":
            mods.append(mod)

__all__ = mods
