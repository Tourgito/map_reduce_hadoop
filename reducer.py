#!/user/bin/env python3i

from operator import itemgetter
import sys

current_word = None
current_ncid = None
word = None
count  = 1


# input comes from STDIN
for line in sys.stdin:
        # remove leading and trailing whitespace


        # parse the input we got from mapper.py
        word, ncid = line.split(' ', 1)

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        if current_word == word:
            current_ncid += ncid
            count += 1
        else:

            if current_word and count > 1 :
                # write result to STDOUT
                print ('%s %s' % (current_word,current_ncid))
                current_ncid = ncid
                current_word = word
                count = 1
# do not forget to output the last word if needed!
if current_word == word and count >1:
print ('%s %s' % (current_word, current_ncid))
                                                                                                                        
