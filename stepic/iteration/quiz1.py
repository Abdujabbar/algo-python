# your code goes here

import sys
import re
for line in sys.stdin:
    line = line.rstrip()

    r = re.search(r'\\', line)
    if r:
        print(line)





