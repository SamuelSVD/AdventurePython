#!/usr/bin/env python
import time
location = time.strftime('%b_%d_%Y.log', time.gmtime())
file = open(location, 'a')
file.write('hi')
file.close()