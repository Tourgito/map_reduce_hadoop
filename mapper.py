#!/usr/bin/env python3

import sys
import io

# input comes from STDIN (standard input)
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='windows-1252')

for line in input_stream:
        # remove leading and trailing whitespace
        line = line.replace('""', '-')
        line = line.replace('" "', '-')
        line = line.replace(' ', '_')
        # split the line into words
        words = line.split()
        # increase counters
        leksi = words[9] + words[10] + words[11] + words[14]

        print ('%s %s' % (leksi,words[68]))
                                        
