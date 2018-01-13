#!/bin/python3

import re, urllib, base64

## This file file has been written for decoding
## url encoded and base 64 encoded strings contained
## in a log file. 


filepath 	= "logs-analysis-web-attack.txt"
pattern		= ".*order=([^ ]+)\ .*"

regexp		= re.compile(pattern)

with open(filepath) as fp:
	line = fp.readline()

	while line:
		decodedString = base64.b64decode(urllib.unquote(regexp.match(line).group(1)))
		print(decodedString + "\n")
		line = fp.readline()