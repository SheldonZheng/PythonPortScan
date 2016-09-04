#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# port_scan.py <host> <start_port>-<end_port>

host = sys.argv[1]
portstrs = sys.argv[2].split('-')

start_port = int(portstrs[0])
end_port = int(portstrs[1])

print (start_port)
print (end_port)
