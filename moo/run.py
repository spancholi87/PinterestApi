#
# start the server
#

import sys

from bottle import run
from apis_pinterest import setup 

if len(sys.argv) > 2:
  base = sys.argv[1]
  conf_fn = sys.argv[2]
  setup(base,conf_fn)

  run(host='192.168.0.78', port=8080)
else:
  print "usage:", sys.argv[0],"[base_dir] [conf file]"

